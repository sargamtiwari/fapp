from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
 import pandas as pd
   #import matplotlib.pyplot as plt
   dfinterndata=pd.read_csv('https://github.com/sargamtiwari/fapp/blob/master/interns.csv',sep=',', parse_dates=['YEAR'],index_col='YEAR')
   print(dfinterndata)
   #plt.plot(dfinterndata)
   train =dfinterndata[:int(0.8*(len(dfinterndata)))]
   valid = dfinterndata[int(0.8*(len(dfinterndata))):]
   from statsmodels.tsa.vector_ar.var_model import VAR
   model = VAR(endog=train)
   model_fit = model.fit()
   prediction = model_fit.forecast(model_fit.y, steps=2)
   #print(prediction)
   cols=dfinterndata.columns
   #print(cols)
   interns = pd.DataFrame(index=range(0,len(prediction)),columns=[cols])
   for j in range(0,10):
    for i in range(0, len(prediction)):
       interns.iloc[i][j] =round( prediction[i][j])
  
   df_list = interns.values.tolist()
   JSONP_data = jsonify(df_list)
   return JSONP_data

if __name__ == '__main__':
  app.run(host= '0.0.0.0')
