class humano:
    def __init__(self,OrganizationId,Name):
        self.__OrganizationId=OrganizationId
        self.__name=Name
    
    def informaciondecompañia(self):
        return self.__OrganizationId+' '+self.__name
        
        
    