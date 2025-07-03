from flask import Flask
from routes.api import api
from models.Producto import db, Producto


app = Flask(__name__)
app.register_blueprint(api)

@app.route('/')
def ok():
    return 'Bienvenido a Flask', 200

if __name__ == '__main__':
    if db.is_closed():
        db.connect()
    db.create_tables([Producto])
    app.run(port=5000, debug=True)