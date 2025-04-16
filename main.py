from apostas.core import Aposta, ControleApostas

def main():
    controle = ControleApostas()
    
    while True:
        print("\nMenu:")
        print("1. Adicionar Aposta")
        print("2. Ver Resumo")
        print("3. Ver Histórico")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            try:
                data = input("Data (DD/MM/AAAA): ")
                descricao = input("Descrição: ")
                valor = float(input("Valor Apostado: R$ "))
                odd = float(input("Odd: "))
                resultado = input("Resultado (ganhou/perdeu): ").lower()
                
                nova_aposta = Aposta(
                    data=data,
                    descricao=descricao,
                    valor_apostado=valor,
                    odd=odd,
                    resultado=resultado
                )
                controle.adicionar_aposta(nova_aposta)
                print("\nAposta registrada com sucesso!")
            except ValueError:
                print("Erro: Valores numéricos inválidos!")
        
        elif opcao == '2':
            print(controle.resumo())
        
        elif opcao == '3':
            print(controle.historico())
        
        elif opcao == '4':
            print("Encerrando o sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()