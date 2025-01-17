# Ülesanne 08
# Teosta ülesanded etteantud sõnastikuga:

# Kuva Rasmuse telefoninumber
# Lisa sõnastikku oma nimi ja telefoninumber
# Kustuta Kristi number
# Muuda Eva telefoninumbri väärtuseks 55555555
# Kuva kõik numbrid
# Lisa võimalus kasutajal otsida nime järgi telefoninumbreid. Lisa teade, kui otsitavat nime ei leitud.

telefonid={
'Mari': '5957503',
'Toomas': '5719979',
'Kertu': '5201750',
'Siim': '5580027',
'Piret': '5960799',
'Jaan': '5160415',
'Lea': '5760164',
'Mart': '5337951',
'Anni': '5004818',
'Tõnu': '5721873',
'Kai': '5811884',
'Rasmus': '5859489',
'Eva': '5039393',
'Oskar': '5635812',
'Liina': '5696114',
'Peeter': '5560756',
'Sandra': '5257415',
'Heiki': '5207248',
'Kristi': '5703338',
'Urmas': '5400549'
}
print(f"Rasmuse telefoninumber on: {telefonid['Rasmus']}") #Rasmuse telefoninumber
telefonid['Asso'] = '55555555' #lisab
telefonid.pop('Kristi') #kustutab
telefonid['Eva'] = '55555555' #muudab
print(telefonid) #kõik numbrid
print("-------------------")
for nimi in telefonid:
    print(telefonid[nimi], end=" ")
otsi = input("Sisesta otsitav nimi: ") #otsib nime järgi
if otsi in telefonid:
    print(f"{otsi} telefoninumber on: {telefonid[otsi]}")
else:
    print(f"Otsitavat nime {otsi} ei leitud")


