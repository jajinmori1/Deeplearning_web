from flask import Flask, request, Response, render_template
from flask_sqlalchemy import SQLAlchemy
import tensorflow as tf
import numpy as np
import os
from models import db, Patient

app = Flask(__name__)
model = tf.keras.models.load_model('apgar_model.h5')




@app.route('/')
def main():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    data1 = request.form['CSEC_DISTRESS']
    data2 = request.form['BABY_WEIGHT']
    data3 = request.form['임신말기정밀_AC']
    data4 = request.form['임신말기정밀_AFI']
    data5 = request.form['Cs_Ix_malpresentation']
    data6 = request.form['임신후기정밀_EBW']
    data7 = request.form['HT_DEL']
    data8 = request.form['SBP']
    data9 = request.form['임신말기정밀_FL']
    
    
    patient_data = Patient(CSEC_DISTRESS=data1, BABY_WEIGHT=data2, 임신말기정밀_AC=data3, 임신말기정밀_AFI=data4, Cs_Ix_malpresentation=data5, 임신후기정밀_EBW=data6, HT_DEL=data7, SBP=data8, 임신말기정밀_FL=data9)
    
    db.session.add(patient_data)
    db.session.commit()
    
    arr = np.array([[int(data1),int(data2),int(data3),int(data4),int(data5),int(data6),int(data7),int(data8),int(data9)]])
    pred = model.predict(arr)
    arg_results = np.argmax(pred, axis=1)

    result = "%s" % (arg_results)


    return render_template('index.html', prediction=result)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ojt_restapi:ojt!1234@surfinn.innerwave.co.kr:13306/ojt_restapi'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'


db.init_app(app)


with app.app_context():
    db.create_all()


# start flask app
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
