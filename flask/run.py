from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)

@app.route('/users', methods=['POST'])
def create_user():
    name = request.form['name']
    email = request.form['email']

    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully.'})

@app.route('/show_users', methods=['GET'])
def show_all_users():
    users = User.query.all()
    return render_template('show_all_users.html', users=users)

@app.route('/', methods=['GET'])
def show_user_form():
    return render_template('user_creation.html')

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)




