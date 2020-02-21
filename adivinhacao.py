print("*****************")
print("Bem vindo ao jogo")
print("*****************")

numero_secreto = 42

chute_str = input("Digite seu numero: ")
chute = int(chute_str)
numero_de_tentativas = 3
rodada = 1

while(rodada <= numero_de_tentativas):
print("Tentativa {} de {}".format(rodada, numero_de_tentativas))
print("Você digitou", chute)
acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print("Voce acertou")
else:
    if(maior):
        print("Voce errou! Seu chute foi maior que o número secreto")
    elif (menor):
        print("Voce errou! Seu chute foi menor que o número secreto")
rodada = rodada + 1

#
# numero_secreto = 42
#
# chute_str = input("Digite seu numero: ")
# chute = int(chute_str)
# numero_de_tentativas = 3
# rodada = 1

# for rodada in range(1, total_de_tentativas + 1) :
# print("Tentativa {} de {}".format(rodada, numero_de_tentativas))
# print("Você digitou", chute)
# acertou = numero_secreto == chute
# maior = chute > numero_secreto
# menor = chute < numero_secreto
#
# if(acertou):
#     print("Voce acertou")
# else:
#     if(maior):
#         print("Voce errou! Seu chute foi maior que o número secreto")
#     elif (menor):
#         print("Voce errou! Seu chute foi menor que o número secreto")
# rodada = rodada + 1
#
#
