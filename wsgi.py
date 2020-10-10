import os

from app.app import create_app

app = create_app(os.getenv("FLASK_ENV") or "test")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)