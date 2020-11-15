from flask import Flask,render_template,request
import pymysql


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route("/bmi", methods=['POST'])
def bmi_cal():
    txt = ""
    KG = request.form['kg']
    HEIGHT = request.form['high']
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

    return render_template('show.html', bmi=bmi, txt=txt)


if __name__ == "__main__":
    app.run(debug=True)