from flask import Flask, request, jsonify, render_template
from joblib import dump, load

app = Flask(__name__)

model = load(r'D:\jupyter\iNetworks\Ahmed_Yahia_Mahmoud_IndustryClassificationTask\01_Code\model.joblib')

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == 'POST':
	    message = request.form['message']
	    data = [message]
	    vect = data
	    my_prediction = model.predict(vect)
    return render_template('result.html',prediction = my_prediction)
    
    

if __name__ == "__main__":
    app.run(debug=True)
    
    
