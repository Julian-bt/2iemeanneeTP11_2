class Rational:
    def __init__(self,numerateur,denominateur):
        self.__numerator=numerateur
        self.__denominateur=denominateur

    def getNumerator(self):
        return self.__numerator

    def getDenominateur(self):
        return self.__denominateur

    def __pgcd(self,n,d):
        reste=n%d
        while reste!=0:
                n=d
                d=reste
                reste=n%d
        return d

    def __add__(self, other):
        n=(self.__numerator * other.__denominateur) +(other.__numerator * self.__denominateur)
        d= ( self.__denominateur*other.__denominateur)
        pgcd=self.__pgcd(n,d)
        return Rational(n/pgcd , d/pgcd)

    def __sub__(self, other):
        n=(self.__numerator * other.__denominateur) -(other.__numerator * self.__denominateur)
        d= ( self.__denominateur*other.__denominateur)
        pgcd=self.__pgcd(n,d)
        return Rational(n/pgcd , d/pgcd)    

    def __radd__(self, other):
        n=(other.__numerator * self.__denominateur) +(self.__numerator * other.__denominateur)
        d= ( self.__denominateur*other.__denominateur)
        pgcd=self.__pgcd(n,d)
        return Rational(n/pgcd , d/pgcd)

    def __rsub__(self, other):
        n=(other.__numerator * self.__denominateur) -(self.__numerator * other.__denominateur)
        d= ( self.__denominateur*other.__denominateur)
        pgcd=self.__pgcd(n,d)
        return Rational(n/pgcd , d/pgcd)

    def __mul__(self, other):
        n=self.__numerator*other.__numerator
        d=self.__denominateur*other.__denominateur
        pgcd=self.__pgcd(n,d)
        return Rational(n/pgcd , d/pgcd)

if __name__=='__main__':
    f1=Rational(2,8)
    f2=Rational(50,10)
    addition=f1+f2
    print(addition.getNumerator(),'/',addition.getDenominateur())
    soustraction=f1-f2
    print(soustraction.getNumerator(),'/',soustraction.getDenominateur())
    print(isinstance(addition,Rational))
    print(isinstance(soustraction,Rational))

    addition2=f2+f1
    print(addition2.getNumerator(),'/',addition2.getDenominateur())

    multi=f1*f2
    print(multi.getNumerator(),'/',multi.getDenominateur())
