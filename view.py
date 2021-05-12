from app import app
from flask import render_template
from flask import request
from flask import redirect
from models import Users
from app import db
from models import Tours

@app.route('/')
def index():
    return "hi"


@app.route('/archive')
def archive():
    return render_template("archive.html")


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        data = dict()
        data['mail'] = request.form.get('mail')
        data['password'] = request.form.get('password')
        data['name'] = request.form.get('name')
        data['surname'] = request.form.get('surname')
        data['patronymic'] = request.form.get('patronymic')
        data['passport_number'] = request.form.get('passport_number')
        data['international_passport_number'] = request.form.get('international_passport_number')
        data['phone_number'] = request.form.get('phone_number')


        user = Users(
            password=data['password'],
            passport_number=data['passport_number'],
            international_passport_number=data['international_passport_number'],
            phone_number=data['phone_number'],
            mail=data['mail'],
            name=data['name'],
            surname=data['surname'],
            patronymic=data['patronymic']
        )
        db.session.add(user)
        db.session.commit()
        return redirect('/reg')

    return render_template('reg.html')


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        data = dict()
        data['mail'] = request.form.get('mail')
        data['password'] = request.form.get('password')

        print(data)

    return render_template('auth.html')


@app.route('/CreateTours', methods=['GET', 'POST'])
def ct():
    if request.method == 'POST':
        data = dict()
        data['name'] = request.form.get('name')
        data['price'] = request.form.get('price')
        data['description'] = request.form.get('description')
        data['Direction'] = request.form.get('Direction')


        tour = Tours(
            name=data['name'],
            price=data['price'],
            description=data['description'],
            Direction=data['Direction'],
        )
        db.session.add(tour)
        db.session.commit()
        return redirect('/CreateTours')

    return render_template('CreateTours.html')



