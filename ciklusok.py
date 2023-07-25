
def nyoc_het():
    #kiírja 10 és 20 között az egész számokat.
    for i in range(10,21):
       print(i)

def nyoc_nyoc():
    #kiírja 10 és 30 között a páros számokat 
    for i in range(10,31,2):
        print(i)

def nyoc_kil():
    #bekér két számot és kiírja kettő közötti páros számokat!
    szam1=int(input("Kérek egy számot: "))
    szam2=int(input("Kérek mégegy számot: "))
    for i in range(szam1,szam2,2):
        print(i)

def kilencven():
    # Nem negatív egész számról határozza meg a program, hogy hány jegyű!
    #ROSSZ!!!!!!

    szam=int(input("Kérek egy nem negatív egész számot: "))

    szam=0
    while szam < 9:
        print("egy jegyű")
    if 9 < szam and szam < 99:
        print("kétszámjegyű")
    elif 99<szam and szam<999:
        print("3 számjegyű")


def f90():
    szam=int(input("Kérek egy nem negatív egész számot: "))
    eredeti_szam=szam
    jegyek_szama=1
    while szam >10:
        szam=szam//10   #tizedére csükkentjük 
      
        jegyek_szama+=1 #helyiértékeket növeljük 1-gyel
    print(f"{eredeti_szam} jegyeinek a száma:{jegyek_szama}")
    


def f91():
    # Készítsünk programot, amely 15 darab ’*’-ot ír ki a képernyőre egy sorba! 
    for i in range(0,15):
        print("*",end=" ")

def f92():
    #Írassa ki a számokat 1-től 20-ig és mellé a négyzetüket is!
    for i in range(1,21):
        print(i,i*i)

def f93():
    #Egy bekért számot kiír nullától növekvő, mellette lévő oszlopban nulláig csökkenő sorrendben.
    #ROSSZ!!!!!

    szam=int(input("Kérek egy számot:"))
    for i in range(0,szam+1):
        print(i,szam-i)



def f94():
    havi_atlagok_lista=[]
    for i in range(0,12):

       ho=int(input("Kérem a havi homersekletet: "))
       havi_atlagok_lista.append(ho)



    


    veg=sum(havi_atlagok_lista)/12
    print(veg)


def f94_B():
    eves_atlag=0
    for i in range(0,12):

       ho=int(input("Kérem a havi homersekletet: "))
       eves_atlag+=ho



    


    veg=eves_atlag/12
    print(veg)
    

def f95():
    #bekér egy számot és kiírja az összes osztóját!
    #ROSSZ!!!!

    szam=int(input("Kérek egy egész számot: "))
    
    for i in range(2,szam):
        if szam%i==0:
            print(f"szám osztója:{i}")
        else:
            print(f"nem {i}")

def f96():

    szo='asztal'
    for i in range(len(szo)-1,-1,-1):
        print(szo[i])
        


    

       

    





   
        

def main():
    #nyoc_het()
    #nyoc_nyoc()
    #nyoc_kil()
    #kilencven()
    #f91()
    #f92()
    #f93()
    #f94()
    #f94_B()
    #bekeres()
    #tarol()
    #szamol()
    #f95()
    #f90()
    f96()
    



main()




