class Duree:
    def __init__(self,heure,minute,seconde):
        self.__heure=heure
        self.__minute=minute
        self.__seconde=seconde
    def __str__(self):
        return (str(self.__heure)+'h'+str(self.__minute)+'m'+str(self.__seconde)+'s')

    def __add__(self, other):
        additionseconde=self.__seconde+other.__seconde

        if additionseconde <=60:
            SECONDE=additionseconde

            additionminute=self.__minute+other.__minute

            if additionminute<=60:
                MINUTE=additionminute
                additionheure=self.__heure+other.__heure
                if additionheure<=24:
                    HEURE=self.__heure+other.__heure+1
                    return Duree(HEURE,MINUTE,SECONDE)
                else:
                    HEURE=self.__heure+other.__heure+1-24
                    return Duree(HEURE,MINUTE,SECONDE)

            else:
                MINUTE=additionminute-60
                #rajouter 1h
                additionheure=self.__heure+other.__heure +1

                if additionheure<=24:
                    HEURE=self.__heure+other.__heure+1
                    return Duree(HEURE,MINUTE,SECONDE)
                else:
                    HEURE=self.__heure+other.__heure+1-24
                    return Duree(HEURE,MINUTE,SECONDE)
        else:
            SECONDE=additionseconde-60
            #rajouter +1 minute
            additionminute=self.__minute+other.__minute+1

            if additionminute<=60:
                MINUTE=additionminute
                additionheure=self.__heure+other.__heure

                if additionheure<=24:
                    HEURE=self.__heure+other.__heure+1
                    return Duree(HEURE,MINUTE,SECONDE)
                else:
                    HEURE=self.__heure+other.__heure+1-24
                    return Duree(HEURE,MINUTE,SECONDE)


            else:
                MINUTE=additionminute-60
                additionheure=self.__heure+other.__heure +1

                if additionheure<=24:
                    HEURE=self.__heure+other.__heure+1
                    return Duree(HEURE,MINUTE,SECONDE)
                else:
                    HEURE=self.__heure+other.__heure+1-24
                    return Duree(HEURE,MINUTE,SECONDE)


if __name__== '__main__':
    h1=Duree(8,54,6) #8h54min6s
    h2=Duree(2,10,5) #2h10min5s
    addition=h1+h2
    print(addition)
