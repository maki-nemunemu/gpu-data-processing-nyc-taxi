# 🚀 GPU-Accelerated ETL Pipeline for 211M Rows (NYC Taxi Dataset)
### 2億1,100万行のビッグデータを RTX 5090 で 30秒クレンジング

## 📌 Project Overview / プロジェクト概要
このプロジェクトは、個人環境最高峰の演算能力を持つ **NVIDIA GeForce RTX 5090** を活用し、2億行を超える膨大なタクシー乗車データを秒単位でクレンジング・分析するパイプラインを構築したものです。
圧縮された 3.1GB のデータを、メモリ上で 20.5GB の生データへと高速展開し、ノイズ除去から統計算出までを完遂します。

## ⚡ Key Achievements / 実績数値 (2026-02-13 更新)
* **Processing Scale (処理規模)**: 211,401,886 rows
* **Storage Efficiency (圧縮効率)**: **3.1 GB on disk** (Compressed Parquet)
* **In-Memory Scale (処理容量)**: **20.53 GB in VRAM** (Uncompressed)
* **Total Processing Time (総処理時間)**: **32.21 seconds** (Full ETL & Statistics)
* **Data Integrity (データ品質)**: 1,044,904件の異常レコード（運賃不正等）を特定し、自動除去。

## 📈 Performance Benchmarks / パフォーマンス詳細



### Yearly Processing Timeline / 年次処理タイムライン
RTX 5090 の 32GB VRAM を活用し、2.1 億行のロードから最終集計までを以下の速度で実行しました。

| Phase / 年次 | Processing Time / 処理時間 | Total Rows / 累計行数 | VRAM Usage (推定) |
| :--- | :--- | :--- | :--- |
| 2019年分追加 | 2.38s | 84,598,444 | 8.21 GB |
| 2020年分追加 | 1.56s | 109,247,536 | 10.61 GB |
| 2021年分追加 | 4.43s | 140,151,844 | 13.61 GB |
| 2022年分追加 | 5.72s | 179,807,942 | 17.46 GB |
| 2023年分追加 | 6.36s | **211,401,886** | **20.53 GB** |
| **精密分析 & 統計** | **32.21s** | **211,401,886** | (Total) |

### Process Performance / プロセス別性能
| Process (処理内容) | Performance (性能) |
| :--- | :--- |
| Data Load (3.1GB → 20.5GB) | ~20.0 seconds |
| Data Cleansing (104万件除外) | < 1.0 second |
| Statistical Aggregation (by Vendor) | < 1.0 second |

## 🛠 Tech Stack / 使用技術
* **GPU**: NVIDIA GeForce RTX 5090 (32GB VRAM)
* **OS/Env**: WSL2 (Ubuntu 24.04), Python 3.10
* **Library**: NVIDIA RAPIDS (cuDF) - GPU並列データ処理
* **Data Warehouse**: Snowflake (ハイブリッド・クラウド連携を想定)

## 🔍 Key Insights / データの洞察
* **圧縮・展開効率**: ディスク上の 3.1GB が VRAM 上で 20.5GB に拡大。
    * 一般的な PC（メモリ 16GB 等）ではメモリ不足で処理不能な領域を、32GB VRAM 環境で安定処理。
* **異常値分析**: 全体の約 0.49%（104万件）に致命的な異常値が含まれていることを特定し、データの信頼性を担保。

## 💡 Cost Optimization Strategy / コスト削減提案
クラウド（Snowflake 等）へのデータロード前に、ローカルの GPU 環境で「重い前処理（ETL/ELT）」を完遂させることで、クラウド側のコンピューティングコストとストレージコストを大幅に削減するハイブリッド構成を提案可能です。
