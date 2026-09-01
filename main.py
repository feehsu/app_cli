import sys

def main():
    # Se o usuário não passar os parâmetros na linha de comando, o script pede via terminal
    if len(sys.argv) > 1:
        param1 = sys.argv[1]
    else:
        param1 = input("DIGITE A ENTRADA 1: ")

    if len(sys.argv) > 2:
        param2 = sys.argv[2]
    else:
        param2 = input("DIGITE A ENTRADA 2: ")

    # Processamento e Saída
    print("\n----------------------------------")
    print(f"OLHA A SAÍDA Y: {param1.upper()} - {param2.upper()}")
    print("----------------------------------\n")

if __name__ == "__main__":
    main()
