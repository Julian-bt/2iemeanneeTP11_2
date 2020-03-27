class Circle:
    def __init__(self,rayon):
        self.__rayon=rayon
    def __add__(self, other):
        return Circle(self.__rayon+other.__rayon) #ici on return un objet
    def __lt__(self, other):
        return self.__rayon<other.__rayon
    def __gt__(self, C):
        return self.__rayon > C.__rayon
    def __str__(self):
        return self.__rayon



if __name__== '__main__':
    c1 = Circle(2)
    c2 = Circle(3)
    c3 = c1 + c2 #on veut creer un nouvel objet donc on doit return un objet

    c4 = c1 < c2
    c5 = c2 > c3
    print(c5)
    print(isinstance(c1,Circle))
    print(isinstance(c2,Circle))

