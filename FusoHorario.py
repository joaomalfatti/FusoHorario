import os

def exibir_menu():
    os.system("cls")
    print("\n" + "="*50)
    print("=== Alterar Fuso Horário - v2.0 ===")
    print("="*50)
    print("\n--- Alterar Fuso Horário no Windows ---")
    print(" 1. (UTC-04:00) Manaus")
    print(" 2. (UTC-05:00) Rio Branco")
    return input("\n Escolha um fuso (1-2) ou pressione Enter para sair: ")

def alterar_fuso(opcao):
    fusos = {
        "1": {
            "nome": "SA Western Standard Time",
            "cidade": "Manaus",
        },
        "2": {
            "nome": "SA Pacific Standard Time",
            "cidade": "Rio Branco",
        }         
    }

    if opcao not in fusos:
        print("Opção inválida!")
        return False
    
    try:
        os.system(f'tzutil /s "{fusos[opcao]["nome"]}"')
        print(f" Fuso alterado para: {fusos[opcao]["cidade"]}")
        return True
    except Exception as error:
         print(f" Erro alterar fuso: {error}")
         return False


def main():
    os.system("cls")
    opcao = exibir_menu()
    if opcao:  
        alterar_fuso(opcao)
    print(" Saindo...")

if __name__ == "__main__":
    main()


""" Version: 2.0.0
Creator: João Malfatti """