import numpy

class Matrice:
    def __init__(self,data):
        self.__data=data #liste

    def getdata(self):
        return self.__data
    def __str__(self):
        return self.__data

    def __add__(self, other):
        a11=self.__data[0][0]+other.__data[0][0]
        a12=self.__data[0][1]+other.__data[0][1]
        a21=self.__data[1][0]+other.__data[1][0]
        a22=self.__data[1][1]+other.__data[1][1]
        return Matrice(numpy.array([[a11,a12],[a21,a22]]))

    def __iadd__(self, other):
        a11=self.__data[0][0]+other.__data[0][0]
        a12=self.__data[0][1]+other.__data[0][1]
        a21=self.__data[1][0]+other.__data[1][0]
        a22=self.__data[1][1]+other.__data[1][1]
        self.__data=numpy.array([[a11,a12],[a21,a22]])
        return (self.__data)

    def __sub__(self, other):
        a11=self.__data[0][0]-other.__data[0][0]
        a12=self.__data[0][1]-other.__data[0][1]
        a21=self.__data[1][0]-other.__data[1][0]
        a22=self.__data[1][1]-other.__data[1][1]
        return Matrice(numpy.array([[a11,a12],[a21,a22]]))

    def __isub__(self, other):
        a11=self.__data[0][0]+other.__data[0][0]
        a12=self.__data[0][1]+other.__data[0][1]
        a21=self.__data[1][0]+other.__data[1][0]
        a22=self.__data[1][1]+other.__data[1][1]
        self.__data=numpy.array([[a11,a12],[a21,a22]])
        return (self.__data)

    def __mul__(self, other):
        a11=self.__data[0][0]*other.__data[0][0] +self.__data[0][1]*other.__data[1][0]
        a12=self.__data[0][0]*other.__data[0][1] +self.__data[0][1]*other.__data[1][1]
        a21=self.__data[1][0]*other.__data[0][0] +self.__data[1][1]*other.__data[1][0]
        a22=self.__data[1][0]*other.__data[0][1] +self.__data[1][1]*other.__data[1][1]
        return Matrice(numpy.array([[a11,a12],[a21,a22]]))




if __name__=='__main__':
    matrice1=Matrice(numpy.array([[1,1],[1,1]]))
    matrice2=Matrice(numpy.array([[2,2],[2,2]]))
    addition=matrice1+matrice2
    print(addition.getdata())
    matrice1+=matrice2
    print(matrice1)
    matrice3=Matrice(numpy.array([[0,1],[1,1]]))
    multiplication=matrice3*matrice2
    print(multiplication.getdata())


