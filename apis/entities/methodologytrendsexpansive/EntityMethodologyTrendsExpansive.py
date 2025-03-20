from decouple import config

from decimal import Decimal

class EntityMethodologyTrendsExpansive():

    def get_id(self):

        return self.config['id']  