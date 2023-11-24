from flask import Blueprint, request, render_template
from .mixins import ConnectionMixin
from .models import WeatherForecast
from . import db
import datetime

home_blueprint = Blueprint('home', __name__)


@home_blueprint.route('/', methods=['GET', 'POST'])
def get_weather():
    data = {}
    if request.method == 'POST':
        location = request.form.get('city')
        city_to_check = WeatherForecast.query.filter_by(city=location, date_time=datetime.datetime.now()).first()
        if city_to_check:
            data = city_to_check.data
        else:
            data = ConnectionMixin().load_data_from_api_to_dict(location)
            weather_forecast = WeatherForecast(city=location, data=data)
            db.session.add(weather_forecast)
            db.session.commit()
    return render_template('home.html', data=data)


