from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('ml.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("covid.html")



@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('covid.html', pred='Your are in Danger.\nProbability of you having Covid is {}'.format(output), bhai="kuch karna hain iska ab?")
    else:
        return render_template('covid.html', pred='You are safe.\n Probability of you having Covid is {}'.format(output), bhai="Your Forest is Safe for now")

@app.route('/covid', methods=['POST', 'GET'])
def covid():
    if request.method == 'POST':
        if request.form['opt'] == 'index1':
            return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)