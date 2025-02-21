import random

def gerarsenhas(comprimento: int, caracteres: dict, criterios: list) -> str:

    senha = []
    for criterio in criterios:
        create_caracteres = lambda: random.choice(caracteres[criterio])
        senha += list(create_caracteres())

    caracteres_possiveis = ""
    for criterio in criterios:
        caracteres_possiveis += random.choice(caracteres[criterio])
    
    senha += [random.choice(caracteres_possiveis) for _ in range(comprimento - len(senha))]

    random.shuffle(senha)

    return "".join(senha)
