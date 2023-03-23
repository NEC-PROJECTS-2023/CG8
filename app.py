from flask import Flask , request ,url_for , render_template
import numpy as np
import pickle


sc = pickle.load(open('sc.pkl' , 'rb'))

model = pickle.load(open('model.pkl' , 'rb'))
app = Flask(__name__)

#@app.route('/welcome')
#def welcome():
    #return render_template('home.html')
    
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/home')
@app.route('/welcome')
def welcome():
    return render_template('index.html')
@app.route('/risk_value', methods=['GET','POST'])
def risk_value():
        Age=int(request.form['age'])
        Gender=request.form['gender']
        #Waist=int(request.form['waist'])
        jaundice=request.form['db']
        itchy=request.form['healthdiet']
        nausea=request.form['nausea']
        pain=request.form['nausea1']
        swell=request.form['nausea2']
        sense=request.form['nausea3']
        risk_score=0

        if Age:
            if Age<35:
                risk_score+=0
            elif Age>=35 and Age <=49:
                risk_score+=20
            else:
                risk_score+=30

       
        if jaundice:
            if jaundice=='1':
                risk_score+=0
            elif jaundice=='2':
                risk_score+=20
            
        if itchy:
            if itchy=='1':
                risk_score+=0
            elif itchy=='2':
                risk_score+=20
        if nausea:
            if nausea=='1':
                risk_score+=0
            elif nausea=='2':
                risk_score+=10
        if pain:
            if pain=='1':
                risk_score+=0
            elif pain=='2':
                risk_score+=10
        if swell:
            if swell=='1':
                risk_score+=0
            elif swell=='2':
                risk_score+=10
        if sense:
            if sense=='1':
                risk_score+=0
            elif sense=='2':
                risk_score+=10
        if risk_score<40:
            risk='LOW'
        elif risk_score>=40 and risk_score<=70:
            risk='MODERATE'
        else:
            risk='HIGH' 
        return render_template('home.html',risk=risk,risk_score=risk_score)


    

@app.route('/predict' , methods=['POST'])

def predict():
    inputs = [float(x) for x in request.form.values()]
    inputs = np.array([inputs])
    inputs = sc.transform(inputs)
    output = model.predict(inputs)
    if output <0.5:
        output = 0
    else:
        output = 1
    return render_template('result.html' , prediction = output)

if __name__ =='__main__':
    app.run(debug=True)
