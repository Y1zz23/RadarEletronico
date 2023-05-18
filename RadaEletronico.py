v = int(input("Digite a velocidade do carro? "))
if v > 80:
    print("MULTADO! Voce excedeu o limite permitido que é de 80Km/h")
    multa = (v - 80) * 7
    print("Voce vai pagar R${} de multa".format(multa))
print("Tenha um bom dia! Dirija com segurança!")
