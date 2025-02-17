from controller import aumento_do_salario, maiores_de_30_anos, media_salarial

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

if __name__ == '__main__':
    main()
