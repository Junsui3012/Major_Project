import pandas as pd
import joblib
import os
import warnings
# Make sure to download the requirements.txt in an appopriate virtual env .venv

# Silent the warnings
warnings.filterwarnings("ignore")

# Make sure to put the model in the same directory as the calling script before running the code below
dir = os.path.dirname(os.path.abspath(__file__))
f_path= os.path.join(dir, "model.joblib")
print(f_path)

# Loading model object in a variable
model = joblib.load(f_path)

# Calling predict method.
res = model.predict(pd.DataFrame({'Rainfall_mm' : [150],        # 1st Feature is the average rainfall in past month in mm
                            'Temperature_Celsius' : [30],       # 2nd Feature is the average temperature in past month in celsius
                            'Fertilizer_Used' : [1],            # 3rd Feature is a 0 or 1 value if any fertilizer was used or not
                            'Irrigation_Used' : [1]             # 4th Feature is a 0 or 1 value if any Irrigation was used or not
                            }))


"""
Alternate caliing method:
res = model.predict([[150, 30, 1, 1]])
"""

# Returns an array of n results for n inputs
print(res[0])