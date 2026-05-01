#Tele_customer_churn_prediction 

**📌 Overview**  
This project is an end-to-end Machine Learning application that predicts whether a telecom customer is likely to churn (leave the service) or not.

**It includes:**  
Data preprocessing & feature engineering  
Model training & evaluation  
REST API development using FastAPI  
Deployment on Render  
Prediction logging using SQLite  

**🚀 Live Demo**   
👉 https://customer-churn-prediction-pm2f.onrender.com/  

👉 API Documentation (Swagger UI):  
👉 https://customer-churn-prediction-pm2f.onrender.com/docs  

**🛠️ Tech Stack**  
Python  
Pandas / NumPy  
Scikit-learn  
FastAPI  
SQLite  
Joblib  
Render (Deployment)  

**Project structure**  
📁customer_churn.ipynb       #Model training script    
📁customer_api.py            #FastAPI app    
📁model.pkl                  #Trained ML model    
📁predictions.db             #SQLite database  
📁requirement.txt            #required libraries  

**Model Details**   
Problem Type: Binary Classification  
Algorithm: Logistic Regression Model      

**Model performance**  
ROC-AUC Score: 0.76  
Suitable for identifying high-risk churn customers

**Sample input and output**  
Input 
{  
   "gender": "Male",  
            "SeniorCitizen": 0,  
            "Partner": "Yes",  
            "Dependents": "No",  
            "tenure": 2,  
            "PhoneService": "No",  
            "MultipleLines": "No",  
            "InternetService": "DSL",  
            "OnlineSecurity": "No",  
            "OnlineBackup": "Yes",  
            "DeviceProtection": "Yes",  
            "TechSupport": "Yes",  
            "StreamingTV": "No",  
            "StreamingMovies": "No",  
            "Contract": "Month-to-month",  
            "PaperlessBilling": "Yes",  
            "PaymentMethod": "Bank transfer (automatic)",  
            "MonthlyCharges": 70.70,  
            "TotalCharges": 151.65  
            }   
Output   
{  
  "prediction":1,  
  "probability":0.6 
}  
