import os

def exibir_menu():
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
            "nome": "SA Western Standard Time",
            "cidade": "Rio Branco",
        }         
    }
    
    if opcao in fusos:
        os.system(f'tzutil /s "{fusos[opcao]["nome"]}"')
        print(f" Fuso alterado para: {fusos[opcao]["cidade"]}")
    else:
        print(" Opção inválida!")

def main():
    os.system("cls")
    opcao = exibir_menu()
    if opcao:  
        alterar_fuso(opcao)
    print(" Saindo...")

if __name__ == "__main__":
    main()


""" Version: 1.0.0
Creator: João Malfatti """