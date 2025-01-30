# # Asso Eesmäe
# #30.01.25

# #1.1 koosta programm, mis väljastab ekraanile teksti "Tere, maailm!"
# print('Tere, maailm!')
# #1.2 aasta liblikas
# #koosta programm, mille
# #1. real luuakse muutuja nimega aasta ja omistatakse väärtus 2020
# #2. real luuakse muutuja nimega liblikas ja omistatakse väärtus "teelehe-mosaiikliblikas"
# #3. real luuakse muutuja nimeha lause_keskosa ja omistatakse väärtus ". aasta liblikas on "
# #4. real luuakse muutuja nimega lause, mille väärtuseks on muutuja aasta + muutuja lause_keskosa + muutuja liblikas
# #5. real väljastatakse muutuja lause väärtus

# aasta = 2020
# liblikas = "teelehe-mosaiikliblikas"
# lause_keskosa = ". aasta liblikas on "
# lause = str(aasta) + lause_keskosa + liblikas
# print(lause)

# # 1.3. Pilved
# # Pilvede alumise pinna (aluse) kõrguse järgi liigitatakse pilvi ülemise, keskmise ja alumise kihi pilvedeks. Ülemiste pilvede alus on kõrgemal kui 6 km, keskmistel pilvedel on 2-6 km kõrgusel, alumistel pilvedel on madalamal kui 2 km. Koostada programm, mis
# # küsib kasutajalt pilvede aluse kõrgust (kilomeetrites),
# # väljastab ekraanile Need on ülemised pilved, kui sisestatu on üle 6,0 km,
# # väljastab Need ei ole ülemised pilved, kui kõrgus on 6,0 km või alla selle.
# # Kasutaja peab saama sisestada pilvede kõrgust nii täisarvuna kui ka ujukomaarvuna, nt 7.5.

# korgus = float(input("Sisesta pilvede aluse kõrgus: "))
# if korgus > 6:
#     print("ülemised")
# elif korgus >= 2 and korgus <= 6:
#     print("keskmised")
# else:
#     print("Alumised")


# # 1.4. Bussid
# # Meil on vaja transportida teatud arv inimesi mingi arvu identsete bussidega. Eeldame, et reisijaid on vähemalt üks. 
# # Koostada programm, mis küsib transporditavate inimeste arvu ja ühe bussi kohtade arvu (just sellises järjekorras) ning 
# # väljastab ekraanile, mitu bussi on vaja ja mitu inimest on viimases bussis (eeldusel, et kõik eelnevad bussid on täis).

# import math
# inim = 80
# koht = 160
# jaak = inim % koht

# bussid_arv = math.ceil(inim / koht)
# if jaak > 0:
#     bussid_arv = (inim // koht) + 1
# elif jaak == 0:
#          bussid_arv = inim // koht
# else:
#     bussid_arv = inim // koht
# print(f"Busside arv: {bussid_arv}")
# print(f"Viimases bussis inimesi: {jaak}")

# 2.1 ÄRATUS
# Otil on hommikuti raske tõusta ja tal on äratuskell, mis äratab teda teatud arv kordi koos tervitustekstiga. 
# Koostada programm, mis
# küsib kasutajalt, mitu korda äratus heliseb ning
# väljastab sama arv kordi ekraanile Tõuse ja sära!.
# kordadearv = int(input("Kordade arv: "))
# for i in range(kordadearv):
#     print("Tõuse ja sära!")

# 2.2 MURELIKUD LAPSEVANEMAD
# Jänesevanemad on mures, et lapsed ei liigu piisavalt. Laste motiveerimiseks mõtlesid nad välja süsteemi, 
# kus 2. metsaringi läbimisel saab jänesepoeg 2 porgandit, 4. metsaringi läbimisel 4 porgandit juurde, 
# 6. metsaringi läbimisel 6 porgandit juurde jne. Paarituarvulistel ringidel porgandeid juurde ei saa. 

# Koostada programm, mis küsib kasutajalt ringide arvu (mittenegatiivne täisarv);
# arvutab while-tsükli abil saadavate porgandite koguarvu;
# väljastab saadavate porgandite koguarvu ekraanile.

# porgandid = 0
# ringide_arv = 6

# while ringide_arv > 0:
#     #print(ringide_arv)
#     if ringide_arv % 2 == 0:
#         porgandid += ringide_arv
#     ringide_arv -= 1
    
# print(porgandid)


# # 2.3 TÄRINGUD
# # Erinevate täringumängude jaoks on vajalik erinev arv täringuid. Näiteks Yahtzee (Yatzy) jaoks on vaja 5 täringut, 
# # Crapsi jaoks aga 2 täringut. Koostada programm, mis
# # küsib kasutajalt vajalike täringute arvu;
# # viskab vastava arvu täringuid (genereerib vastava arvu suvalisi arve, mis jäävad 1 ja 6 vahele);
# # väljastab iga arvu eraldi reale.


# Yatzy = 5
# Craps = 2
# import random
# taringud = int(input("Sisesta täringute arv: "))
# for i in range(taringud):
#     print(random.randint(1,6))



# # 2.5 ÕUNAD
# # Lumivalgekesel oli 14 õuna ja ta tahtis neid pöialpoistega jagada. Ta sai aru, et kui kõik seitse pöialpoissi 
# # tahavad õunu ja ta annaks kõigile kaks õuna, jääks ta ise üldse ilma. Nüüd otsustas ta õunu jagada nii, et küsib, 
# # mitu pöialpoissi tahab õunu, ja seejärel loosib iga soovija korral, kas anda talle üks või kaks õuna. Koostada 
# # programm, mis küsib kasutajalt, mitu pöialpoissi tahab õunu (võib eeldada, et sisestatakse täisarv lõigust [0; 7]);
# # leiab ja väljastab eraldi ridadele, mitu õuna saab iga pöialpoiss (programm genereerib iga kord juhuslikult arvu 1 või 2);
# # leiab ja väljastab eraldi reale, mitu õuna jääb Lumivalgekesele.

# import random
# ounad = 14
# pp = int(input("Mitu PP tahab õunu: "))
# for i in range(pp):
#     suv_oun = random.randint(1,2)
#     print(suv_oun)
#     ounad -= suv_oun
# print(f"Lumivalgukesele jäi {ounad} õuna.")



# 3.1 Ülikooli vastuvõetud
# Ülikooli I õppeastmesse (bakalaureuseõpe jm) võetakse igal aastal vastu sadu inimesi. Viimastel aastatel vastuvõetud 
# inimeste arvud on aastate kaupa failis rebased.txt, kus esimesel real on 2011. aastal vastuvõetute arv, 
# teisel real 2012. aastal vastuvõetute arv kuni viimasel real on 2019. aastal vastuvõetute arv. 
# Koostada programm, mis
# loeb failist registreeritud vastuvõetute andmed aastate järgi järjendisse;
# Failist järjendisse saab lugeda järgmise programmijupi abil:

# fail = open("rebased.txt", encoding="UTF-8")

# vastuvõetud = []

# for rida in fail:
#     # print(rida, end="")
#      vastuvõetud.append(int(rida))

# fail.close()
# # aasta = 9
# # print(vastuvõetud[aasta-1])
# aasta = input("Lisa aasta 2011-2019: ")
# print(vastuvõetud[int(aasta[3])-1])


# # küsib kasutajalt aastat
# # võib eeldada, et sisestatakse täisarv, mis kuulub lõiku [2011; 2019].
# # väljastab, mitu inimest sel aastal vastu võeti.




# # 3.3 Failis konto.txt on kirjas ujukomaarvudena pangakonto tehingud 
# # (kus positiivsed arvud on sissetulekud ja negatiivsed arvud on väljaminekud). Iga arv on eraldi real. 
# # Tekstifaili kasutamiseks programmi sees peab fail asuma programmifailiga samas kaustas.
# # Koostada programm, mis
# # loeb failist nimega konto.txt andmed;
# # väljastab ekraanile kõik sissetulekud ehk failist leitud positiivsed arvud. 
# # Iga arv peab olema eraldi real ja positiivsete arvude omavaheline järjekord peab jääma samaks nagu failis. 

# fail = open ("konto.txt", encoding="UTF-8")

# for kirje in fail:
#     if float(kirje) > 0:
#         print(float(kirje), end="\n")


# fail.close()


# # 3.4 Jukebox
# # Ada tahab valida plaadiautomaadist laulu ja uurib, milliseid laule masin mängib. Muusikapalad on kirjas failis, 
# # kus iga laul on eraldi real.
# # Programmi testimiseks kasutatakse järgmisi faile, mida võite salvestada või koostada ise mõne tekstiredaktoriga 
# # (nt Notepad):
# # jukebox.txt
# # 80ndad.txt
# # eesti_muusika.txt 
# # edm.txt
# # Koostada programm, mis
# # küsib kasutajalt failinime (kasutaja sisestab failinime koos laiendiga, nt jukebox.txt);
# # loeb sisestatud nimega failist andmed;
# # näitab kõiki laule koos järjekorranumbritega (alates 1);
# # küsib kasutajalt, mitmendat laulu ta soovib (kasutaja sisestab alati täisarvu);
# # väljastab ekraanile vastavalt valitud arvule muusikapala
####EI toimi veel
# musa = "edm.txt"
# fail = open(musa, encoding="UTF-8")
# #näita kõiki lugusid
# nr = 1
# for pala in fail:
#     print(str(nr)+". "+pala, end="")
#     nr += 1
# # Kuva valitud lugu
# print()
# # valik = int(input("Vali lugu: "))
# while True:
#     # valik = print("Mängitakse "+str(valik)+". lugu: "+pala)
#     valik = int(input("Vali lugu: "))
#     if valik == fail:
#         print("Mängitakse "+str(valik)+". lugu: "+pala)
#         break
#     else:
#         print(input("Valitud lugu ei eksisteeri, valige uuesti: "))

# # print("Mängitakse "+str(valik)+". lugu: "+pala)


# fail.close()




