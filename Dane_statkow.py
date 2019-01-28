"""- Klasa ‘DaneStatków’ zawierająca statyczne tablice przechowujące parametry wszystkich typów
statków. Powinna te parametry wczytać z plików.
"""
import linecache
class DaneStatkow:
    def __init__(self):
        file = open('szybkie_dziala.txt','r')
        self.szybkie_dziala= {}
        self.a= file.readline().split()[1:]
        for self.line in file.readlines():
            self.line = self.line.split()
            self.line = [self.line[0]]+[int(x) for x in self.line[1:]]
            self.szybkie_dziala[self.line[0]] = dict(zip(self.a,self.line[1:]))
        #print(self.szybkie_dziala)
        
        self.slownik={}
        for i in range(2,15):
            wiersz = linecache.getline('dane_statkow.txt', i)
            self.slownik[wiersz.split()[0]]=wiersz.split()[0],wiersz.split()[1],int(wiersz.split()[2]),int(wiersz.split()[3]),int(wiersz.split()[4])
        file.close()
        print(self.slownik)
        
#DS=DaneStatkow().szybkie_dziala['mt']['mt']
#print(DS)