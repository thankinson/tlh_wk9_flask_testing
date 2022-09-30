from flask import Flask, render_template, redirect, url_for, request
from application import app

@app.route('/', methods=['GET',"POST"])
def index():
    if request.method == "POST":
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        add = float(num1) + float(num2)
        return render_template('addresults.html', num1=num1, num2=num2, add=add)
    
    return render_template('index.html')
