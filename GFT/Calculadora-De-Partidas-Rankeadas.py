def calcula():
 vitorias = int(input("Quantas partidas você venceu?"))
 derrotas = int(input("Quantas partidas você perdeu?"))
 return vitorias - derrotas

rank = int(calcula())
nivel = ''

if(rank <=10):
 nivel = "ferro"
elif(rank <=20):
 nivel = "bronze"
elif(rank <=50):
 nivel = "prata"
elif(rank <=80):
 nivel = "ouro"
elif(rank <=90):
 nivel = "diamante"
elif(rank <=100):
 nivel = "lendário"
elif(rank >=101):
 nivel = "imortal"


print(f"O herói tem um saldo de vitórias de {rank} e está no nível {nivel}")

