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
@app.route("/eng")
def hello2():
   import pandas as pd
   
   #Pridiction about engineers and senior enginiors
   dfengg=pd.read_csv('Engineer and Senior Engineer.csv',sep=',', parse_dates=['YEAR'],index_col='YEAR')
  # print(dfengg)
   train_engineers_and_sr_engg =dfengg[:8]
   valid_engineers_and_sr_engg = dfengg[8:]
   from statsmodels.tsa.vector_ar.var_model import VAR
   model = VAR(endog=train_engineers_and_sr_engg)
   model_fit = model.fit()
   pre = model_fit.forecast(model_fit.y, steps=2)
   print(pre)
   coles=dfengg.columns
   print(coles)
   engineers_and_sr_engg = pd.DataFrame(index=range(0,len(pre)),columns=[coles])
   for j in range(0,10):
     for i in range(0, len(pre)):
      engineers_and_sr_engg.iloc[i][j] =round( pre[i][j])
   df_list = engineers_and_sr_engg .values.tolist()
   JSONP_dataengineerse = jsonify(df_list)
   return  JSONP_dataengineerse
    
    

if __name__ == '__main__':
  app.run(host= '0.0.0.0')
