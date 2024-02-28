from flask import Flask,request,render_template,url_for
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib as joblib
import os

model=joblib.load('model9.pkl')
#scaler=joblib.load('scaler.save')

app =Flask(__name__)

#IMG_FOLDER=os.path.join('static','IMG')
#app.config['UPLOAD_FOLDER']=IMG_FOLDER


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def home():
    if request.method =='POST':
        jan=request.form['January']
        feb = request.form['February']
        mar = request.form['March']
        apr = request.form['April']
        may = request.form['May']
        jun = request.form['June']
        jul = request.form['July']
        aug = request.form['August']
        sep = request.form['September']
        oct = request.form['October']
        nov = request.form['November']
        dec = request.form['December']
        kin = request.form['Kind']

        data = np.array([[jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec,kin]])
       # x = scaler.transform(data)
        print(data)
        prediction = model.predict(data)
        print(prediction)
        #image=prediction[0]+'.png'
        #image=os.path.join(app.config['UPLOAD_FOLDER'],image)
    return render_template('index.html',prediction=prediction[0])


if __name__ == '__main__':
    app.run(debug=True)
