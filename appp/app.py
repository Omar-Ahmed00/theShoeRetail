# from app import create_app
# from app import db
# from flask import Flask


# app = Flask(__name__)

# # Set the secret key for session management
# app.secret_key = 'A1b2c3d4e10&'  # Replace with a strong, unique key

# # Initialize your database and other components
# db.init_app(app)


# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)  # Start the Flask application



from app import create_app, db

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask application
