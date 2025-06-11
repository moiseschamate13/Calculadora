nome_usuario = input("Digite Seu nome:")
print(f"Seja bem-vindo, {nome_usuario}, à calculadora de expressões do primeiro grau.")
print("Esta calculadora realiza apenas equações possíveis e determinadas, ou seja, apenas quando o valor de a é diferente de 0.")

while True:

  opcao = input("Você deseja realizar alguma equação? S/N:")

  if opcao == "S":
    a = float(input("Digite o valor de a:"))
    b = float(input("Digite o valor de b:"))
    resultado = float(input("Digite o resultado da equação:"))
    x = (resultado - b) / a
    print(f"O valor de x é: {x}")

  elif opcao == "N":
    print("Obrigado por ultilizar nossa calculadora")
    break



