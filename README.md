# 🚀 GPU-Accelerated ETL Pipeline for 211M Rows (NYC Taxi Dataset)
### GPU加速による 2.1 億行のデータクレンジングと統計分析パイプライン

## 📌 Project Overview / プロジェクト概要
このプロジェクトは、NVIDIA GeForce RTX 5090 の 32GB VRAM を活用し、2 億行を超える大規模なタクシー乗車データを 1 分以内で高速にクレンジング・分析するパイプラインを構築したものです。
This project leverages NVIDIA GeForce RTX 5090 (32GB VRAM) to process and analyze over 211 million rows of taxi trip data in under 1 minute using GPU-accelerated computing.

## ⚡ Key Achievements / 実績数値 (2026-02-13 更新)
* **Processing Scale (処理規模)**: 211,401,886 rows (約 2.1億行)
* **Processing Time (処理時間)**: 32.21 seconds (Full ETL & Statistics)
* **Data Cleaning (データクレンジング)**: 1,044,904 anomaly records identified and removed.
    * 運賃 $0 以下のデータや $1,000 を超える異常値を正確に除外。

## 📈 Performance Benchmarks / パフォーマンス詳細

### Yearly Processing Timeline / 年次処理タイムライン
RTX 5090 の 32GB VRAM を活用し、各年次データのロードから最終集計までを以下のタイムラインで実行しました。

| Phase / 年次 | Processing Time / 処理時間 | Total Rows / 累計行数 |
| :--- | :--- | :--- |
| 2019年分追加 | 2.38s | 84,598,444 |
| 2020年分追加 | 1.56s | 109,247,536 |
| 2021年分追加 | 4.43s | 140,151,844 |
| 2022年分追加 | 5.72s | 179,807,942 |
| 2023年分追加 | 6.36s | 211,401,886 |
| **精密分析 & 統計** | **32.21s** | **211,401,886** |

### Process Performance / プロセス別性能
| Process (処理内容) | Performance (性能) |
| :--- | :--- |
| Data Load (2.1億行) | ~20.0 seconds |
| Data Cleansing (104万件除外) | < 1.0 second |
| Statistical Aggregation (by Vendor) | < 1.0 second |

## 🛠 Tech Stack / 使用技術
* **Hardware**: NVIDIA GeForce RTX 5090 (32GB VRAM)
* **OS/Env**: WSL2 (Ubuntu 24.04), Python 3.10
* **Library**: NVIDIA RAPIDS (cuDF) - GPU-parallelized data processing
* **Data Warehouse**: Snowflake (Planned for hybrid cloud architecture)

## 🔍 Key Insights / データの洞察
* **データ品質**: 全体の約 0.49% に致命的な異常値（マイナス運賃等）が含まれていることを特定。
* **ベンダー分析**: クレンジング後の正確なデータに基づき、VendorID ごとの平均運賃や中央値を瞬時に算出。

## 💡 Cost Optimization Strategy / コスト削減提案
重い前処理（ETL）をローカルの GPU 環境で完遂させることで、クラウド（Snowflake 等）へのデータロード量を最適化し、クラウドコンピューティングコストを大幅に削減するハイブリッド構成を提案可能です。
