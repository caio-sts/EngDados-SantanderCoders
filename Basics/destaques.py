# Operador divisão inteira

print(3 // 4)  # 0

# Atribuir à variável o que for recebido do teclado, 
# OBS: o armazenamento é feito em string, faça o casting se necessário

idade = input("Insira sua idade.")

# While para validar dados

senha = input("Digite sua senha")

while (senha != "LetsCode"):
  senha = input("Senha inválida. Tente novamente!")

print("Acesso permitido.")

# Uso da keyword continue, não será executado o que está na sequência

contador = 0

while (contador < 10):
  contador += 1
  if contador == 1:
    continue
  print(contador + "volta(s) no while.")

print("Fim da repetição")


