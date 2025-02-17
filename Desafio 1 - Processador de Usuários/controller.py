from functools import reduce

def aumento_do_salario(usuarios: list) -> list:
    """ Pegando cada salário do dicionário e achando o seu 10% e armazenando em uma lista """
    salario_porcentagem_aumento = list(map(lambda salario: (salario['salario']*(0.1)), usuarios))

    """ Pegar cada elemento da tipo dicionário dentro da lista, na posição 'salario' e fazer 
        a soma dele com 10% de aumento, cada armazenado um em na lista acima criada cada um
        na sua respectiva posição """ 
    for i, user in enumerate(usuarios):
        user['salario'] += salario_porcentagem_aumento[i]
    return usuarios

def maiores_de_30_anos(usuarios: list) -> list:
    usuarios_mais_30 = list(filter(lambda idade: idade['idade'] > 30, usuarios))
    return usuarios_mais_30

def media_salarial(usuarios: list) -> int:
    salario = reduce(lambda acc, item: acc + item['salario'], usuarios, 0)
    return (salario/len(usuarios))

def main():
    usuarios = [
        {"nome": "Alice", "idade": 25, "salario": 3000},
        {"nome": "Bob", "idade": 35, "salario": 5000},
        {"nome": "Carlos", "idade": 40, "salario": 7000},
    ]
    print('Salários com aumentos de 10%: ')
    users = aumento_do_salario(usuarios)
    for user in users:
        print(user)
    print('='*50)

    print('Usuaários com mais de 30 anos:')
    maiores = maiores_de_30_anos(usuarios)
    for maior in maiores:
        print(maior)
    print('='*50)
    
    media_salario = media_salarial(usuarios)
    print(f'A média do salário dos usuários: {media_salario}')
