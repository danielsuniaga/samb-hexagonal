import apis.entities.reports.EntityReports as EntityReports

class ServicesReports():

    entity = None

    def __init__(self):

        self.entity = EntityReports.EntityReports()

    def init_data_add_persistence(self,type_reports):

        return True

    def add_persistence(self,type_reports):

        data_peristence = self.init_data_add_persistence(type_reports)

        return True 