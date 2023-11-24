from . import db
import datetime


class WeatherForecast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, default=datetime.datetime.now())
    city = db.Column(db.String(50), nullable=False)
    data = db.Column(db.JSON)
