# Homework 5 — Data Storage

## 📌 Objective
Implement a reproducible storage layer using CSV + Parquet formats, environment-driven paths, and validation utilities.

---

## ✅ Tasks Completed
- **Save in two formats**  
  Data saved to:
  - `data/raw/` as CSV  
  - `data/processed/` as Parquet  
  using `DATA_DIR_RAW` and `DATA_DIR_PROCESSED` from `.env` in the root folder.

- **Reload and validate**  
  Confirmed shape matches and dtypes (`exchange`, `date_time`, `bid`, `ask`) after reloading.

- **Utilities implemented**  
  - `write_df(df, path)` → saves DataFrames to CSV/Parquet.  
  - `read_df(path)` → loads DataFrames, auto-parses `date` columns, handles missing parquet engines.

- **Documentation**  
  Folder structure and design choices are described here.

---

## 📂 Folder Structurehomework5/
│── notebooks/stage05_data_storage.ipynb
│── data/
│ ├── USD_ZAR_2025_07.zip
│ ├── raw/USD_ZAR_2025_07.csv
│ ├── raw/util_20250816-13461.csv
│ ├── processed/USD_ZAR_2025_07.csv
│ └── processed/utils_20250816-134641.parquet
│── README.md