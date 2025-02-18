import random

def gerarsenhas(caracteres: dict, comprimento: int, criterios: list) -> str:
    ...


caracteres = {
        "maiúsculas": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "minúsculas": "abcdefghijklmnopqrstuvwxyz",
        "números": "1234567890",
        "especiais": "!@#$^/*()_+-[]{}|;:,.<>?"
    }

senha = lambda: random.randint(1, 10)

senhas = [str(senha()) for _ in range(4)] 
for _ in range(4):
    senhas += str(senha())

print(senhas)
s = ''.join(senhas)
print(s)    
#print(random.shuffle(senhas))
