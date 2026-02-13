import cudf
import os
import time


def vram_test():
    YEARS = [2019, 2020, 2021, 2022, 2023]
    DATA_DIR = "data"
    gdf_total = None
    all_gdfs = [] # 効率化のためのリスト

    TARGET_COLUMNS = [
        'VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 
        'passenger_count', 'trip_distance', 'RatecodeID', 
        'PULocationID', 'DOLocationID', 'payment_type', 
        'fare_amount', 'tip_amount', 'total_amount'
    ]

    print(f"--- RTX 5090 VRAM 負荷テスト開始 (全容量: 32GB) ---")

    for year in YEARS:
        files = [os.path.join(DATA_DIR, f"yellow_tripdata_{year}-{m:02d}.parquet") for m in range(1, 13)]
        valid_files = [f for f in files if os.path.exists(f)]

        if not valid_files:
            continue

        print(f"\n【{year}年分を追加中...】")
        start_time = time.time()

        for f in valid_files:
            try:
                gdf_month = cudf.read_parquet(f, columns=TARGET_COLUMNS)
                all_gdfs.append(gdf_month) # リストに追加していく
            except Exception as e:
                print(f"   - ⚠️ ファイル {os.path.basename(f)} の読み込みに失敗: {e}")

        # 年ごとに一旦合体させて、現在のメモリ状況を確認
        gdf_total = cudf.concat(all_gdfs)
        
        current_vram_gb = gdf_total.memory_usage(deep=True).sum() / (1024**3)
        print(f"   - 処理時間: {time.time() - start_time:.2f} 秒")
        print(f"   - 現在の総行数: {len(gdf_total):,}")
        print(f"   - 推定 VRAM 占有量: {current_vram_gb:.2f} GB")

        if current_vram_gb > 28:
            print("🛑 警告: VRAM が限界(32GB)に近づいています！")
            break

    # --- 分析フェーズ：データクレンジング版 ---
    print("\n【データクレンジングと精密分析を開始】")
    start_analysis = time.time()

    # 異常値のフィルタリング（0円より大きく1000ドル以下に限定）
    gdf_clean = gdf_total[
        (gdf_total['fare_amount'] > 0) & 
        (gdf_total['fare_amount'] <= 1000)
    ]

    # クリーンなデータで集計
    summary = gdf_clean.groupby('VendorID').agg({
        'fare_amount': ['min', 'mean', 'median', 'max', 'count']
    })

    print(summary.round(2))

    # ファイル保存
    summary.to_csv("taxi_analysis_clean.csv")
    print(f"   - 精密分析完了まで: {time.time() - start_analysis:.2f} 秒") 

    # --- データ規模の統計出力 ---
    print("\n--- データ規模の比較統計 ---")
    print(f"【レコード数】")
    print(f"   - 元のデータ (gdf_total): {len(gdf_total):,d} 行")
    print(f"   - 掃除後のデータ (gdf_clean): {len(gdf_clean):,d} 行")
    print(f"   - 削除された異常値: {len(gdf_total) - len(gdf_clean):,d} 行")

    print(f"\n【カラム数】")
    print(f"   - 元のデータ (gdf_total): {len(gdf_total.columns)} 列")
    print(f"   - 掃除後のデータ (gdf_clean): {len(gdf_clean.columns)} 列")

if __name__ == "__main__":
    vram_test()