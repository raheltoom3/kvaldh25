lause1="Kui Arno isaga koolimajja jõudis olid tunnid juba alanud"
lause2="Mu isamaa mu õnn ja rõõm kui kaunis oled sa"

#leia T-testi abil, kas nende lausete sõnade keskmine pikkus erineb üldistavalt

#kõigepealt leia sõnade pikkused

sonad1=lause1.split() #splitin lause sõnadeks
print(sonad1) #näita sõnu
print(sonad1[3]) #näita kolmandat sõna
print(len("tere"))
#kuva sõna nr 3 kolm tähtede arv
print(len(sonad1[3])) 
print(len(sonad1)) #sõnu lauses kokku

sonapikkused1=[len(sona) for sona in sonad1]

sonad2=lause2.split()
print(sonad2)
print(sonad2[3])
#kuva sõna nr 3 kolm tähtede arv
print(len(sonad2[3]))
print(len(sonad2)) #sõnu lauses kokku
sonapikkused2=[len(sona) for sona in sonad1]
=======
#Leia T-testi abil, kas nende lausete sõnade keskmine pikkus erineb üldistatavalt
sonad1=lause1.split()
print(sonad1)
print(sonad1[3])
print(len("tere"))
#Kuva sõna nr 3 tähtede arv
print(len(sonad1[3]))
print(len(sonad1)) #Sõnu lauses kokku
sonapikkused1=[len(sona) for sona in sonad1]
print(sonapikkused1)
>>>>>>> origin/main

