from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    
    
    with app.app_context():
        from api_biblioteca.routes import bp
        from api_biblioteca.models import Cliente, Prestamo
        app.register_blueprint(bp)
        # Descomentar para resetear la bbdd
        # db.drop_all()
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
