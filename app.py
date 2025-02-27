from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from ApiResponse import ApiResponse

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:950423@localhost:3306/web01'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'  # 指定資料表名稱
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [ApiResponse.format_user(user) for user in users]
    return ApiResponse.success(users_list)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    existing_user = User.query.filter_by(account=data['account']).first()
    if existing_user:
        return ApiResponse.fail("Account already exists", 409)
    
    new_user = User(account=data['account'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return ApiResponse.success("User added successfully!")

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return ApiResponse.success(ApiResponse.format_user(user))
    else:
        return ApiResponse.fail("User not found")

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if user:
        user.account = data['account']
        user.password = data['password']
        db.session.commit()
        return ApiResponse.success("User updated successfully!")
    else:
        return ApiResponse.fail("User not found")

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return ApiResponse.success("User deleted successfully!")
    else:
        return ApiResponse.fail("User not found")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)