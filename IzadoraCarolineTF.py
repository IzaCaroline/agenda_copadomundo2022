#IZADORA CAROLINE - TRABALHO FINAL - ALGORITMOS II
#pesquisa a partir de uma palavra chave, a informação em um dos arquivos de texto: equipes ou jogos!
def search_keyword():
    opc = int(input('insira [1] para equipes, [2] para jogos: '))
    #opção 1 para busca no arquivo de equipes!
    if opc == 1:
        print('[1] para equipes')
        arquivo = open("equipes.txt", "r", encoding = "utf-8")
        arquivo1 = open("jogos.txt", "r", encoding = "utf-8")
        palavrachave = input('insira uma palavra chave para ir em busca de equipes registradas: ').upper()
        aux = 0
        for linha in arquivo:
            if palavrachave in linha:
                print(linha)
                aux+=1
        for linha in arquivo1:
            if palavrachave not in linha and aux == 0:
                print(f'sem registro para {palavrachave}!')
                break
        arquivo.close()
        arquivo1.close()
        print('⚠️  retornando ao menu! ⚠️')
        menu()
    #opção 1 para busca no arquivo de equipes!
    elif opc == 2:
        print('[2] para jogos')
        arquivo = open("jogos.txt", "r", encoding = "utf-8")
        arquivo1 = open("jogos.txt", "r", encoding = "utf-8")
        palavrachave = input('👉 Insira uma palavra chave para ir em busca de jogos registrados: ').upper()
        aux = 0
        for linha in arquivo:
            if palavrachave in linha:
                print(linha)
                aux+=1
        for linha in arquivo1:
            if palavrachave not in linha and aux == 0:
                print(f'sem registro para {palavrachave}!')
                break
        arquivo.close()
        arquivo1.close()
        print('⚠️  retornando ao menu! ⚠️')
        menu()
    #opção de número inválido para a escolha dos arquivos
    else:
        print('⚠️  opção inválida, retornando ao menu! ⚠️')
        menu()

#lista todos os jogos e suas informações
def list_all_games_and_teams():
    arquivo = open("jogos.txt", "r", encoding = "utf-8")
    for linha in arquivo:
        print(linha)
    all_games()

#Função de somar a quantidade de jogos registrados no Banco de Dados!
def all_games():
    arquivo = open("jogos.txt","r", encoding="utf8") 
    count = 0
    conteudo = arquivo.readlines() 
    for i in conteudo:  
            count += 1

    count = count - 1
    print(f"Possui {count} jogos registrados no Banco de Dados!")
    arquivo.close()
    print("⚠️  Retornando ao menu ⚠️")
    menu()

#Função de somar a quantidade de equipes registradas no Banco de Dados!
def all_teams():
    arquivo = open("equipes.txt","r", encoding="utf8") 
    count = 0
    conteudo = arquivo.readlines() 
    for i in conteudo:  
            count += 1

    count = count - 1
    print(f"Possui {count} equipes registrados no Banco de Dados!")
    arquivo.close() 
    print("⚠️  Retornando ao menu ⚠️")
    menu()

#Função que recebe do usuário as informações de acordo com o jogo realizado através de variáveis, 
#verifica se já existe registro e depois escreve-as no arquivo caso não exista registro!
#Ao final chama a função new_all_games_of_readlines!
def new_game_of_write():
    equipe1 = (input('👉 Insira aqui o nome da 1ª Equipe: ')).upper()
    equipe2 = (input('👉 Insira aqui o nome da 2ª Equipe: ')).upper()
    gols1 = (int(input(f'👉 Insira aqui a quantidade de gols da {equipe1}: ')))
    gols2 = (int(input(f'👉 Insira aqui a quantidade de gols da {equipe2}: ')))
    faltas1 = (int(input(f'👉 Insira aqui a quantidade de faltas da {equipe1}: ')))
    faltas2 = (int(input(f'👉 Insira aqui a quantidade de faltas da {equipe2}: ')))
    descrição = input('Tipo de jogo? por exemplo fases de grupo, oitavas de final, etc...: ')
    aux = 0
    aux1 = 0
    with open("equipes.txt", "r", encoding = "utf-8") as leitura:
        for linha in leitura.readlines():
            if equipe1 in linha:
                aux += 1
            if equipe2 in linha:
                aux1 += 1
        leitura.close()

    if aux == 0 or aux1 == 0:
        print(f"⚠️ Uma das equipes não consta no registro de equipes!!\nRegistre-a primeiro através do menu na opção [2] Nova Equipe! ⚠️")
        menu()

    if aux == 1 and aux1 == 1:
        with open("jogos.txt", "a", encoding = "utf-8") as escrita:
            escrita.write(f"\nJogo: {equipe1} VS {equipe2}, Placar: {gols1} X {gols2}, Faltas: {faltas1} VS {faltas2}, Tipo de Jogo: {descrição}")
            print('✅ Jogo registrado com sucesso!! ✅')
        escrita.close()
    new_all_games_of_readlines()
    

#Função que lê as informações existentes do arquivo, e questiona o usuário se ele deseja adicionar novas informações
#ou se desejas encerrar essa opção assim retornando ao Menu!
def new_all_games_of_readlines():
    arquivo = open("jogos.txt", "r", encoding="utf8")
    for linha in arquivo.readlines():
        print(linha)
    arquivo.close()
    
    adicionar = int(input("Gostaria de adicionar dados de um novo jogo? \n[1] SIM \n[_]Para NÃO, pressione qualquer tecla númerica\n 👉 somente número da opção: "))
    if adicionar == 1:
        new_game_of_write()
    else:
        print ('⚠️  Retornando ao menu! ⚠️')
        menu()

#Função que lê as informações existentes do arquivo, e questiona o usuário se ele deseja adicionar novas informações
#ou se desejas encerrar essa opção assim retornando ao Menu!
def new_team_of_readlines():
    arquivo = open("equipes.txt", "r", encoding="utf8")
    for linha in arquivo.readlines():
        print(linha)
    arquivo.close()
    
    adicionar = int(input("Gostaria de adicionar nova equipe? \n [1] SIM \n [_]Para NÃO, pressione qualquer tecla númerica\n 👉 Insira aqui somente o número da opção: "))
    if adicionar == 1:
        new_team_of_write()
    else:
        print ('⚠️  Retornando ao menu! ⚠️')
        menu()

#Função que recebe as informações da equipe, através de variáveis, verifica se já existe e depois escreve-as no
#arquivo caso não existe registro!
#Ao final chama a função new_team_of_readlines()
def new_team_of_write():
    equipe = (input('👉 Insira aqui o nome da Equipe: ')).upper()
    sigla = (input('👉 Insira aqui a sigla da Equipe: ')).upper()
    grupo = (input('👉 Insira aqui o grupo da Equipe: ')).upper()
    arquivo = open("equipes.txt", "r", encoding="utf-8")
    aux = 0
    for linha in arquivo:
        if equipe in linha:
            print('⚠️  A equipe já existe! Tente Novamente! ⚠️')
            aux += 1   
         
    if aux == 0:
        with open("equipes.txt", "a", encoding = "utf-8") as escrita:
            escrita.write(f'\n{equipe}, {sigla}, {grupo}')
            print('✅ Equipe registrada com sucesso!! ✅')
        escrita.close()
    
    arquivo.close()
    new_team_of_readlines()
  
#DEFINIÇÃO DO MENU
def menu():
    print('''
    ~~~~~~~~~~~ 🔰 BEM VINDO(A) A COPA DO MUNDO 2022 🔰 ~~~~~~~~~~~
                    ESTE É O MENU DE INFORMAÇÕES                 
    § ❌ [1] Sair do Menu                                        §
    § 🆕 [2] Nova Equipe                                         §
    § 🆕 [3] Novo Jogo                                           §
    § ⚽ [4] Quantidade de Jogos Registrados                     §
    § 🏳️  [5] Quantidade de Equipes Registradas                   §
    § ⚽ [6] Listar Todos os Jogos Com Suas Respectivas Equipes  §
    § 🔎 [7] Pesquisa por palavra chave                          §
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')
    opc = int(input('👉 Insira aqui somente o número da opção desejada: '))
#VALIDAÇÃO DAS OPÇÕES DO MENU E CHAMA A FUNÇÃO DE ACORDO COM A MESMA
    if opc == 1:
        print ('🤩 ENCERRO AQUI O MENU DE INFORMAÇÕES, DESEJO-LHE UMA 🤩\n   🤩 BOA COPA DO MUNDO 2022 E UMA ÓTIMA TORCIDA 🤩 ')
    elif opc == 2:
        print ('🆕 [2] Nova Equipe! Segue abaixo todas as equipes já registradas\n(caso não tenha nenhuma informação estará vazio): ')
        new_team_of_readlines()
    elif opc == 3:
        print ('🆕 [3] Novo Jogo! Segue abaixo todas os jogos já realizados\n(caso não tenha nenhuma informação estará vazio): ')
        new_all_games_of_readlines()
    elif opc == 4:
        print ('⚽ [4] Quantidade de jogos registrados!')
        all_games()
    elif opc == 5:
        print ('🏳️  [5] Quantidade de equipes registradas!')
        all_teams()
    elif opc == 6:
        print ('⚽ [6] Listar Todos os Jogos Com Suas Respectivas Equipes')
        list_all_games_and_teams()
    elif opc == 7:
        print ('🔎 [7] Pesquisa por palavra chave')
        search_keyword()
    else:
        print ('⚠️ Essa opção não é válida! Tente Novamente ⚠️')
        menu()

#INICIALIZAÇÃO DO MENU
menu()