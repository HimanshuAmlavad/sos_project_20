from service.dao.BaseDAO import BaseDAO
from service.models import WeatherAlert
from service.utility.DataValidator import DataValidator


class WeatherAlertDAO(BaseDAO):
    def get_Unique(self):
        return ["alert_id"]

    def get_model(self):
        return WeatherAlert

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("alert_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(alert_id=int(value))
        
        return query