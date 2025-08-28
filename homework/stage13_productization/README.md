## 📌 Objective
Build, save, and serve a simple Linear Regression model using Flask and Streamlit, including API endpoints and an interactive dashboard.

---

## ✅ Tasks Completed
- **Dataset Generation**
  - Generated synthetic regression data with 2 features using `sklearn.datasets.make_regression`.
  
- **Model Training**
  - Trained a `LinearRegression` model on the generated data.
  - Saved the trained model to `model/model.pkl` using `joblib`.
  
- **Utilities**
  - Created `src/utils.py` with reusable functions such as `calculate_metrics`.
  - Example usage:
    ```python
    from src.utils import calculate_metrics
    metrics = calculate_metrics([row[0] for row in X], y)
    ```

- **Flask API**
  - Implemented endpoints for predictions and a demo plot:
    - `GET /predict/<input1>` → Single input prediction
    - `GET /predict/<input1>/<input2>` → Two input prediction
    - `POST /predict` → JSON payload prediction
    - `GET /plot` → Demo plot rendered in HTML
  - Home page with links to all routes.

- **Streamlit Dashboard**
  - Interactive app for user inputs for features and live predictions.
  - Launched via:
    ```bash
    streamlit run flask_streamlit/app_streamlit.py
    ```

---

## 📂 Folder Structure
stage13_productization/
│── model/
│   └── model.pkl
│── src/
│   └── utils.py
│── flask_streamlit/
│   ├── app.py
│   └── app_streamlit.py
│── requirements.txt
│── README.md

---

## ⚙️ Usage
1. **Flask API**
    ```bash
    python flask_streamlit/app.py
    ```
    Access API at `http://127.0.0.1:5000/`.

2. **Streamlit Dashboard**
    ```bash
    streamlit run flask_streamlit/app_streamlit.py
    ```
    Interact with the model via the browser.

---

## 📝 Notes
- Model trained on synthetic data for demonstration purposes.
- Both Flask API and Streamlit dashboard are independent; Flask must be running to make API requests.
- Environment dependencies captured in `requirements.txt`.
