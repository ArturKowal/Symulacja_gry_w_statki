from DaneStatkow import *
from random import randint as rand
import numpy as np
class Statek:
    """
    return True - Statek wroga zoastał zniszczony
    return False - Statek atakującego zyskuje ponowne trafienie
    return 3 - Statek nie otrzymuje obrażeń lub nie został zniszczony
    """
    def __init__(self,statek):
        self.skrot=statek
        self.dane=DaneStatkow().slownik
        self.statek=str((self.dane[statek])[1])
        self.ps=(self.dane[statek])[2]
        self.niezmienna_ps=(self.dane[statek])[2]
        self.oslona=(self.dane[statek])[3]
        self.niezmienna_oslona=(self.dane[statek])[3]
        self.atak=(self.dane[statek])[4]
    def dawaj(self):
        return (self.statek,' ps: ',self.ps,' oslona: ',self.oslona,' atak: ',self.atak)
    def attack(self, atakowany): 
        if self.atak<(1/100)*atakowany.oslona:
            #print('Atak nie udany bo punkty ataku atakujacego sa mniejsze niż 1/100 punktów osłony atakowanego')
            return 3
        else:
            return self.trafiony(atakowany)
            
    def trafiony(self, atakowany):
        atakowany.ps=atakowany.ps-(self.atak-atakowany.oslona)
        atakowany.oslona=0
        #print('Statek: ',self.statek,' atakuje ',atakowany.statek,'Punkty strukturalne obroncy: ',atakowany.ps)
        if atakowany.ps>0:
            if atakowany.niezmienna_ps>atakowany.ps*(70/100):
                szanse=1-(atakowany.ps/atakowany.niezmienna_ps)
                #print(atakowany.ps,'/',atakowany.niezmienna_ps)
                losowa=rand(1,10)
                losowa/=10
                #print('no wybuch los ',losowa,' szansa ',szanse)
                if losowa<szanse:
                    #print('Statek: ',atakowany.statek,' ma mniej niz 70% punktow strukturalnych i wybucha')
                    return True
                else:
                    return self.ponowny_strzal(atakowany)
            else:
                return self.ponowny_strzal(atakowany)
        else:
            return True
        
    def odnowa(self):
        self.oslona=self.niezmienna_oslona
        
    def ponowny_strzal(self,atakowany):
        n=DaneStatkow().szybkie_dziala[str(self.skrot)][str(atakowany.skrot)]
        szanse=1-(1/n)
        los=np.random.rand()
        print('Szanse na ponowny strzal',los,'/</',szanse)
        if los<szanse:
            #print('Statek: ',self.statek,' zyskuje kolejne trafienie')
            return False
        return 3