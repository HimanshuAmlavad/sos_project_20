from service.dao.BaseDAO import BaseDAO
from service.models import Branch
from service.utility.DataValidator import DataValidator


class BranchDAO(BaseDAO):
    def get_model(self):
        return Branch

    def get_Unique(self):
        return ["branch_name"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("branch_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(branch_id=int(value))
        
        return query
