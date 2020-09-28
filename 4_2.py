from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    bmi=''
    weight=''
    height=''
    if request.method=='POST' and 'weight' in request.form and 'height' in request.form:
        weight=float(request.form.get('weight'))
        height=(float(request.form.get('height')))/100
        bmi=calc_bmi(weight, height) 
    return render_template('bmicalc.html',bmi=bmi)
def calc_bmi(weight, height):
    return round((weight/(height**2)),2)
app.run()