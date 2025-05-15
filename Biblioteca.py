#Boas Vindas ao Usuário
print('|'+59*'-'+'|')
print('|-----Bem vindo a Livraria do Tiago Raimundo de Jesus-------|')
print('|'+59*'-'+'|')

#Lista base de livros 
lista_livro = []
#ID de livros cadastrados
id_global = 0

#Cadastro de Livro
def cadastrar_livro(id):
  #Menu de cadastro
  print('|-----------------------------|')
  print('|-----Cadastro de Livro-------|')
  print('|-----------------------------|')

  nome_livro = input('Informe o nome do livro: ')
  autor_livro = input('Informe o autor do livro: ')
  editora_livro = input('Informe o ano de lançamento do livro: ') 

  #Criando registro do livro no dicionário
  livro = {'ID'      : id,
           'NOME'    : nome_livro.upper(),
           'AUTOR'   : autor_livro.upper(),
           'EDITORA' : editora_livro.upper()}
  
  #Copiando registro criado para a lista
  lista_livro.append(livro.copy())
  return

#Consulta de Livro
def consultar_livro():
  while (True):
    try:
      #Menu de cadastro
      print('|-----------------------------|')
      print('|-----Consulta de Livros------|')
      print('|-----------------------------|')
      print('| Escolha a opção desejada: |')
      print('| 1 - Consultar Todos         |')
      print('| 2 - Consultar por Id        |')
      print('| 3 - Consultar por Autor     |')
      iMenuConsulta = int(input('| 4 - Retornar ao Menu        |'+'\n'))
      
      #Caso não for uma opção válida já bloqueia aqui
      if not (iMenuConsulta > 0 and iMenuConsulta <= 4):
        print('Opção inválida.'+'\n')
        continue
      else:
        #Consulta Todos os Livros
        if iMenuConsulta == 1:
          print('>>Todos os Livros<<')
          print(10*'-'+'Resultado'+10*'-')
          for livro in lista_livro:            
            print(f'ID:      {livro['ID']}')
            print(f'NOME:    {livro['NOME']}')
            print(f'AUTOR:   {livro['AUTOR']}')
            print(f'EDITORA: {livro['EDITORA']}')            
            print('-------------------------')                    
          print('\n')
          continue      
        #Consulta por ID
        elif iMenuConsulta == 2:
          print('>>Livros por ID<<')
          iIDInformado = int(input('Informe o ID do Livro: '+'\n'))          
          print(10*'-'+'Resultado'+10*'-')
          for livro in lista_livro:            
            if livro['ID'] == iIDInformado:              
              print(f'ID:      {livro['ID']}')
              print(f'NOME:    {livro['NOME']}')
              print(f'AUTOR:   {livro['AUTOR']}')
              print(f'EDITORA: {livro['EDITORA']}')
              print('-------------------------'+'\n')     
              continue
        #Consulta por Autor
        elif iMenuConsulta == 3:
          print('>>Livros por Autor<<')
          sAutorInformado = input('Informe o Autor do Livro: '+'\n')
          print(10*'-'+'Resultado'+10*'-')
          for livro in lista_livro:            
            if livro['AUTOR'] == sAutorInformado.upper():              
              print(f'ID:      {livro['ID']}')
              print(f'NOME:    {livro['NOME']}')
              print(f'AUTOR:   {livro['AUTOR']}')
              print(f'EDITORA: {livro['EDITORA']}')
              print('-------------------------'+'\n') 
              continue
        #Caso não for nenhuma das outras só pode ser 4
        else:
          break
    except ValueError:
      print('Opção inválida.'+'\n')
      continue

#Remover Livro
def remover_livro():
  while (True):
    print('>>Exclusão de Livro<<')
    iIDLivro = int(input('Informe o ID do Livro: '+'\n'))
    for livro in lista_livro:
      if livro['ID'] == iIDLivro:
        #Remove o Livro conforme ID informado
        lista_livro.remove(livro)
        print('Livro Removido com sucesso.')
        return
    print('Id Inválido!'+'\n')
    continue
  
#MENU Principal
while (True):  
  try:
    #Menu de cadastro
    print('\n')
    print('|-----------------------------|')
    print('|-------Menu Principal--------|')
    print('|-----------------------------|')
    print('| Escolha a opção desejada:   |')
    print('| 1 - Cadastra Livro          |')
    print('| 2 - Consulta Livro          |')
    print('| 3 - Remover Livro           |')
    iMenuPrincipal = int(input('| 4 - Sair                    |'+'\n'))
    print('\n')

    #Teste para opção Valida
    if not (iMenuPrincipal > 0 and iMenuPrincipal <= 4):
      print('Opção inválida.'+'\n')
      continue
    else:
      if iMenuPrincipal == 1:
        id_global += 1
        cadastrar_livro(id_global)
        continue      
      elif iMenuPrincipal == 2:
        consultar_livro()
        continue
      elif iMenuPrincipal == 3:
        remover_livro()
        continue
      else:
        print('FIM DO PROGRAMA!')
        break
  except ValueError:
      print('Opção inválida.'+'\n')
      continue