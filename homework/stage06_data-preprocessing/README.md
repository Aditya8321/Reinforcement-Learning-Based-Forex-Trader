## 📌 Objective
Explore and implement common preprocessing techniques including missing value handling, visualization, and feature scaling.

---

## ✅ Tasks Completed
- **Dataset Generation**
  - Generated a sample dataset and saved it as instructor_dirty.csv

- **Missing values**
  - Identified missing values in numerical and categorical features.
  - Strategies discussed: dropping, imputation, or domain-driven filling.

- **Scaling features**
  - Implemented **Min-Max Scaling** and **Standard Scaling**.
  - Compared transformations and preserved feature distributions.

- **Utilities**
  - Centralized reusable cleaning functions in `src/cleaning.py`.
  - Imported via:
    ```python
    from src import cleaning
    ```

---

## 📂 Folder Structure
homework6/
│── notebooks/stage06_data-preprocessing_homework-starter.ipynb
│── src/
│ ├── init.py
│ └── cleaning.py
│── data/ 
│ ├── processed/instructor_cleaned.csv
│ └── instructor_dirty.csv
│── README.md