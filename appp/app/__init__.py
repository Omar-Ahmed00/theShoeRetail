


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes import main 
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='../templates')  # Specify the template folder

    # Load configuration from the Config class
    app.config.from_object('app.config.Config')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
    # Initialize the SQLAlchemy instance with the app
    db.init_app(app)

    # Create a new app context
    with app.app_context():
        # Import models to avoid circular imports
        from app.models import Product  
        
        # Create the database tables if they don't exist
        db.create_all()

    # Import and register the routes
    from app.routes import main  

    app.register_blueprint(main)

    return app
