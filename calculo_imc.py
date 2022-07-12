#Calcular o IMC 

#Função para o Usuário inserir seus respectivos dados e após isso calcular o IMC do mesmo.
def User_Dados():
    global imc_user
    while True: #Tratamento para não erro.
        try:
            user_insert_peso = float(input("Digite seu peso em KG: "))
        except ValueError:
            print('Digite apenas números.')
            continue
        else:
            break
    while True:
        try:
            user_insert_altura = float(input("Digite sua altura em METROS: "))
        except ValueError:
            print("Digite apenas números.")
            continue
        else:
            break
    imc = round(user_insert_peso / (user_insert_altura**2),2)
    imc_user = imc

#Função para analisar qual categoria o USUÁRIO pertence de acordo com seu IMC.
def Classificacao_IMC():
    if imc_user < 18.5:
        print(f'De acordo com seu IMC:{imc_user} você está na CATEGORIA: ABAIXO DO PESO.')
    elif imc_user >= 18.5 and imc_user <= 24.9:
        print(f'De acordo com seu IMC:{imc_user} você está na CATEGORIA: PESO NORMAL.')
    elif imc_user >= 25 and imc_user <= 29.9:
        print(f'De acordo com seu IMC:{imc_user} você está na CATEGORIA: SOBREPESO.')
    elif imc_user >= 30 and imc_user <= 34.9:
        print(f'De acordo com seu IMC:{imc_user} você está na CATEGORIA: OBESIDADE GRAU 1.')
    elif imc_user >= 35 and imc_user <= 39.9:
        print(f'De acordo com seu IMC:{imc_user} você está na CATEGORIA: OBESIDADE GRAU 2. ')
    elif imc_user >= 40:
        print(f'De acordo com seu IMC:{imc_user} você está na CATEGORIA: OBESIDADE MÓRBIDA.')

#Função para UNIR AS 2 funções
def Funcionamento_PROG():
    from time import sleep
    import os
    while True:
        User_Dados()
        Classificacao_IMC()
        while True:
            try:
                user_answer = int(input("""DESEJA CALCULAR OUTRO IMC?
                [1] SIM
                [2] NÃO
                Digite sua escolha: """))
            except ValueError:
                print('Digite SIM ou NÂO.')
                continue
            except IndexError:
                print("Digite SIM ou NÂO.")
                continue
            else:
                break
        if user_answer == 1:
            continue
        elif user_answer == 2:
            print("SAINDO....")
            sleep(1)
            break
            
