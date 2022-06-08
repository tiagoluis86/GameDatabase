from functions import valida_int, existeArquivo, listarArquivo, cadastrarGame, criaArquivo

#programa principal

arquivo = 'notas.txt'

if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)

while True:
    print('Cadastro de Games \n')
    print('MENU \n')
    print('1 - Cadastrar game 2 - Consultar games 3 - Sair')

    op = valida_int('O que você deseja fazer? ', 1, 3)

    if op == 1:
        print('Cadastrar Game \n')
        nomeGame = input('Nome do game: ')
        try:
		notaGame = float(input('Nota do game (0.0 à 10): '))
		cadastrarGame(arquivo, nomeGame, notaGame)
		print("Game {} cadastrado com a nota {} \n".format(nomeGame, notaGame))
	except:
		print("Dados inválidos. Verifique se digitou no formato número.número corretamente")	
    elif op == 2:
        print('Listar itens \n')
        listarArquivo(arquivo)

    elif op == 3:
        print('Encerrando o programa...')
        break


