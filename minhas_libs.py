"""
Aqui iremos colocar nossos métodos próprios
"""

def ler_ficheiro(nome_do_ficheiro):
    """
    método para abrir um ficheiro txt em modo leitura e imprimir o conteúdo
    do ficheiro
    param: nome do ficheiro .txt
    """
    meu_ficheiro = open(nome_do_ficheiro, "r", encoding="utf-8")
    for line in meu_ficheiro:
        print(line.strip())
    meu_ficheiro.close()