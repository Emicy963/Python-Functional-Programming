from controller import gerarsenhas

def main():
    while True:
        caracteres = {
            "maiúsculas": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "minúsculas": "abcdefghijklmnopqrstuvwxyz",
            "números": "1234567890",
            "especiais": "!@#$^/*()_+-[]{}|;:,.<>?"
        }
        print('='*20)
        print('Gerador de Senhas!')
        print('='*20)

        criterios = list()
        m = input('Adicionar letras maísculas: (y/n)')
        if m == 'y':
            criterios.append("maiúsculas")
        n = input('Adicionar letras minúsculas: (y/n)')
        if n == 'y':
            criterios.append("minúsculas")
        num = input('Adicionar números: (y/n)')
        if num == 'y':
            criterios.append("números")               
        especiais = input('Adicionar caracteres especiais: (y/n)')
        if especiais == 'y':
            criterios.append("especiais")

        comprimento = int(input('Escolha um tamanho para senha (>6): '))
        qtd_senhas = int(input("Quantas senhas quer gerar: "))
        try:
            senha = [gerarsenhas(comprimento, caracteres, criterios) for _ in range(1, qtd_senhas+1)]
            print('Senhas geradas com sucesso!')
            print("Senhas:")
            for i, s in enumerate(senha, start=1):
                print(f"{i} - {s}")
            break
        except Exception as e:
            print(f'Falha a gerar uma senha: {e}')

if __name__ == '__main__':
    main()
        