class Complex:
    def __init__(self,re,im):
        self.__re=re
        self.__im=im
    def __add__(self, other):
        return Complex(self.__re + other.__re,self.__im + other.__im)
    def __sub__(self, other):
        return Complex(self.__re - other.__re,self.__im - other.__im)
    def __mul__(self, other):
        a=self.__re * other.__re
        b=self.__im*other.__re
        c=-self.__im*other.__im
        d=self.__re*other.__im
        return Complex(a+c,b+d)
    def __truediv__(self, other):
        if other.__re !=0 and other.__im!=0:
            return Complex(self.__re / other.__re,self.__im / other.__im)
    def __abs__(self):
        return ((self.__re**2 + self.__im**2)**0.5)
    def __eq__(self, other):
        return self.__re== other.__im and self.__im == other.__im
    def __ne__(self, Comp):
       return (self.__re != Comp.__re or self.__im != Comp.__im)
    def getre(self):
        return self.__re
    def getim(self):
        return self.__im



if __name__== '__main__':
    c1=Complex(2,6)
    c2=Complex(1,2)
    C3=(c1+c2)
    print(str(C3.getre())+"+"+str(C3.getim())+"i")

    C4=(c1-c2)
    print(str(C4.getre())+"+"+str(C4.getim())+"i")

    C5=(c1*c2)
    print(str(C5.getre())+"+"+str(C5.getim())+"i")

    C6=abs(c1)
    print(C6)

    C7=(c1==c2)
    print(C7)

    C8= c1!=c2
    print(C8)
    print(isinstance(c1,Complex))
    print(isinstance(c2,Complex))
