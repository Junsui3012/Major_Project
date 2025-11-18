import pandas as pd
import joblib
import os

dir = os.path.dirname(os.path.abspath(__file__))
f_path= os.path.join(dir, "model.joblib")
print(f_path)

model = joblib.load(f_path)

res = model.predict(pd.DataFrame({'Rainfall_mm' : [150], 
                            'Temperature_Celsius' : [30], 
                            'Fertilizer_Used' : [1], 
                            'Irrigation_Used' : [1]
                            }))
print(res)