from flask import Flask, request, render_template, redirect, url_for
import requests
import numpy as np
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/predict", methods=['GET', 'POST'])

def predict():
    if request.method == 'POST':
        print(request.form.get('age'))
        try:

            total_training = float(request.form.get("total_training"))
            age = float(request.form.get('age'))
            length_of_service = float(request.form.get("length_of_service"))
            KPI = int(request.form.get("KPI"))
            awards_won = float(request.form.get("awards_won"))
            avg_training_score = float(request.form.get("avg_training_score"))
            previous_year_rating = float(request.form.get("previous_year_rating"))
            department_Analytics = float(request.form.get("department_Analytics"))
            department_Finance = float(request.form.get("department_Finance"))
            department_HR = float(request.form.get("department_HR"))
            department_Legal = float(request.form.get("department_Legal"))
            department_Operations = float(request.form.get("department_Operations"))
            department_Procurement = float(request.form.get("department_Procurement"))
            department_R = float(request.form.get("department_R"))
            department_Sales_Marketing = float(request.form.get("department_Sales_Marketing"))
            department_Technology = float(request.form.get("department_Technology"))
            education_level_Bachelor = float(request.form.get("education_level_Bachelor"))
            education_level_Below_Secondary = float(request.form.get("education_level_Below_Secondary"))
            education_level_Master = float(request.form.get("education_level_Master"))
            gender_f = float(request.form.get("gender_f"))
            gender_m = float(request.form.get("gender_m"))
            arguments = [total_training, age, length_of_service, KPI, awards_won, avg_training_score, previous_year_rating, department_R,
                        department_Analytics, department_Sales_Marketing, department_Finance, department_HR, department_Legal, department_Operations, department_Procurement,
                        department_Technology, education_level_Bachelor, education_level_Below_Secondary, education_level_Master, gender_f, gender_m]
            pred_arg = np.array(arguments)
            pred_arg = pred_arg.reshape(1, 21)
            load_model = open("decision_model.pkl", "rb")
            model = joblib.load(load_model)
            prediction = model.predict(pred_arg)

            pre = lambda predi: 'Successful' if (predi == 1) else "Rejected"

              # $FlaskEmployee
              # hM6QpjtRCNTogcelEJswbQDszlgLunx4dkceCbT97wMZYPyroRnFckvSAwcT

        except ValueError:
            return "Please Checked the Value Entered and Try again Cheers"
      
    return render_template("predict.html", final_prediction = pre(prediction) )



if __name__ == "__main__":
    app.run(debug=True)

   