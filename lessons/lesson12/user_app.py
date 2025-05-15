from flask import Flask, render_template, redirect, url_for, request

from models import User, generate_users



APP = Flask(__name__)
USERS = generate_users(10)

@APP.route('/')
def hello_world():
    return render_template('user_table.html', data=USERS)

@APP.route('/user/<int:pk>')
def user_detail(pk):
    user = None
    print(f"pk: {pk}")
    for u in USERS:
        if u.pk == pk:
            user = u
    return render_template('user_detail.html', user=user)

@APP.route('/user', methods=['GET', 'POST'])
def user_create():
    if request.method == 'POST':
        username = request.form['username1']
        email = request.form['email1']
        password = request.form['password1']
        new_user = User(len(USERS) + 1, username, email, password)
        USERS.append(new_user)
        return redirect(url_for('hello_world'))
    return render_template('user_create.html')


@APP.route('/api/user', methods=['GET', 'POST'])
def api_user():
    if request.method == 'POST':
        print(f"request.json: {request.json}")
        new_user = User(**request.json)
        USERS.append(new_user)
    return [user.to_dict() for user in USERS]

if __name__ == '__main__':
    
    APP.run(host='0.0.0.0', port=5000, debug=True)