class hero:
    nome = ''
    idade = 0
    tipo = ''

    def __init__ (self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar (self):
        ataque = ''
        if(self.tipo == "mago"):
         ataque = "usou magia"
        elif(self.tipo == "guerreiro"):
         ataque = "usou espada"
        elif(self.tipo == "monge"):
         ataque = "usou artes marciais"
        elif(self.tipo == "ninja"):
         ataque = "usou shurikens"
         
        print(f"O {self.tipo} atacou usando {ataque}")


heroi1 = hero("Guilherme", 21, "monge")
heroi1.atacar()
heroi2 = hero("Alice", 20, "mago")
heroi2.atacar()