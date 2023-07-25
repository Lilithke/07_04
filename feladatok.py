import math
def elso():
    #Kérjünk be a felhasználótól két egész számot, majd kiszámolja a két szám összegét, különbségét.

    szam1=int(input("Kérem az első egész számot: "))
    szam2=int(input("Kérem az második egész számot: "))

    osszeg=szam1+szam2
    print(osszeg)
    kul=szam1-szam2
    print(kul)

def masodik():
    #Kérjünk be a felhasználótól két egész számot, majd kiszámolja a két szám szorzatát 
    # és hányadosát 2 tizedes pontossággal.

    szam1=int(input("Kérem az első egész számot: "))
    szam2=int(input("Kérem az második egész számot: "))

    szorzat=szam1*szam2
    print(szorzat)
    hanyad=szam1/szam2
    print(round(hanyad,2))

def harmadik():
    #Kérjünk be a felhasználótól egy pozitív egész számot, 
    # majd adjuk meg a kettővel és a hárommal vett osztási maradékát. 
    
    szam1=int(input("Kérek egy pozitív egész számot: "))

    maradek_kettovel=szam1%2
    print(maradek_kettovel)

    maradek_harom=szam1%3
    print(maradek_harom)

def negyedik():
    # Kérjünk be egy valós számot a felhasználótól, 
    # majd írjuk ki a képernyőre két tizedesjegy pontossággal. 

    valos=float(input("Kérek egy valós számot: "))
    print(round(valos,2))

def ot():
    #Kérjünk be a felhasználótól egy páros számot, majd adjuk meg a felét.
    paros=int(input("Kérek egy páros számot: "))
    fele=paros//2
    print(fele)

def hat():
    #Kérjünk be a felhasználótól egy valós számot, majd adjuk meg a harmadát. 
    valos2=float(input("Kérek egy valós számot: "))
    harmad=valos2//3
    print(harmad)

def het():
    atmero=int(input("Kérem a medence átmérőjét: "))
    magassag=int(input("Kérem a medence magaságát: "))

    terfogat=math.pi*(math.pow(atmero//2,2))*magassag
    print(terfogat)


    

    
  








def main():
    #elso()
    #masodik()
    #harmadik()
    #negyedik()
    #ot()
    #hat()
    het()



main()


