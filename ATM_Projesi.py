sifre = 1453
bakiye = 10000

while(True):
	print("HOSGELDINIZ, LUTFEN KARTI GIRDIGINIZI DOGRULAYIN (E/H)")
	dogrulama = input()

	kontrol = 3

	sayac = 1

	if(dogrulama == "E" or dogrulama == "e"):
		print("Lutfen 4 haneli sifrenizi giriniz (Giris Hakki : {})".format(kontrol))
		_sifre = int(input())		
		
		while(_sifre != sifre):
		
			kontrol -= 1
		
			if(kontrol == 0):
				print("Kartiniza guvenlik sebebi ile el konulmustur")
				print("Lutfen sorunun cozumu icin bankanizla iletisime geciniz")
				break
			
			print("Lutfen tekrar deneyiniz (Giris Hakki : {})".format(kontrol))
			_sifre = int(input())
			
		
		while(_sifre == sifre):
			
			if(sayac == 1):
				print("Giris Basarili")
				sayac-=1
				
			print("Lutfen yapmak istediginiz islemi listeden secin\n")
			liste = ["1.Bakiye Sorma","2.Para Cekme","3.Para Yatirma","4.Sifre Degistirme","5.Cikis\n"]
			for i in liste:
				print(i)
			secim = int(input("Secim : "))
			
			if(secim == 1):
				print("Bakiye kontrolu yapiliyor, lutfen bekleyiniz...")
				print("Guncel Bakiye : ", bakiye,"€\n")
				
				print("< Geri gitmek icin 'g' tusuna basin ", end = "")
				secim = input()
				print("\n")
				
				if(secim == "g"):
					continue
			if(secim == 2):
				while(True):
					print("Guncel Bakiye : ", bakiye,"€")
					print("Lutfen cekmek istediginiz tutari girin : ")
					tutar = int(input())
				
					if(tutar > bakiye):
						print("Yetersiz Bakiye...\n")
						continue
					else:
						bakiye -= tutar
						print("Lutfen paranizi aliniz...\n")
						print("Guncel Bakiye : ", bakiye,"€\n")
						print("< Geri gitmek icin 'g' tusuna basin ", end = "")
						secim = input()
						print("\n")
						if(secim == "g"):
							break
				continue
				
			if(secim == 3):
			
				while(True):
					print("Guncel Bakiye : ", bakiye,"€")
					print("Lutfen yatirmak istediginiz tutari girin (Tek seferde en fazla 5000 € ' dur) : ")
					tutar = int(input())
				
					if(tutar > 5000):
						print("Maximum yukleme yapilacak tutari gectiniz...")
						print("Lutfen tekrar deneyiniz...")
						continue
					else:
						bakiye += tutar
						print("Lutfen Bekleyiniz...\n")
						print("Guncel Bakiye : ", bakiye,"€\n")
						print("< Geri gitmek icin 'g' tusuna basin ", end = "")
						secim = input()
						print("\n")
						if(secim == "g"):
							break
				continue
			
			if(secim == 4):
				print("Lutfen asagiya yeni sifrenizi giriniz...")
				_sifre = int(input("Yeni sifre : "))
				sifre = _sifre
				print("Sifreniz basarili bir sekilde degistirilmistir...\n")
				print("< Geri gitmek icin 'g' tusuna basin ", end = "")
				secim = input()
				print("\n")
				if(secim == "g"):
					continue
		
			if(secim == 5):
				print("Bizi tercih ettiginiz icin tesekkurler...")
				print("Cikis yapiliyor...")
				break
	continue		
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
				
				
	
			
