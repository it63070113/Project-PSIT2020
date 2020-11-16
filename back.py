from flask import Flask,render_template,request
import pymysql


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route("/bmi", methods=['POST'])
def bmi_cal():
    txt = ""
    bmi = "กรุณากรอกข้อมูลให้ถูกต้อง"
    KG = request.form['kg_bmi']
    HEIGHT = request.form['high']
    if KG.isdigit() and HEIGHT.isdigit():
        bmi = round(float(KG) / ((float(HEIGHT)/100) ** 2), 2)
        if bmi < 18.5:
            txt = "น้ำหนักน้อย/ผอม"
        elif 18.50 <= bmi <= 22.90:
            txt = "ปกติ"
        elif 23 <= bmi <= 25.90:
            txt = "ท้วม/โรคอ้วนระดับ 1"
        elif 23 <= bmi <= 29.90:
            txt = "ท้วม/โรคอ้วนระดับ 2"
        else:
            txt = "ท้วม/โรคอ้วนระดับ 3"
        return render_template('index.html', bmi=bmi, txt=txt)
    else:
        return render_template('index.html', bmi=bmi)



@app.route("/bmr", methods=['POST'])
def bmr():
    bmr = "กรุณากรอกข้อมูลให้ถูกต้อง"
    sex_bmr = request.form["sex_bmr"]
    kg_bmr = request.form['kg_bmr']
    height_bmr = request.form['high_bmr']
    age_bmr = request.form['age_bmr']
    if kg_bmr.isdigit() and height_bmr.isdigit():
        if sex_bmr == "male":
            bmr = int(66 + (13.7*float(kg_bmr)) + (5*float(height_bmr)) - (6.8 * float(age_bmr)))
            return render_template('index.html', bmr=bmr)
        elif sex_bmr == "female":
            bmr = int(665 + (9.6 * float(kg_bmr)) + (1.8 * float(height_bmr)) - (4.7 * float(age_bmr)))
            return render_template('index.html', bmr=bmr)
    else:
        return render_template('index.html', bmr=bmr)



if __name__ == "__main__":
    app.run(debug=True)