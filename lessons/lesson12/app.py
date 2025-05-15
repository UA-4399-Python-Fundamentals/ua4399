from flask import Flask, url_for


my_app = Flask(__name__)



@my_app.route('/')
def hello_world():
    return 'Hello, World!'

@my_app.route('/user')
@my_app.route('/user/<name>')
def hello_user(name=None):
    return f'Hello, user {name if name else ""}!'

if __name__ == '__main__':
    with my_app.test_request_context():
        print(my_app.url_map)
        print(my_app.url_for('hello_world'))
        print(my_app.url_for('hello_user', name='John'))
        print(url_for('hello_user', name='Jane'))
        print(url_for('hello_user', name='Doe'))
    # my_app.run(debug=True)
    my_app.run(host='0.0.0.0', port=3000, debug=True)
    