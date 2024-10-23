menu = """

[d]
[s]
[e]
[q]

 ==> """

saldo = 0;  
limite = 500;   
extrato = ""
numero_saques = 0;  
LIMITE_SAQUES = 3;  

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = int(input("Qual o valor? "))
        if deposito > 0:
            saldo += deposito
            print("Saldo atual: ",saldo)
        else:
            print("Valor invalido!!")
    
    if opcao == "s":
        if numero_saques <= LIMITE_SAQUES:
            sacar = input ("qual valor sacar? ")
            s = saldo - sacar
            numero_saques += 1  
        else:
            print("Você já ultilizou o limite diário.")


            
            
        print(numero_saques)
        

    if opcao == "e":
        print("Extrato")
    
    if opcao == "q":
        break   

else:
    print("Op inválida, selecione a op desejada: ")


# https://github.com/digitalinnovationone/trilha-python-dio/blob/main/01%20-%20Estrutura%20de%20dados/desafio.py
# repositório c resolução.