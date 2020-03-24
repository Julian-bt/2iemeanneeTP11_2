class complexe:
    def __init__(self,Re, Im):
        self.__Re = Re
        self.__Im = Im

    def getRe(self):
        return self.__Re

    def getIm(self):
        return self.__Im

    def __add__(self, Comp):
       return complexe(self.__Re + Comp.__Re, self.__Im + Comp.__Im)

    def __sub__(self, Comp):
       return complexe(self.__Re - Comp.__Re, self.__Im - Comp.__Im)

    def __mul__(self, Comp):
       return complexe(self.__Re * Comp.__Re - self.__Im * Comp.__Im, self.__Re * Comp.__Im +self.__Im * Comp.__Re )

    def __truediv__(self, Comp):
       return complexe(self.__Re / Comp.__Re, self.__Im / Comp.__Im)

    def __abs__(self):
       return ((self.__Re**2 + self.__Im**2)**0.5)

    def __eq__(self, Comp):
       return (self.__Re == Comp.__Re and self.__Im == Comp.__Im)

    def __ne__(self, Comp):
       return (self.__Re != Comp.__Re or self.__Im != Comp.__Im)

if __name__ == '__main__':
    C1 = complexe(1,1)
    C2 = complexe(2,2)
    C3 = C1*C2
    print(str(C3.getRe())+"+"+str(C3.getIm())+"i")
    C4 = abs(C1)
    print(C4)
    C5 = abs(C2)
    #print("la valeur absolue de "+str(C5.getRe())+"+"+str(C5.getIm())+"i est de :"+C5)
