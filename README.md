# customer-purchase-prediction

This project predicts whether a customer will return to purchase in the next month using real retail transaction data.  
It combines RFM (Recency, Frequency, Monetary) features with additional behavioral metrics to build a practical, business‑focused machine learning model.

The goal is to help retail teams identify customers at risk of churn and take proactive action such as targeted promotions, personalized emails, or loyalty incentives.

The project is designed to be clear, well‑structured, and easy to follow — ideal for showcasing end‑to‑end data science skills in a real business context.


---

## Dataset Description

This project uses the **Online Retail** dataset, a real transactional dataset containing:

- Customer purchases from a UK-based online store  
- Invoice-level transaction records  
- Product descriptions and quantities  
- Unit prices  
- Customer IDs  
- Timestamps for each purchase  

The dataset spans **2010–2011** and includes thousands of customers and tens of thousands of transactions.  
It is widely used for customer segmentation, RFM analysis, and churn prediction tasks.

For this project, the dataset is stored in the `data/` folder of the repository.


---

## Business Problem

Retail businesses lose significant revenue when customers stop returning.  
Understanding **which customers are likely to return next month** helps teams:

- Reduce churn  
- Target promotions more effectively  
- Personalize marketing  
- Improve customer lifetime value  

This project builds a machine learning model that predicts whether a customer will return in the next month based on their past purchasing behavior.


---

## Feature Engineering

To capture customer behavior, the following features were created:

### **RFM Features**
- **Recency** — days since last purchase  
- **Frequency** — number of unique invoices  
- **Monetary** — total spending  

### **Behavioral Features**
- **AvgBasketSize** — average quantity per transaction  
- **AvgUnitPrice** — average price of items purchased  
- **UniqueProducts** — number of distinct products purchased  

These features help the model understand purchasing intensity, price sensitivity, and product diversity — all strong indicators of customer loyalty.


---

## Modeling Approach

The modeling pipeline includes:

1. Train-test split with stratification  
2. Feature scaling using StandardScaler  
3. Random Forest classifier with class balancing  
4. Evaluation using precision, recall, and F1-score  

Multiple models were tested, but Random Forest provided the best balance between performance and interpretability.


---

## Results

The final model achieved:

| Metric | Class 0 (Churn) | Class 1 (Return) |
|--------|------------------|------------------|
| Precision | 0.47 | 0.72 |
| Recall | 0.41 | 0.77 |
| F1-score | 0.44 | 0.74 |

- **Overall accuracy:** 0.65  
- **Macro F1:** 0.59  

The model performs strongly on predicting returning customers and provides meaningful signals for churn prediction — a significant improvement over baseline models.


---

## Feature Importance

The Random Forest model highlights the following features as most important:

1. **Recency**  
2. **Frequency**  
3. **Monetary**  
4. **UniqueProducts**  
5. **AvgBasketSize**  
6. **AvgUnitPrice**

These insights help explain customer behavior and guide business decisions.


---

## Business Insights

Based on the model and feature importance:

- Customers who purchased **recently** are far more likely to return.  
- Higher **frequency** and **monetary** value indicate strong loyalty.  
- Customers who buy a **wide variety of products** tend to stay engaged.  
- Low basket size and low spending may signal early churn risk.  

Retail teams can use these insights to:

- Target at-risk customers with personalized offers  
- Reward high-value customers  
- Improve product recommendations  
- Design loyalty programs based on behavior patterns  


---

## Next Steps

Future improvements could include:

- Adding time-between-purchases features  
- Using XGBoost or LightGBM for higher performance  
- Applying SMOTE to improve class 0 recall  
- Building a dashboard for business users  
- Deploying the model as an API  

These enhancements would make the project even more production-ready.


---

## Project Structure

customer-purchase-prediction/
│
├── data/
│   └── Online Retail.xlsx
│
├── notebooks/
│   └── retail_churn_model.ipynb
│
├── src/
│   └── utils.py   (optional)
│
├── README.md
│
└── requirements.txt


This structure keeps the project clean, modular, and easy to navigate.


---

## Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib / Seaborn  
- Jupyter Notebook  


---

## Author

**Mahsa**  
Data Science & Machine Learning Enthusiast  
Passionate about building practical, business-focused ML solutions.

