import apis.repositories.framework.RepositoryFramework as RepositoryFramework
import apis.entities.framework.EntityFramework as EntityFramework

class ServicesFramework:

    def __init__(self):
        self.repository = RepositoryFramework.RepositoryFramework()
        self.entity = EntityFramework.EntityFramework()
        self.ServicesDates = None

    def init_services_dates(self, value):
        self.ServicesDates = value
        return True

    def get_current_date_hour(self):
        return self.ServicesDates.get_current_date_hour()

    def generate_id(self):
        return self.entity.generate_id()

    def get_config_add_description(self):
        return self.entity.get_config_add_description()

    async def get_config_add_condition(self):
        return await self.entity.get_config_add_condition()

    async def init_data_add(self):

        return {
            'id_framework': self.generate_id(),
            'description': self.get_config_add_description(),
            'fecha': self.get_current_date_hour(),
            'condition': await self.get_config_add_condition()
        }

    async def add(self):

        data_persistence = await self.init_data_add()

        result = await self.repository.add(data_persistence)

        return result
