from flask import Flask,render_template,request
from app.utils import predictions
import CONFIG
app=Flask(__name__)

@app.route('/')
def start():
    return render_template("car.html")

@app.route('/predict',methods= ["POST","GET"])
def predict_price():
    data= request.form
    pred_obj= predictions()
    predicted_millage=pred_obj.predicted_millage(data)
    print(predicted_millage)

    return (predicted_millage)

if __name__=="__main__":
    app.run(host=CONFIG.HOST_NAME, port= CONFIG.PORT_NUMBER)
    