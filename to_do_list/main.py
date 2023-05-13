import pathlib
from to_do import exist
from os import system
from time import sleep


def wstep():
    global wybor 
    print(wybor)
    system("title To_Do_List")
    system("cls")
    print("TO DO LIST")
    print("1.Wypisanie zawartosci pliku")
    print("2.Wpisanie nowego zadania ")
    print("3.Wyczyszczenie calej to_do_list ")
    print("4.Usuniecie konkretnego elementu z listy")


    wybor=int(input(""))
    if wybor==1:
        system("cls")
        print("Wypisywanie: ")
    elif wybor==2:
        system("cls")
        print("Nadpisanie: ")
    elif wybor==3:
        system("cls")
        print("Czyszczenie:")
    elif wybor==4:
        system("cls")
        print("Ktory element chcesz usunac? ")
    else:
        system("cls")
        print("Wychodznie")
        exit()



       
while True:   
    system("cls")
    sciezka=input("Podaj sciezke do pliku: ")

    path=pathlib.Path(sciezka)
    linijka=0
    wybor=0
    ilosc=0
    tekst=[]
    x=exist(path)
    if x==1:
        while True:
            
            wstep()
            if wybor==1:
                tekst=[]
                path=str(path)
                file=open(path,"r",encoding="utf-8")
                for line in file: 
                    tekst.append(line)
                file.close()

                ilosc=0
                for x in range (0,len(tekst)):
                    print(f"{x+1}.{tekst[x]}",end="")
                if tekst==[]:
                    print("Brak zadan")
                file.close()
                system("pause>nul")
            elif wybor==2:
                file=open(path,"a",encoding="utf-8")
                x=input("Podaj linie:")

                file.write(x)
                file.write("\n")
                file.close()
                file=open(path,"r",encoding="utf-8")
                ilosc=0
                for line in file:

                    ilosc+=1
                    print(f"{ilosc}.{line}",end="")
                file.close()
                system("pause>nul")
            elif wybor==3:
                file=open(path,"w",encoding="utf-8")
                file.write("")
                ilosc=0
                file.close()
                sleep(0.5)
                system("cls")
                for x in range(0,5):
                    print("Trwa.")
                    sleep(0.3)
                    system("cls")
                    print("Trwa..")
                    sleep(0.3)
                    system("cls")
                    print("Trwa...")
                    sleep(0.3)
                    system("cls")
            elif wybor==4:
                tekst=[]
                ilosc=0
                file=open(path,"r",encoding="utf-8 ")
                for line in file:
                    ilosc+=1
                    print(f"{ilosc}.{line}",end="")
                    tekst.append(line)
                file.close()
                file=open(path,"w",encoding="utf-8")
                file.write("") 
                wynik=int(input(""))
                del tekst[wynik-1]     
                file.close()
                file=open(path,"r",encoding="utf-8")
                for line in file:
                    tekst.append(line)

                tekst.pop(wynik-1)
                file.close()
                file=open(path,"a",encoding="utf-8")
                for x in range (0,len(tekst)):
                    file.write(tekst[x])
                    file.write("\n")
                file.close()
                file=open(path,"r",encoding="utf-8")
                ilosc=0
                for line in file:
                    ilosc+=1
                    print(f"{ilosc}.{line}",end="")
                file.close()
                system("pause>nul")
    else:
        print("Bledna sciezka / brak pliku")
        system("pause>nul")
        continue
