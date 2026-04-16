altura = float(input("Digite sua altura(m): "))
peso = float(input("Digite seu peso(kg): "))

IMC = peso / altura**2

print(f"Seu IMC é de: {IMC:.2f}")