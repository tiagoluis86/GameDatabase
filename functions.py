#funcoes
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

#verifica se o arquivo existe
def  existeArquivo(nomeArquivo):
    try:
       a = open(nomeArquivo, 'rt')
       a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Aconteceu um erro')
    else:
        print(a.read())
    finally:
        a.close()

def cadastrarAluno(nomeArquivo, nomeAluno, notaAluno):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{}; {}\n'.format(nomeAluno, notaAluno))
    finally:
        a.close()

#tenta criar o arquivo se necessário
def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} foi criado com sucesso! \n'.format(nomeArquivo))
