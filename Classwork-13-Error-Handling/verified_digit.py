class DigitoApocrifoError(Exception):
    pass
check= True
while check:
    try:
        rol =input("Escribe el rol: ")
        rol_sin_digito, digito= rol.split("-")
        check= False
    except ValueError:
        print("Rol no valido")

inverso=rol_sin_digito[::-1]
secuencia =[2,3,4,5,6,7]
suma=0
for index in range (len(inverso)):
    numero =int(inverso[index])
    suma +=  numero*secuencia[index%6]
resultado =suma %11
verificador = 11- resultado
try:
    if verificador != int(digito):
        raise DigitoApocrifoError ()
        pass
except DigitoApocrifoError as e:
    print("Digito verificador apocrifo")
print(f"{rol_sin_digito} - {verificador}")