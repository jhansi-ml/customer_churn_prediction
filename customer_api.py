from fastapi import FastAPI
from pydantic import BaseModel,Field
import pandas as pd
import joblib
import sqlite3
import json
from datetime import datetime

#create Database
conn=sqlite3.connect("customer_churn.db",check_same_thread=False)
cursor=conn.cursor()
#create table
cursor.execute('''CREATE TABLE IF NOT EXISTS churn_predictions (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               input TEXT,
               prediction INTEGER,
               probability REAL,
               created_at TEXT
               )'''
              )
conn.commit()

model=joblib.load("model.pkl")

app=FastAPI()

class Churn(BaseModel):
    gender: str = Field(..., example="Female")
    SeniorCitizen: int = Field(..., example=0)
    Partner: str = Field(..., example="Yes")
    Dependents: str = Field(..., example="No")         
    tenure: int = Field(..., example=42)            
    PhoneService: str = Field(..., example="No")       
    MultipleLines: str = Field(..., example="No")        
    InternetService: str = Field(..., example="Fiber optic")    
    OnlineSecurity: str = Field(..., example="No")   
    OnlineBackup: str = Field(..., example="Yes")       
    DeviceProtection: str = Field(..., example="Yes")
    TechSupport: str = Field(..., example="Yes")
    StreamingTV: str = Field(..., example="No")
    StreamingMovies: str = Field(..., example="No")
    Contract: str = Field(..., example="One year")
    PaperlessBilling: str = Field(..., example="Yes")
    PaymentMethod: str = Field(..., example="Electronic check")
    MonthlyCharges: float = Field(..., example=54.5)
    TotalCharges: float = Field(..., example=1900.0)
    

@app.get("/")
def home():
    return {"message":"Prediction of churn model is running"}

@app.get("/sample_input")
def sample_input():
     return {
        "sample_input": {
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
            "TotalCharges": 151.65},
         "message":{"you can copy and paste above sample input"}
        }
         
@app.post("/predict")
def prediction(data:Churn):
    df=pd.DataFrame([data.dict()])
    pred=int(model.predict(df)[0])
    prob=float(model.predict_proba(df)[0][1])

    #insert into DataBase
    cursor.execute('''INSERT INTO churn_predictions (input,prediction,probability,created_at) VALUES(?,?,?,?)''',             
                   (json.dumps(data.dict()),
                    pred,
                    prob,
                    datetime.now().isoformat())
                  )
    conn.commit()
    return {"prediction":pred,
            "probability":prob}
       
#view logs
@app.get("/logs")
def get_logs():
    cursor.execute("SELECT *FROM churn_predictions ORDER BY id DESC")
    rows=cursor.fetchall()
    #converting database tuple into clean json response which is readable
    result=[]
    for row in rows:
        result.append({
        "id":row[0],
        "input":json.loads(row[1]),
        "prediction":row[2],
        "probability":row[3],
        "time":row[4]
        })
    return {
        "total_rows":len(result),
        "rows":result
    }
    