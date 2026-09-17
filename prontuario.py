# contador para, dentro do while e da função adicionarPac() sempre alterar o contador para +1, assim posso criar vários dicionários infinitamente.
contador = 0
pacientes = dict()
import shutil


# Função para adicionar paciente ao dicionário "pacientes"

def adicionarPac():
    global contador
    nome = input("Digite o nome do paciente: ")
    pa = input("Digite a Pressão do Paciente(aperte um espaço): ")
    pa = pa.replace(' ', 'x')
    bpm = input("Digite os Batimentos Cardíacos do Paciente: ")
    sat = input("Digite a saturação do Paciente: ")
    temp = input("Digite a temperatura do Paciente: ")
    palgrau = input("Digite o grau de Paliativo(1 a 3): ")
    sinaisV = {'PA': pa, 'BPM':bpm, "Temperatura":f'{temp}°C', 'Saturação':f'{sat}%'}
    pacientes[contador] = {
        "Nome": nome, "Sinais Vitais": sinaisV, "Grau de Paliativo":f'{palgrau}°'
    }   
    contador += 1      


# Função para atualizar dados dentro da função "Pacientes"

def atualizarPac():
    for chave, valor in pacientes.items():
        print(f'Valor ID:{chave}, Nome do Paciente: {valor['Nome']}')
    n = int(input("Digite o número de ID do paciente que você deseja alterar: "))
    
    # Loop while para não precisar acessar a opção de atualizarPAC() toda vez, podendo cancelar.

    while True:

        print('[1]Pressão')
        print('[2]Batimentos Cardíacos')
        print('[3]Saturação')
        print('[4]Temperatura')
        print('[5]Grau de Paliativo')
        print("[6]Cancelar")
        
        opcao = input("Digite a opção que deseja alterar: ")

        if opcao == "1":
            pa = input("Digite o novo valor para a Pressão(com um espaço no meio): ")
            pa = pa.replace(' ', 'x')
            pacientes[n]['Sinais Vitais']['PA'] = pa
            
        elif opcao == "2":
            bpm = input("Digite o novo valor para o Batimento Cardíaco: ")
            pacientes[n]['Sinais Vitais']['BPM'] = bpm
            
        elif opcao == "3":
            sat = input("Digite o novo valor para a Saturação: ")
            pacientes[n]["Sinais Vitais"]["Saturação"] = sat
            
        elif opcao == "4":
            temp = input("Digite o novo valor da Temperatura: ")
            pacientes[n]["Sinais Vitais"]["Temperatura"] = temp
            
        elif opcao == "5":
            palgrau = input("Digite o novo grau de paliativo(de 1 a 3): ")
            pacientes[n]["Grau de Paliativo"] = palgrau

        elif opcao == "6":
            print("Cancelando...")
            break
        else:
            print("Digite um número de 1 a 6!")
        

# Mostrar pacientes cadastrados no sistema.

def mostrarPac():
    for key, valor in pacientes.items():
        print(f'O paciente de código {key} é {valor['Nome']}')

# Mostra algum dado específico do paciente

def mostrarPacEspc():
    pac = int(input("Digite o código do paciente: "))
    print(f'O paciente {pacientes[(pac)]["Nome"]} possui o código {pac}')
    resposta = input("Deseja verificar algo específico do paciente?[S/N] ").upper()
    if resposta == "S":
        print('[1]Pressão')
        print('[2]Batimentos Cardíacos')
        print('[3]Saturação')
        print('[4]Temperatura')
        print('[5]Grau de Paliativo')
        print('[6]Cancelar')
        while True:
            nresposta = int(input("Digite a opção que deseja verificar: "))
            if nresposta == 1:
                print(f'A Pressão atual do paciente é de {pacientes[pac]["Sinais Vitais"]["PA"]}')
            elif nresposta == 2:
                print(f'A Frequência Cardíaca atual do paciente é de {pacientes[pac]["Sinais Vitais"]["BPM"]}')
            elif nresposta == 3:
                print(f'A Saturação atual do paciente é de {pacientes[pac]["Sinais Vitais"]["Saturação"]}')
            elif nresposta == 4:
                print(f'A Temperatura atual do paciente é de {pacientes[pac]["Sinais Vitais"]["Temperatura"]}')
            elif nresposta == 5:
                print(f'O Grau de paliativo atual do paciente é {pacientes[pac]["Grau de Paliativo"]}')
            elif nresposta == 6:
                print("Cancelando...")
                break
            else:
                print("Digite um valor de 1 a 5!")

# Fecha a aplicação.

def fecharPront():
    print("Encerrando sistema")
    

    # Comando com import que pesquisei na internet, "calibra" os tracejados (-) para serem compatíveis com a tela do terminal de quem executar.
tela = shutil.get_terminal_size().columns
print("=" * tela)
print('PRONTUÁRIO DO PACIENTE EM UTI'.center(tela))
print("=" * tela)


# Menu 

while True:
    print("Menu".center(tela))
    print("[1]Adicionar Paciente")
    print("[2]Atualizar Paciente")
    print("[3]Verificar Pacientes")
    print("[4]Verificar Sinais Vitais de paciente por código")
    print("[5]Fechar Prontuário")
    x= input("Digite a opção que quer interagir: ")
    if x in '12345':
        print("Carregando...")    
        if x == '1':
            adicionarPac()
        elif x == '2':
            atualizarPac()
        elif x == '3':
            mostrarPac()
            
        elif x == '4':
            mostrarPacEspc()
        else:
            fecharPront()
            break
    else:
        print("Apenas valores de 1 a 5 permitidos!")