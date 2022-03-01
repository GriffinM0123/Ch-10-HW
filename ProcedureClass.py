

class Procedure:
    def __init__(self, nop, dop, prac, charge, pinfo):
        self.__nop = nop
        self.__dop = dop
        self.__prac = prac
        self.__charge = charge
        self.__pinfo = pinfo
    
    def get_nop(self):
        return self.__nop
    
    def get_dop(self):
        return self.__dop

    def get_prac(self):
        return self.__prac

    def get_charge(self):
        return self.__charge

    def get_pinfo(self):
        return self.__pinfo
    



