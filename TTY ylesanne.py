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

import math
inim = 80
koht = 160
jaak = inim % koht

bussid_arv = math.ceil(inim / koht)
if jaak > 0:
    bussid_arv = (inim // koht) + 1
elif jaak == 0:
         bussid_arv = inim // koht
else:
    bussid_arv = inim // koht
print(f"Busside arv: {bussid_arv}")
print(f"Viimases bussis inimesi: {jaak}")