# Homework 2 — Tooling Setup

## 📌 Objective
Set up a reproducible Python project scaffold with virtual environments, secrets management, Jupyter integration, and GitHub version control.

---

## ✅ Tasks Completed
- **Environment setup**  
  Created an isolated Python environment (`conda` or `venv`) and installed required packages:
  - `python-dotenv`
  - `numpy`
  - `jupyter`

- **Project scaffold**  
  Created the following structure:

- **Secrets management**  
- Copied `.env.example` → `.env`
- Added sample values:
  ```ini
  API_KEY=dummy_key_123
  DATA_DIR=./data
  ```
- Added `.env` to `.gitignore` to avoid committing secrets.

- **Config helper**  
Implemented `src/config.py` with helper functions:
- `load_env()` → loads `.env`
- `get_key()` → retrieves secrets safely

- **Jupyter check**  
Verified environment by creating `notebooks/00_project_setup.ipynb` with:
- Title: *Environment & Config Check*
- Code that loads `.env`, checks `API_KEY`, and runs a simple NumPy array operation.

- **Dependencies frozen**  
Saved all dependencies to `requirements.txt` using:
```bash
pip freeze > requirements.txt

--- 

## 📂 Folder Structurehomework5/
homework2/
│── data/                # data folder (gitignored)
│── notebooks/
│    └── 00_project_setup.ipynb
│── src/
│    └── config.py
│── .env                 # local secrets (not committed)
│── .env.example         # template with dummy values
│── requirements.txt
│── README.md
