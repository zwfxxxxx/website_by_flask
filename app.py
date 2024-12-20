from flask_app import app
from api.api import api_bp

app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)