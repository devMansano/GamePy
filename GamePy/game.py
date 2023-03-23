from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)
    
def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]:'))
    
    calc: Calcular = Calcular(dificuldade)
    
    print('Informe o resultado da seguinte operação:')
    calc.mostrar_operacao()
    
    resultado: float = float(input())
    
    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')
        
    continuar: int = int(input( f'Deseja continuar no jogo  [1 - sim, 2 - não]'))
    
    
    if continuar == 1:
     jogar(pontos)
    elif continuar == 2:
     print(f'Você finalizou com {pontos} ponto(s).')
    else:
        print(f'Ação informada desconhecida')

if __name__ == '__main__':
    main()