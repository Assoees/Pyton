# # Ülesanne 17
# # Asso Eesmae
# # Pangakonto – pangakonto.txt
# # Sinu ülesandeks on kirjutada Pythoni skript, mis loeb andmeid failist pangakonto.txt. Fail sisaldab eraldi ridadel 
# # pangatehingute summasid: positiivsed summad tähistavad sissetulekuid ja negatiivsed summad väljaminekuid. 
# # Skript peab arvutama ja väljastama:
# # kogu tehingute arvu
# # positiivsete tehingute arvu
# # positiivsete tehingute kogusumma
# # Tulemused tuleb väljastada konsooli

# teharv = 0
# teharv_pos = 0
# posarv_summa = 0

# with open("pangakonto.txt") as fail:
#     sisu=fail.readlines()
#     for number in sisu:
#         #print(float(number))
#         teharv+=1
#         if float(number) > 0:
#             teharv_pos+=1
#             posarv_summa+=float(number)
# print(f"Tehingute arv: {teharv}")
# print(f"Positiivsete tehingute arv: {teharv_pos}")
# print(f"Positiivsete arvude summa: {posarv_summa:.2f}")

#teine osa

mpalgad = 0

with open("palgad.txt") as fail:
    sisu=fail.readlines()
    for i in sisu:
        # print(i,end="")
        tykeldus = i.split(",")
        if tykeldus[3] =="Mees":
            mpalgad+=float(tykeldus[6])
print(f"Meeste palgad: {mpalgad:.2f}")