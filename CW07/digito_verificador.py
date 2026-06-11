rol = input("Introduce el rol (ej. 201012341): ")
rol_invertido = rol[::-1]
suma_total = 0
multiplicador = 2
for digito in rol_invertido:
    numero = int(digito)
    suma_total = suma_total + (numero * multiplicador)
    multiplicador = multiplicador + 1
    if multiplicador > 7:
        multiplicador = 2
resto = suma_total % 11
digito_verificador = 11 - resto
if digito_verificador == 11:
    digito_verificador = 0
elif digito_verificador == 10:
    digito_verificador = "K"
print("El rol con su dígito verificador es:", rol + "-" + str(digito_verificador))