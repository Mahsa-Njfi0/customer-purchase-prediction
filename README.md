# 🛒 Customer Purchase Prediction  
Predicting whether a customer will return next month using transactional retail data.

## 📌 Project Overview  
This project builds a machine learning model that predicts whether a customer will make a purchase in the following month.  
It uses real-world retail transaction data and applies feature engineering techniques such as:

- **RFM (Recency, Frequency, Monetary)**
- **Behavioral features** (average basket size, average unit price, product diversity)
- **Customer‑month purchase patterns**

The goal is to help businesses identify customers at risk of churn and target them with retention strategies.

---

## 🚀 Key Features  
- Clean, modular project structure using a `src/` folder  
- Professional feature engineering pipeline  
- Clear target variable creation (customer return next month)  
- Machine learning model (Random Forest)  
- Evaluation metrics for imbalanced classification  
- GitHub‑ready notebook and utilities  

---

## 🧠 Project Workflow  
1. **Data Cleaning**  
2. **Feature Engineering**  
   - RFM features  
   - Behavioral features  
3. **Target Variable Creation**  
4. **Merge Features + Target**  
5. **Model Training (Random Forest)**  
6. **Evaluation**  

---

## 📊 Model Performance  
The Random Forest model shows strong performance on the positive class (customers who return):

| Metric | Class 1 (Return) |
|--------|------------------|
| Precision | 0.69 |
| Recall | 0.79 |
| F1‑Score | 0.74 |

This indicates the model is effective at identifying returning customers.

---

## 🗂 Project Structure  

customer-purchase-prediction/

│

├── notebooks/

│   └── retail_purchase_prediction.ipynb

│

├── src/

│   └── utils.py

│

├── data/

│   └── (raw data not included)

│

├── results/

│   └── model_metrics.txt (optional)

│

└── README.md



---

## 🛠 Technologies Used  
- Python  
- Pandas  
- NumPy  
- Scikit‑learn  
- Jupyter Notebook  

---

## 📬 Contact  
If you’d like to discuss this project or my work in data science, feel free to connect with me on LinkedIn.

