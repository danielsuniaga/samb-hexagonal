import apis.repositories.framework.RepositoryFramework as RepositoryFramework

class ServicesFramework: 

    repository = None

    def __init__(self):

        self.repository = RepositoryFramework.RepositoryFramework()

    def add_repository(self):        
        
        return self.repository.add()
    
    def init_data_add(self):

        return {
            'id_framework': 'Test',
            'description': 'Test',
            'fecha': 'Test',
            'condition': 'Test'
        }

    def add(self):

        data_persistence = self.init_data_add()

        return self.add_repository(data_persistence)