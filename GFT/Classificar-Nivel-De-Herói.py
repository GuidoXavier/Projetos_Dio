nome = input("Qual o nome do herói?")
xp = int(input("Quanto de experiência ele tem?"))

if(xp <= 1000):
    xp = "ferro"
elif(xp <= 2000):
    xp = "bronze"
elif(xp <= 5000):
    xp = "prata"
elif(xp <= 7000):
    xp = "ouro"
elif(xp <= 8000):
    xp = "platina"
elif(xp <= 9000):
    xp = "ascendente"
elif(xp <= 10000):
    xp = "imortal"
elif(xp >= 10001):
    xp = "radiante"
 

print(f"O herói {nome} está no nivel de {xp}")