from app import app
from flask_cors import CORS



if __name__ == "__main__":
    CORS(app)
    app.run(host="0.0.0.0",debug=True)