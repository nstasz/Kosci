from tkinter import *
import tkinter as tk
import tkinter.messagebox as tkm
import random


#globalne
liczba_graczy= 4
obecnygracz = 0
cast = [0,0,0,0,0]
kopia_cast = cast
kostka1_zaznaczona = True #niewidzialne zaznaczenie
kostka2_zaznaczona = True
kostka3_zaznaczona = True
kostka4_zaznaczona = True
kostka5_zaznaczona = True
kostki_zaznaczone = [kostka1_zaznaczona, kostka2_zaznaczona, kostka3_zaznaczona, kostka4_zaznaczona, kostka5_zaznaczona]
imie_gracza = ["a","b","c","d"]
zostalo_rzutow = 2

okno_ilugraczy = Tk()
okno_ilugraczy.geometry("300x280+30+30")
okno_ilugraczy.resizable(width=False, height=False)


def wpiszgraczy():
	global imie_gracza
	for i in range(liczba_graczy):
		imie_gracza[i]=GraczXEntry[i].get()
	okno_ilugraczy.destroy()
	pokaz_plansze();

Przycisk_zatwierdz_graczy = tk.Button(okno_ilugraczy, text ="Zatwierdź liczbę graczy",  bd=3, command = wpiszgraczy)
Przycisk_zatwierdz_graczy.place(x = 20, y = 20, width=260, height=25) 

kolory = ["red", "black", "blue", "green", "orange", "yellow"]
def lewyklick_kwadratwyboru1(event):
	global liczba_graczy
	liczba_graczy = 1
	okno_ilugraczy.geometry("300x160+30+30") 
def lewyklick_kwadratwyboru2(event):
	global liczba_graczy
	liczba_graczy = 2
	okno_ilugraczy.geometry("300x200+30+30")
def lewyklick_kwadratwyboru3(event):
	okno_ilugraczy.geometry("300x240+30+30")
	global liczba_graczy
	liczba_graczy = 3
def lewyklick_kwadratwyboru4(event):
	global liczba_graczy
	liczba_graczy = 4
	okno_ilugraczy.geometry("300x280+30+30")
def malujliczbegraczy():
	kwadratwyboru1 = tk.Label(okno_ilugraczy, text="1", bg=kolory[0], fg="white", font=("Helvetica", 20)) 
	kwadratwyboru2 = tk.Label(okno_ilugraczy, text="2", bg=kolory[1], fg="white", font=("Helvetica", 20))
	kwadratwyboru3 = tk.Label(okno_ilugraczy, text="3", bg=kolory[2], fg="white", font=("Helvetica", 20)) 
	kwadratwyboru4 = tk.Label(okno_ilugraczy, text="4", bg=kolory[3], fg="white", font=("Helvetica", 20))

	kwadratwyboru1.bind("<Button-1>", lewyklick_kwadratwyboru1)
	kwadratwyboru2.bind("<Button-1>", lewyklick_kwadratwyboru2)
	kwadratwyboru3.bind("<Button-1>", lewyklick_kwadratwyboru3)
	kwadratwyboru4.bind("<Button-1>", lewyklick_kwadratwyboru4)
	kwadratwyboru = [kwadratwyboru1, kwadratwyboru2, kwadratwyboru3, kwadratwyboru4]
	for i in range (4):
		kwadratwyboru[i].place(x = 20+i*70, y = 60, width=50, height=50)
malujliczbegraczy()	

for i in range (liczba_graczy):  
	napis_nr_gracza=tk.Label(okno_ilugraczy, text="Gracz numer {}".format(i+1), bg=kolory[i], fg="white")
	napis_nr_gracza.place(x = 20, y = 120+i*40, width=120, height=25)

	Gracz1Entry	= Entry(okno_ilugraczy)  #stworz pole do wpisania imienia
	Gracz2Entry	= Entry(okno_ilugraczy)
	Gracz3Entry	= Entry(okno_ilugraczy)
	Gracz4Entry = Entry(okno_ilugraczy)

	GraczXEntry=  [Gracz1Entry, Gracz2Entry, Gracz3Entry, Gracz4Entry] #zawiera pola do wpisywania imion

	for i in range (liczba_graczy): 
		GraczXEntry[i] = Entry(okno_ilugraczy, bd =2, justify = CENTER)
		GraczXEntry[i].insert(0,"Gracz {}".format(i+1))
		GraczXEntry[i].place(x = 160, y = 120+i*40, width=120, height=25) #postaw pola do wpisywania imion na planszy

def pokaz_plansze():
	global imie_gracza
	okno_gra = Tk()
	okno_gra.geometry("800x800+30+30")
	
	#rysuj_plansze
	#pierwsza kolumna
	tresc_pierwszakolumna = ["Pole", "1", "2", "3", "4", "5", "6", "= (+)", "3x", "4x", "3+2x", "mały strit", "duży strit", "generał", "szansa", "="]	
	for i in range(16): 
				if (i == 0 or i == 7 or i == 15):
					labele_pierwszakolumna = tk.Label(okno_gra, text=tresc_pierwszakolumna[i], width=15, borderwidth=0, bg="darkgrey", fg="white", font=("Helvetica", 14))
				else:
					if (i == 2 or i == 4 or i == 6 or i == 8 or i == 10 or i == 12 or i == 14):
						labele_pierwszakolumna = tk.Label(okno_gra, text=tresc_pierwszakolumna[i], width=12, borderwidth=0, bg="lightgrey", font=("Helvetica", 14))
					else:
						labele_pierwszakolumna = tk.Label(okno_gra, text=tresc_pierwszakolumna[i], width=12, borderwidth=0, font=("Helvetica", 14))
				labele_pierwszakolumna.grid(row=i, column=0)
				
	for i in range(liczba_graczy):  #nagłówki dla imion graczy
			label_nazwa_gracza = tk.Label(okno_gra, text=imie_gracza[i], width=15, borderwidth=0, bg=kolory[i], fg="white", font=("Helvetica 12 bold"))
			
			label_nazwa_gracza.grid(row=0, column=i+1)
				
					   
			graczwyniki = [[[0, False],[0, False],[0, False],[0, False],[0, False],[0, False],[0, True],[0, False],[0, False],[0, False],[0, False],[0, False],[0, False],[0, False],[0, True]], 
						   [[0, False],[0, False],[0, False],[0, False],[0, False],[0, False],[0, True],[0, False],[0, False],[0, False],[0, False],[0, False],[0, False],[0, False],[0, True]],
						   [[0, False],[0, False],[0, False],[0, False],[0, False],[0, False],[0, True],[0, False],[0, False],[0, False],[0, False],[0, False],[0, False],[0, False],[0, True]],
							[[0, False],[0, False],[0, False],[0, False],[0, False],[0, False],[0, True],[0, False],[0, False],[0, False],[0, False],[0, False],[0, False],[0, False],[0, True]],]
			
	for x in range(liczba_graczy): #początek gry
				for y in range(15):
				
					if (y == 6 or y == 14):
						label_poczatek_gry = tk.Label(okno_gra, text=graczwyniki[x][y][0], width=12, borderwidth=0, bg="black", fg="white", font=("Helvetica", 14))
					else:
						if (y == 1 or y == 3 or y == 5 or y == 7 or y == 9 or y == 11 or y == 13):
							if graczwyniki[x][y][1] == False:
								label_poczatek_gry = tk.Label(okno_gra, text=graczwyniki[x][y][0], width=12, borderwidth=0, bg="lightgrey", fg="grey", font=("Helvetica", 14))
							if graczwyniki[x][y][1] == True:
								label_poczatek_gry = tk.Label(okno_gra, text=graczwyniki[x][y][0], width=12, borderwidth=0, bg="lightgrey", fg="black", font=("Helvetica 14"))	
						else:
							if graczwyniki[x][y][1] == False:
								label_poczatek_gry = tk.Label(okno_gra, text=graczwyniki[x][y][0], width=12, borderwidth=0, bg="white", fg="grey", font=("Helvetica", 14))
							if graczwyniki[x][y][1] == True:
								label_poczatek_gry = tk.Label(okno_gra, text=graczwyniki[x][y][0], width=12, borderwidth=0, bg="white", fg="black", font=("Helvetica 14"))
					label_poczatek_gry.grid(row=y+1, column=x+1)
	def nowatura():
	
		global obecnygracz
		graczwyniki[obecnygracz][6][0] = 0
		graczwyniki[obecnygracz][14][0] = 0
		for i in range(6):	#generowanie dwóch sum na planszy
			graczwyniki[obecnygracz][6][0] = graczwyniki[obecnygracz][6][0] + graczwyniki[obecnygracz][i][0] 
		for i in range(8):	
			graczwyniki[obecnygracz][14][0] = graczwyniki[obecnygracz][14][0] + graczwyniki[obecnygracz][i+6][0] 	
						
		obecnygracz=obecnygracz+1
		if obecnygracz == liczba_graczy:		 #czyli tak naprawdę 5
			obecnygracz = 0
		
		gra_sie_skonczyla = True #ale spokojnie zaraz zaprzeczam
		for x in range(liczba_graczy): #rysowanie tabeli
			for y in range(15):
				if (y == 6 or y == 14):
					label_poczatek_gry = tk.Label(okno_gra, text=graczwyniki[x][y][0], width=12, borderwidth=0, bg="black", fg="white", font=("Helvetica", 14))
				else:
					if (y == 1 or y == 3 or y == 5 or y == 7 or y == 9 or y == 11 or y == 13):
						if graczwyniki[x][y][1] == False:
							label_poczatek_gry = tk.Label(okno_gra, text=graczwyniki[x][y][0], width=12, borderwidth=0, bg="lightgrey", fg="grey", font=("Helvetica", 14))
						if graczwyniki[x][y][1] == True:
							label_poczatek_gry = tk.Label(okno_gra, text=graczwyniki[x][y][0], width=12, borderwidth=0, bg="lightgrey", fg="black", font=("Helvetica 14"))	
					else:
						if graczwyniki[x][y][1] == False:
							label_poczatek_gry = tk.Label(okno_gra, text=graczwyniki[x][y][0], width=12, borderwidth=0, bg="white", fg="grey", font=("Helvetica", 14))
						if graczwyniki[x][y][1] == True:
							label_poczatek_gry = tk.Label(okno_gra, text=graczwyniki[x][y][0], width=12, borderwidth=0, bg="white", fg="black", font=("Helvetica 14"))
				label_poczatek_gry.grid(row=y+1, column=x+1)
				
				###sprawdzanie czy koniec gry!!!
				if graczwyniki[x][y][1] == False:
					gra_sie_skonczyla = False
		global imie_gracza
		remis = False
		zwyciezca = imie_gracza[0] #bo łatwiej napisać tak remis
		wynik_zwyciezcy = graczwyniki[0][14][0]
		if gra_sie_skonczyla == True:
			if liczba_graczy > 1:
				for i in range (liczba_graczy-1):
					if graczwyniki[i][14][0] > graczwyniki[i+1][14][0]:
						wynik_zwyciezcy = graczwyniki[i][14][0]
						zwyciezca = imie_gracza[i]
					else:
						if wynik_zwyciezcy == graczwyniki[i+1][14][0]:
							wynik_zwyciezcy = graczwyniki[i][14][0] 
							remis = True
							zwyciezca = "{} i {}".format(imie_gracza[i],imie_gracza[i+1])
						else:
							wynik_zwyciezcy = graczwyniki[i+1][14][0]
							zwyciezca = imie_gracza[i+1]
							remis = False
				if remis == True: 
					tkm.showinfo("Koniec gry!", "{} wygrywają turniej remisem. Piękne gratulacje. \n\nLiczba punktów: {}.".format(zwyciezca, wynik_zwyciezcy))
				else:
					tkm.showinfo("Koniec gry!", "{} wygrywa turniej. Piękne gratulacje. \n\nLiczba punktów: {}.".format(zwyciezca, wynik_zwyciezcy))
			else:	
				tkm.showinfo("Koniec gry!", "{}. \n\nLiczba punktów: {}".format(zwyciezca, wynik_zwyciezcy))
		for i in range (5):
			kostki_zaznaczone[i] = True
		
		
		rzuckoscia()
	

			

				

	def rzuckoscia(): #OGÓLNE RZUCANIE
		global cast
		global kostka1_zaznaczona 
		global kostka2_zaznaczona 
		global kostka3_zaznaczona 
		global kostka4_zaznaczona 
		global kostka5_zaznaczona 
		global kopia_cast 
		global kostki_zaznaczone
		global zostalo_rzutow
		zostalo_rzutow = 2
		kostka1_zaznaczona = False #niewidzialne zaznaczenie
		kostka2_zaznaczona = False
		kostka3_zaznaczona = False
		kostka4_zaznaczona = False
		kostka5_zaznaczona = False

		##generowanie kości

		kopia_cast = cast
		for i in range(5): #RZUĆ KOŚCIĄ PIĘĆ RAZY JEŚLI WSZYSTKIE SĄ ZAZNACZONE. PRZY STARCIE GRY WSZYSTKIE SĄ NIEWIDZIALNIE ZAZNACZONE
			cast[i] = random.randint(1, 6)
	

	
				
	
		
		def lewyklick_kostka1odznacz(event): #kostka 1
					global kostka1_zaznaczona
					kostka1_zaznaczona = False
					kostka1odznaczona = tk.Label(okno_gra, text=cast[0], bg="green", fg="black", font=("Helvetica", 35), bd=1200)
					kostka1odznaczona.bind("<Button-1>", lewyklick_kostka1zaznacz)
					kostka1odznaczona.place(x = 30+1*120, y = 450, width=100, height=100)
		def lewyklick_kostka1zaznacz(event):
					global kostka1_zaznaczona
					kostka1_zaznaczona = True
					kostka1zaznaczona = tk.Label(okno_gra, text=cast[0], bg="yellow", fg="black", font=("Helvetica", 35), bd=1200)
					kostka1zaznaczona.bind("<Button-1>", lewyklick_kostka1odznacz)
					kostka1zaznaczona.place(x = 30+1*120, y = 450, width=100, height=100)	
		def lewyklick_kostka2odznacz(event): #kostka 2
					global kostka2_zaznaczona
					kostka2_zaznaczona = False
					kostka2odznaczona = tk.Label(okno_gra, text=cast[1], bg="green", fg="black", font=("Helvetica", 35), bd=1200)
					kostka2odznaczona.bind("<Button-1>", lewyklick_kostka2zaznacz)
					kostka2odznaczona.place(x = 30+2*120, y = 450, width=100, height=100)
		def lewyklick_kostka2zaznacz(event):
					global kostka2_zaznaczona
					kostka2_zaznaczona = True
					kostka2zaznaczona = tk.Label(okno_gra, text=cast[1], bg="yellow", fg="black", font=("Helvetica", 35), bd=1200)
					kostka2zaznaczona.bind("<Button-1>", lewyklick_kostka2odznacz)
					kostka2zaznaczona.place(x = 30+2*120, y = 450, width=100, height=100)	
		def lewyklick_kostka3odznacz(event): #kostka 3
					global kostka3_zaznaczona
					kostka3_zaznaczona = False
					kostka3odznaczona = tk.Label(okno_gra, text=cast[2], bg="green", fg="black", font=("Helvetica", 35), bd=1200)
					kostka3odznaczona.bind("<Button-1>", lewyklick_kostka3zaznacz)
					kostka3odznaczona.place(x = 30+3*120, y = 450, width=100, height=100)
		def lewyklick_kostka3zaznacz(event):
					global kostka3_zaznaczona
					kostka3_zaznaczona = True
					kostka3zaznaczona = tk.Label(okno_gra, text=cast[2], bg="yellow", fg="black", font=("Helvetica", 35), bd=1200)
					kostka3zaznaczona.bind("<Button-1>", lewyklick_kostka3odznacz)
					kostka3zaznaczona.place(x = 30+3*120, y = 450, width=100, height=100)	
		def lewyklick_kostka4odznacz(event): #kostka 4
					global kostka4_zaznaczona
					kostka4_zaznaczona = False
					kostka4odznaczona = tk.Label(okno_gra, text=cast[3], bg="green", fg="black", font=("Helvetica", 35), bd=1200)
					kostka4odznaczona.bind("<Button-1>", lewyklick_kostka4zaznacz)
					kostka4odznaczona.place(x = 30+4*120, y = 450, width=100, height=100)
		def lewyklick_kostka4zaznacz(event):
					global kostka4_zaznaczona
					kostka4_zaznaczona = True
					kostka4zaznaczona = tk.Label(okno_gra, text=cast[3], bg="yellow", fg="black", font=("Helvetica", 35), bd=1200)
					kostka4zaznaczona.bind("<Button-1>", lewyklick_kostka4odznacz)
					kostka4zaznaczona.place(x = 30+4*120, y = 450, width=100, height=100)		
		def lewyklick_kostka5odznacz(event): #kostka 5
					global kostka5_zaznaczona
					kostka5_zaznaczona = False
					kostka5odznaczona = tk.Label(okno_gra, text=cast[4], bg="green", fg="black", font=("Helvetica", 35), bd=1200)
					kostka5odznaczona.bind("<Button-1>", lewyklick_kostka5zaznacz)
					kostka5odznaczona.place(x = 30+5*120, y = 450, width=100, height=100)
		def lewyklick_kostka5zaznacz(event):
					global kostka5_zaznaczona
					kostka5_zaznaczona= True
					kostka5zaznaczona = tk.Label(okno_gra, text=cast[4], bg="yellow", fg="black", font=("Helvetica", 35), bd=1200)
					kostka5zaznaczona.bind("<Button-1>", lewyklick_kostka5odznacz)
					kostka5zaznaczona.place(x = 30+5*120, y = 450, width=100, height=100)	
					
		def generuj_podstawowa_kosc1(): #pierwszy rzut przy tworzeniu planszy
			kostka1 = tk.Label(okno_gra, text=cast[0], bg="green", fg="black", font=("Helvetica", 35), bd=1200)
			kostka1.place(x = 30+120, y = 450, width=100, height=100) 
			kostka1.bind("<Button-1>", lewyklick_kostka1zaznacz)
		def generuj_podstawowa_kosc2():			
			kostka2 = tk.Label(okno_gra, text=cast[1], bg="green", fg="black", font=("Helvetica", 35), bd=1200)
			kostka2.place(x = 30+2*120, y = 450, width=100, height=100) 
			kostka2.bind("<Button-1>", lewyklick_kostka2zaznacz)
		def generuj_podstawowa_kosc3():				
			kostka3 = tk.Label(okno_gra, text=cast[2], bg="green", fg="black", font=("Helvetica", 35), bd=1200)
			kostka3.place(x = 30+3*120, y = 450, width=100, height=100) 
			kostka3.bind("<Button-1>", lewyklick_kostka3zaznacz)
		def generuj_podstawowa_kosc4():				
			kostka4 = tk.Label(okno_gra, text=cast[3], bg="green", fg="black", font=("Helvetica", 35), bd=1200)
			kostka4.place(x = 30+4*120, y = 450, width=100, height=100) 
			kostka4.bind("<Button-1>", lewyklick_kostka4zaznacz)
		def generuj_podstawowa_kosc5():				
			kostka5 = tk.Label(okno_gra, text=cast[4], bg="green", fg="black", font=("Helvetica", 35), bd=1200)
			kostka5.place(x = 30+5*120, y = 450, width=100, height=100) 
			kostka5.bind("<Button-1>", lewyklick_kostka5zaznacz)	
		generuj_podstawowa_kosc1()	
		generuj_podstawowa_kosc2()
		generuj_podstawowa_kosc3()
		generuj_podstawowa_kosc4()
		generuj_podstawowa_kosc5()
			
			
		def wykonaj_testy():
#Jest 10 testów na porównanie każdej kości z każdą. 
			#Wyniki: 	x=10, czyli generał (chociaż można to sprawdzić prościej)
			#			x=6, czyli są 4 takie same kości
			#			x=4, czyli 3a+2b   (jest takie pole)				
			#			x=3, czyli 3a+b+c  (jest takie pole)
			#			x=2, czyli 2a+2b+c
			#			x=1, czyli 2a+b+c+d
			#			x=a. czyli a+b+c+d+e (mały albo duży strit)
			x = 0
			for y in range(4):
				for z in range (4-y):
					if cast[y] == cast[4-z]:
						x = x+1
						
						
			def dodaj_ewentualne_dodatkowe_generaly():
						if graczwyniki[obecnygracz][12][1]==True:
							if graczwyniki[obecnygracz][12][0] != 0:
								if x == 10:
									graczwyniki[obecnygracz][12][0] = graczwyniki[obecnygracz][12][0] + 100
			def lewyklick_jedynki(event):
						graczwyniki[obecnygracz][0][0] = propozycja_jedynek
						graczwyniki[obecnygracz][0][1] = True
						dodaj_ewentualne_dodatkowe_generaly()
						nowatura()
			def lewyklick_dwojki(event):
						graczwyniki[obecnygracz][1][0] = propozycja_dwojek
						graczwyniki[obecnygracz][1][1] = True
						dodaj_ewentualne_dodatkowe_generaly()
						nowatura()
			def lewyklick_trojki(event):
						graczwyniki[obecnygracz][2][0] = propozycja_trojek
						graczwyniki[obecnygracz][2][1] = True
						dodaj_ewentualne_dodatkowe_generaly()
						nowatura()
			def lewyklick_czworki(event):
						graczwyniki[obecnygracz][3][0] = propozycja_czworek
						graczwyniki[obecnygracz][3][1] = True
						dodaj_ewentualne_dodatkowe_generaly()
						nowatura()
			def lewyklick_piatki(event):
						graczwyniki[obecnygracz][4][0] = propozycja_piatek
						graczwyniki[obecnygracz][4][1] = True
						dodaj_ewentualne_dodatkowe_generaly()
						nowatura()
			def lewyklick_szostki(event):
						graczwyniki[obecnygracz][5][0] = propozycja_szostek
						graczwyniki[obecnygracz][5][1] = True
						dodaj_ewentualne_dodatkowe_generaly()
						nowatura()	
				
			def lewyklick_3a(event):
						graczwyniki[obecnygracz][7][0] = propozycja_3a
						graczwyniki[obecnygracz][7][1] = True
						dodaj_ewentualne_dodatkowe_generaly()
						nowatura()
			def lewyklick_4a(event):
						graczwyniki[obecnygracz][8][0] = propozycja_4a
						graczwyniki[obecnygracz][8][1] = True				
						dodaj_ewentualne_dodatkowe_generaly()
						nowatura()
			def lewyklick_3a2b(event):
						graczwyniki[obecnygracz][9][0] = propozycja_3a2b
						graczwyniki[obecnygracz][9][1] = True				
						dodaj_ewentualne_dodatkowe_generaly()
						nowatura()
			def lewyklick_malystrit(event):
						graczwyniki[obecnygracz][10][0] = propozycja_malystrit
						graczwyniki[obecnygracz][10][1] = True				
						dodaj_ewentualne_dodatkowe_generaly()
						nowatura()		
			def lewyklick_duzystrit(event):
						graczwyniki[obecnygracz][11][0] = propozycja_duzystrit
						graczwyniki[obecnygracz][11][1] = True				
						dodaj_ewentualne_dodatkowe_generaly()
						nowatura()
			def lewyklick_general(event):
						graczwyniki[obecnygracz][12][0] = propozycja_general
						graczwyniki[obecnygracz][12][1] = True	
						#tutaj nie dodaje DODATKOWYCH generałów, tylko pierwszy. Następne dopiero, jak ten przejdzie		
						nowatura()				
			def lewyklick_szansa(event):
						graczwyniki[obecnygracz][13][0] = propozycja_szansa
						graczwyniki[obecnygracz][13][1] = True		
						dodaj_ewentualne_dodatkowe_generaly()
						nowatura()					
					
		
			#testy
			#jedynki-szóstki
			if graczwyniki[obecnygracz][0][1]==False:
					propozycja_jedynek = cast.count(1)
					label_propozycja = tk.Label(okno_gra, text=propozycja_jedynek, width=12, borderwidth=0, bg="yellow", fg="red", font=("Helvetica", 14)) #jedynki
					label_propozycja.grid(row=1,column=obecnygracz+1)
					label_propozycja.bind("<Button-1>", lewyklick_jedynki)	
			if graczwyniki[obecnygracz][1][1]==False:
					propozycja_dwojek = 2*cast.count(2)
					label_propozycja = tk.Label(okno_gra, text=propozycja_dwojek, width=12, borderwidth=0, bg="gold", fg="red", font=("Helvetica", 14)) #dwójki
					label_propozycja.grid(row=2,column=obecnygracz+1)
					label_propozycja.bind("<Button-1>", lewyklick_dwojki)
			if graczwyniki[obecnygracz][2][1]==False:
					propozycja_trojek = 3*cast.count(3)
					label_propozycja = tk.Label(okno_gra, text=propozycja_trojek, width=12, borderwidth=0, bg="yellow", fg="red", font=("Helvetica", 14)) #trojki
					label_propozycja.grid(row=3,column=obecnygracz+1)
					label_propozycja.bind("<Button-1>", lewyklick_trojki)
			if graczwyniki[obecnygracz][3][1]==False: 
					propozycja_czworek = 4*cast.count(4)
					label_propozycja = tk.Label(okno_gra, text=propozycja_czworek, width=12, borderwidth=0, bg="gold", fg="red", font=("Helvetica", 14)) #czworki
					label_propozycja.grid(row=4,column=obecnygracz+1)
					label_propozycja.bind("<Button-1>", lewyklick_czworki)
			if graczwyniki[obecnygracz][4][1]==False: 
					propozycja_piatek = 5*cast.count(5)
					label_propozycja = tk.Label(okno_gra, text=propozycja_piatek, width=12, borderwidth=0, bg="yellow", fg="red", font=("Helvetica", 14)) #piatki
					label_propozycja.grid(row=5,column=obecnygracz+1)
					label_propozycja.bind("<Button-1>", lewyklick_piatki)	
			if graczwyniki[obecnygracz][5][1]==False: 
					propozycja_szostek = 6*cast.count(6)
					label_propozycja = tk.Label(okno_gra, text=propozycja_szostek, width=12, borderwidth=0, bg="gold", fg="red", font=("Helvetica", 14)) #szostki
					label_propozycja.grid(row=6,column=obecnygracz+1)
					label_propozycja.bind("<Button-1>", lewyklick_szostki)	


						
			if graczwyniki[obecnygracz][7][1]==False:  #3a+b+c
				
				if x >= 3:
					propozycja_3a = (cast[0]+cast[1]+cast[2]+cast[3]+cast[4])
					label_propozycja = tk.Label(okno_gra, text=propozycja_3a, width=12, borderwidth=0, bg="gold", fg="red", font=("Helvetica", 14))
				else:
					propozycja_3a = 0
					label_propozycja = tk.Label(okno_gra, text=(propozycja_3a), width=12, borderwidth=0, bg="gold", fg="red", font=("Helvetica", 14))				
				label_propozycja.grid(row=8,column=obecnygracz+1)
				label_propozycja.bind("<Button-1>", lewyklick_3a)
				
			if graczwyniki[obecnygracz][8][1]==False:  #4a+b
				
				if (x == 6 or x == 10):
					propozycja_4a = (cast[0]+cast[1]+cast[2]+cast[3]+cast[4])
					label_propozycja = tk.Label(okno_gra, text=(propozycja_4a), width=12, borderwidth=0, bg="yellow", fg="red", font=("Helvetica", 14))
				else:
					propozycja_4a = 0
					label_propozycja = tk.Label(okno_gra, text=(propozycja_4a), width=12, borderwidth=0, bg="yellow", fg="red", font=("Helvetica", 14))				
				label_propozycja.grid(row=9,column=obecnygracz+1)
				label_propozycja.bind("<Button-1>", lewyklick_4a)
			
			if graczwyniki[obecnygracz][9][1]==False:  #3a+2b
				
				if x == 4:
					propozycja_3a2b = 25
					label_propozycja = tk.Label(okno_gra, text=propozycja_3a2b, width=12, borderwidth=0, bg="gold", fg="red", font=("Helvetica", 14))
				else:
					propozycja_3a2b = 0
					label_propozycja = tk.Label(okno_gra, text=(propozycja_3a2b), width=12, borderwidth=0, bg="gold", fg="red", font=("Helvetica", 14))				
				label_propozycja.grid(row=10,column=obecnygracz+1)
				label_propozycja.bind("<Button-1>", lewyklick_3a2b)
			
			#test wstępny dla małego strita
			jest_jedynka=False
			jest_dwojka=False
			jest_piatka=False
			jest_szostka=False			
			for i in range (5):
				if cast[i] == 1:
					jest_jedynka = True
				if cast[i] == 2:
					jest_dwojka = True	
				if cast[i] == 5:
					jest_piatka = True					
				if cast[i] == 6:
					jest_szostka = True
				
					
			if graczwyniki[obecnygracz][10][1]==False:  #mały strit
				
				if x == 0 or (x == 1 and ((jest_szostka == False and jest_piatka == False) or (jest_szostka == False and jest_jedynka == False) or (jest_jedynka == False and jest_dwojka == False))):
					propozycja_malystrit = 30	
					label_propozycja = tk.Label(okno_gra, text=propozycja_malystrit, width=12, borderwidth=0, bg="yellow", fg="red", font=("Helvetica", 14))
				else:
					propozycja_malystrit = 0
					label_propozycja = tk.Label(okno_gra, text=propozycja_malystrit, width=12, borderwidth=0, bg="yellow", fg="red", font=("Helvetica", 14))				
				label_propozycja.grid(row=11,column=obecnygracz+1)
				label_propozycja.bind("<Button-1>", lewyklick_malystrit)

			if graczwyniki[obecnygracz][11][1]==False:  #duży strit
				
				if x == 0:						
					propozycja_duzystrit = 40	
					label_propozycja = tk.Label(okno_gra, text=propozycja_duzystrit, width=12, borderwidth=0, bg="gold", fg="red", font=("Helvetica", 14))
				else:
					propozycja_duzystrit = 0
					label_propozycja = tk.Label(okno_gra, text=propozycja_duzystrit, width=12, borderwidth=0, bg="gold", fg="red", font=("Helvetica", 14))				
				label_propozycja.grid(row=12,column=obecnygracz+1)	
				label_propozycja.bind("<Button-1>", lewyklick_duzystrit)				
			
			if graczwyniki[obecnygracz][12][1]==False:  #generał
				if x == 10:	
					propozycja_general = 50
					label_propozycja = tk.Label(okno_gra, text=propozycja_general, width=12, borderwidth=0, bg="yellow", fg="red", font=("Helvetica", 14))
				else:
					propozycja_general = 0
					label_propozycja = tk.Label(okno_gra, text=propozycja_general, width=12, borderwidth=0, bg="yellow", fg="red", font=("Helvetica", 14))				
				label_propozycja.grid(row=13,column=obecnygracz+1)	
				label_propozycja.bind("<Button-1>", lewyklick_general)
			
			if graczwyniki[obecnygracz][13][1]==False: #szansa
				propozycja_szansa = (cast[0]+cast[1]+cast[2]+cast[3]+cast[4])
				label_propozycja = tk.Label(okno_gra, text=propozycja_szansa, width=12, borderwidth=0, bg="gold", fg="red", font=("Helvetica", 14)) 
				label_propozycja.grid(row=14,column=obecnygracz+1)
				label_propozycja.bind("<Button-1>", lewyklick_szansa)		
		wykonaj_testy()
		def lewyklick_button_rzuc_koscia():  #button rzuć wybranymi
			global cast
			global kostka1_zaznaczona 
			global kostka2_zaznaczona 
			global kostka3_zaznaczona 
			global kostka4_zaznaczona 
			global kostka5_zaznaczona 
			global kopia_cast
			global zostalo_rzutow
			kopia_cast = cast
			
			if (kostka1_zaznaczona == True or kostka2_zaznaczona == True or kostka3_zaznaczona == True or kostka4_zaznaczona == True or kostka5_zaznaczona == True):
				if kostka1_zaznaczona == True:
					cast[0] = random.randint(1, 6)
					generuj_podstawowa_kosc1()	
					kostka1_zaznaczona = False
				if kostka2_zaznaczona == True:
					cast[1] = random.randint(1, 6)
					generuj_podstawowa_kosc2()	
					kostka2_zaznaczona = False
				if kostka3_zaznaczona == True: 
					cast[2] = random.randint(1, 6)
					generuj_podstawowa_kosc3()	
					kostka3_zaznaczona = False
				if kostka4_zaznaczona == True: 
					cast[3] = random.randint(1, 6)
					generuj_podstawowa_kosc4()	
					kostka4_zaznaczona = False
				if kostka5_zaznaczona == True: 
					cast[4] = random.randint(1, 6)
					generuj_podstawowa_kosc5()	
					kostka5_zaznaczona = False
					
				zostalo_rzutow = zostalo_rzutow -1
				
				if zostalo_rzutow > 0:
					Przycisk_rzuc_koscia = tk.Button(okno_gra, text ="Rzuć zaznaczonymi kośćmi\n\nPozostało rzutów: {}".format(zostalo_rzutow),  bd=2, command = lewyklick_button_rzuc_koscia)

				if zostalo_rzutow == 0:	
					Przycisk_rzuc_koscia = tk.Button(okno_gra, text ="Brak rzutów".format(zostalo_rzutow),  bd=2, bg="red")
					zostalo_rzutow = 3  #bo i tak się zmniejszy o 0
				Przycisk_rzuc_koscia.place(x = 400, y = 600, width=200, height=100)
				wykonaj_testy()

		Przycisk_rzuc_koscia = tk.Button(okno_gra, text ="Rzuć zaznaczonymi kośćmi\n\nPozostało rzutów: {}".format(zostalo_rzutow),  bd=2, command = lewyklick_button_rzuc_koscia)
		Przycisk_rzuc_koscia.place(x = 400, y = 600, width=200, height=100) 
			

		
			
	rzuckoscia()
	
okno_ilugraczy.mainloop(0)

