from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from views.main import main
from views.api import api
from datetime import datetime
from path import path
import os

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(main)

ROOT_PATH = path(__file__).dirname()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{0}'.format(os.path.abspath(os.path.join(ROOT_PATH, "chillout.db")))
db = SQLAlchemy(app)

class Event(db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer, primary_key=True)
    peltier = db.Column(db.Float())
    pentiometer = db.Column(db.Float())
    temp = db.Column(db.Float())

    created = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    updated = db.Column(db.DateTime(timezone=True), onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Event %r>' % self.id

db.create_all()
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)
