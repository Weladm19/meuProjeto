menu = """

    [d]-Depositar
    [s]-Sacar
    [e]-Extrato
    [q]-Sair
    
    
....:"""

saldo  = 0
limite = 500
extrato =  ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    op = input(menu).lower()
    match op:
        case 'd':
            valor  = float(input("Informe  o valor do deposito: "))
            if valor > 0:
                saldo += valor
                extrato += f'Deposito R${valor:.2f}\n'
            else:
                print("Operação falhou! o valor  informado é invalido")
        case 's':
            valor = float(input("Informe o valor do saque: "))
            execedeu_saldo  = valor  > saldo
            execedeu_limite = valor  > limite
            execedeu_saques = numero_saques >= LIMITE_SAQUES
            
            if execedeu_saldo:
                print("Operação falhou! Você  não tem saldo suficiente")
            
            elif execedeu_limite:
                print("Operação falhou! O valor  do do  saque excedeu o limite")
            
            elif execedeu_saques:
                print("Operação falhou! Numero  maximo de saques  excedido")
            
            elif valor  > 0:
                saldo -= valor 
                extrato += f'Saque: R${valor:.2f}'   
                numero_saques += 1
                
            else:
                print("Operação falhou! o vavlor informado é invalido")
                
        case 'e':
            print("------------------Extrato---------------------")
            print("Não foram realizados movimentações." if not extrato else extrato)
            print("\n Saldo: R${saldo:.2f}")
            print('----------------------------------------------')
        case 'q':
            break
        case _:
            print("Operação Invalidada, por favor selecione a opção correta")