#Calcular o IMC 

#Função para o Usuário inserir seus respectivos dados e após isso calcular o IMC do mesmo.

def User_Dados():
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
    return imc_user

#Função para analisar qual categoria o USUÁRIO pertence de acordo com seu IMC.
def Classificacao_IMC(imc_user):
    match imc_user:
        case imc_user if imc_user <= 18.5:
            print(f'De acordo com seu IMC:{imc_user} você está na CATEGORIA: ABAIXO DO PESO.')

        case imc_user if imc_user >= 18.5:
            print(f'De acordo com seu IMC:{imc_user} você está na CATEGORIA: PESO NORMAL.')

        case  imc_user if imc_user >= 25.0:
            print(f'De acordo com seu IMC:{imc_user} você está na CATEGORIA: SOBREPESO.')

        case imc_user if imc_user >= 30.0:
            print(f'De acordo com seu IMC:{imc_user} você está na CATEGORIA: OBESIDADE GRAU 1.')
            
        case imc_user if imc_user >= 35.0:
            print(f'De acordo com seu IMC:{imc_user} você está na CATEGORIA: OBESIDADE GRAU 2. ')

        case imc_user if imc_user >= 40.0:
            print(f'De acordo com seu IMC:{imc_user} você está na CATEGORIA: OBESIDADE MÓRBIDA.')

#Função para UNIR AS 2 funções
def Funcionamento_PROG():
    from time import sleep
    while True:
        Classificacao_IMC(User_Dados())
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

        match user_answer:
            case 1:
                continue

            case 2:
                print("SAINDO....")
                sleep(1)
                break
                