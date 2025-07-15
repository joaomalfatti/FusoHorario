import os

def mostrar_menu():
    os.system("cls")
    print("\n" + "="*50)
    print("=== Fuso Horário - v3.0 ===")
    print("="*50)
    print("\n Menu de Fusos Horários")
    print("="*30)
    print("1. Manaus (UTC-04:00)")
    print("2. Rio Branco (UTC-05:00)")
    print("\n")

def alterar_fuso(opcao):
    fusos = {
        "1": {"nome": "SA Western Standard Time", "cidade": "Manaus"},
        "2": {"nome": "SA Pacific Standard Time", "cidade": "Rio Branco"}
    }
    
    if opcao in fusos:
        os.system(f'tzutil /s "{fusos[opcao]["nome"]}"')
        print(f"\nPronto! Fuso horário alterado para {fusos[opcao]["cidade"]}.\n")
        return True
    
    print("\nOpção não reconhecida. Por favor, tente novamente.\n")
    return False

def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha o fuso horário (1-2) ou 'S' para sair: ").upper()
            
        if alterar_fuso(escolha):
            continuar = input("Deseja alterar outro fuso? (S/N): ").upper()
            if continuar != 'S':
                print("\n" + "="*50)
                print("=== Encerrando o programa ===")
                print("="*50)
                break

if __name__ == "__main__":
    main()


'''
Version: 3.0.0
Creator: João Malfatti
'''