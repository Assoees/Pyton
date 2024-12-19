#19.12.24
#Eesmae
#Ülesanne 07

nimi = ["Jyri","Martin","Andres","Juuli","Maali"]

# for i in nimi:
#     
#     print(i)
#     
for i in range(5):
        print(f"{i+1}. {nimi[i]}")
valik = int(input("Vali lugu (1-5): "))

print(f"Mängin: {nimi[valik-1]}")
