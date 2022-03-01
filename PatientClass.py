

class Patient:

    def __init__(self, ID, name, add, phone, vs):
        self.__ID = ID
        self.__name = name
        self.__add = add
        self.__phone = phone
        self.__vs = vs

    def get_ID(self):
        return self.__ID

    def get_name(self):
        return self.__name

    def get_add(self):
        return self.__add

    def get_phone(self):
        return self.__phone

    def get_vs(self):
        return self.__vs
        
    



