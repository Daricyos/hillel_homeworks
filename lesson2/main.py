# -*- coding:utf-8 -*-
from flask import Flask
from faker import Faker
import pandas as pd
import requests

app = Flask(__name__)
fake = Faker(encoding="utf-8")



@app.route('/requirements/')
def len():
    with app.open_resource('requirements.txt', 'r') as f:
        file_content = f.read()
    return file_content

@app.route('/generate-users/')
@app.route('/generate-users/<int:namber>')
def len2(namber = 100):
    name = []
    email = []
    for _ in range(namber):
        name.append(fake.name())
        email.append(fake.ascii_email())
    d = dict(zip(name, email))
    return d

@app.route('/mean/')
def len3():
    data = pd.read_csv('hw.csv', sep=r',', skipinitialspace = True)
    data['Height(Inches)'] *= 2.54
    data['Weight(Pounds)'] /= 2.205
    a = str(int(data['Height(Inches)'].mean()))
    b = str(int(data['Weight(Pounds)'].mean()))
    return f'Средний рост: {a}см.\n Средний вес: {b}кг.'

@app.route('/space/')
def len4():
    r = requests.get('http://api.open-notify.org/astros.json')
    k = r.json()['number']
    return str(k)




if __name__ == '__main__':
    app.run()