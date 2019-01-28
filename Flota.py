import linecache
from random import randint as rand
from Statek import *
class Flotaa:
    def __init__(self):
        self.flota_1=[] ; self.dodadkowa_1=[] ; self.zniszczone_1=[]
        self.flota_2=[] ; self.dodadkowa_2=[] ; self.zniszczone_2=[]
        for i in range(2,15):
            wiersz = linecache.getline('flota_1.txt', i)
            if int(wiersz.split()[1])!=0:                                                         
                for a in range(int(wiersz.split()[1])): 
                    self.flota_1.append(Statek(wiersz.split()[0]))
        for i in range(2,15):
            wiersz = linecache.getline('flota_2.txt', i)
            if int(wiersz.split()[1])!=0: 
                for a in range(int(wiersz.split()[1])): 
                    self.flota_2.append(Statek(wiersz.split()[0]))
        print('Gracz_1 ma statkow: ',len(self.flota_1),'Gracz_2 ma statkow: ',len(self.flota_2))  
        
    def rozgrywka(self):
        for i in range(0,len(self.flota_1)):
            losowa = rand(0,len(self.flota_2)-1)
            wynik=self.flota_1[i].attack(self.flota_2[losowa])
            if wynik==True and self.zniszczone_2.count(losowa)==0:
                self.zniszczone_2.append(losowa)
            elif wynik==False and self.dodadkowa_1.count(losowa)==0:
                self.dodadkowa_1.append(i)
        
        while len(self.dodadkowa_1)>0:
            losowa = rand(0,len(self.flota_2)-1)
            wynik=self.flota_1[self.dodadkowa_1[0]].attack(self.flota_2[losowa])
            aktualna=self.dodadkowa_1[0]
            self.dodadkowa_1.pop(0)
            if wynik==True and self.zniszczone_2.count(losowa)==0:
                self.zniszczone_2.append(losowa)
            elif wynik==False and self.dodadkowa_1.count(losowa)==0:
                self.dodadkowa_1.append(aktualna)
        #// drugi team
        
        for i in range(0,len(self.flota_2)):
            losowa = rand(0,len(self.flota_1)-1)
            wynik=self.flota_2[i].attack(self.flota_1[losowa])
            if wynik==True and self.zniszczone_1.count(losowa)==0:
                self.zniszczone_1.append(losowa)
            elif wynik==False and self.dodadkowa_2.count(losowa)==0:
                self.dodadkowa_2.append(i)
        
        while len(self.dodadkowa_2)>0:
            losowa = rand(0,len(self.flota_1)-1)
            wynik=self.flota_2[self.dodadkowa_2[0]].attack(self.flota_1[losowa])
            aktualna=self.dodadkowa_2[0]
            self.dodadkowa_2.pop(0)
            if wynik==True and self.zniszczone_1.count(losowa)==0:
                self.zniszczone_1.append(losowa)
            elif wynik==False and self.dodadkowa_2.count(losowa)==0:
                self.dodadkowa_2.append(aktualna)
        
        return self.usuwanie()
        
    def usuwanie(self):
        self.zniszczone_1.sort() ; self.zniszczone_2.sort()
        while len(self.zniszczone_1) !=0:
            self.flota_1.pop(self.zniszczone_1[-1])
            self.zniszczone_1.pop(-1)
            
        while len(self.zniszczone_2) !=0:
            self.flota_2.pop(self.zniszczone_2[-1])
            self.zniszczone_2.pop(-1)
            
        return self.winner()
    
    def odnowa_oslony(self):
        for i in range(len(self.flota_1)):
            self.flota_1[i].odnowa()
        for i in range(len(self.flota_2)):
            self.flota_2[i].odnowa()
            
    def winner(self):
        if len(self.flota_1)==0: return 2
        elif len(self.flota_2)==0: return 1
        else: 
            self.odnowa_oslony()
            return 3
    def wyswietl(self):
        print('Gracz_1 ma statkow: ',len(self.flota_1),'Gracz_2 ma statkow: ',len(self.flota_2))
                
f=Flotaa()
runda=1
for i in range(1,7):
    print('Runda: ',i)
    f.rozgrywka()
    if f.winner()==1:
        print('Gracz 1 wygrywa w rundzie: ',i)
        break
    elif f.winner()==2:
        print('Gracz 2 wygrywa w rundzie: ',i)
        break
    elif (f.winner()==3 and i==6):
        print('Jest remis !!')
        break
f.wyswietl()