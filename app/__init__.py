
from flask import Flask



def create_app():
    app = Flask(__name__)

    @app.after_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        return response

    app.config.from_object('config.Config')

    from app.routes.mobileWalletRoutes import main as main_blueprint
    from app.routes.paypalRoutes import paypal_bp as paypal_blueprint

    app.register_blueprint(paypal_blueprint, url_prefix='/paypal')
    app.register_blueprint(main_blueprint)
    # app.register_blueprint(paypal_blueprint)
    
    return app
