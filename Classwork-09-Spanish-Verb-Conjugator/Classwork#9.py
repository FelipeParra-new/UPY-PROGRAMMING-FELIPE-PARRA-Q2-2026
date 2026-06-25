#Estructuras requeridas
pronombres = ["Yo", "Tu", "El", "Nosotros" , "Vosotros","Ellos"]

endings ={
    "ar": ["o", "as", "a", "amos", "ais", "an"],
    "er": ["o", "es", "e", "emos", "eis", "en"],
    "ir": ["o", "es", "e", "imos", "is", "en"],
}
verb=input("Ingrese el verbo en español: ")
stem= verb[:-2] #Para obtener la raiz de la palabra
ending=verb[-2:] #Para obtener el final de la palabra
conjugations= endings[ending]
for index, pronombres in enumerate (pronombres):
    termination=conjugations[index]
    print(f"{pronombres} {stem}{termination}")