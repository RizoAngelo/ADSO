class humano:
    def __init__(self,index,OrganizationId,Name,Website,Country,Description,Founded,Industry,Numberofemployees):
        self.__idex=index
        self.__OrganizationId=OrganizationId
        self.__name=Name
        self.__Website=Website
        self.__Country=Country
        self.__Description=Description
        self.__founded=Founded
        self.__Industry=Industry
        self.__Numberofemployees=Numberofemployees
    def informaciondecompañia(self):
        return self.__idex +' '+self.__OrganizationId+' '+self.__name+' '+self.__Website+' '+self.__Country+' '+self.__Description+' '+self.__founded+' '+self.__Industry+' '+self.__Numberofemployees
        
        
        