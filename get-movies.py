import requests
import json

#isto eh uma funcao  
def requisicao(titulo):
     #tratando erros com try except, ainda tenho que entender os mecanismos internos no VSCODE
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=a9b0d085&t=' + titulo)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print ("erro ao acessar o site")
        return None


def print_detalhes(filme):
    print ("Nome Filme:", filme['Title'])
    print ("Atores:", filme['Actors'])
    print ("Ano:", filme['Year'])
    print ("NotaImdb:", filme['imdbRating'])
    print ("")


sair = False
while not sair: 
    op = input("Escreva o nome de um filme ou SAIR para fechar: ")
    if op == 'SAIR':
        sair = True
    else:
        filme = requisicao(op)
        if filme['Response'] == "False":
            print ("Filme Nao encontrado")
        else:
            print_detalhes (filme)