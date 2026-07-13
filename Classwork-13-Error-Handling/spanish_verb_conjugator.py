# Listas y diccionarios con las estructuras requeridas para conjugar
pronombres = ["Yo", "Tú", "Él", "Nosotros" , "Vosotros", "Ellos"]

endings = {
    "ar": ["o", "as", "a", "amos", "ais", "an"],
    "er": ["o", "es", "e", "emos", "eis", "en"],
    "ir": ["o", "es", "e", "imos", "is", "en"],
}

verb = input("Ingrese el verbo en español: ")

# Valido que la entrada del usuario no contenga espacios accidentales al inicio o al final
if verb != verb.strip():
    print("El verbo no debe tener espacios extra")
    
# Reviso que toda la entrada esté en minúsculas para evitar problemas con las llaves del diccionario
elif verb != verb.lower():
    print("El verbo debe escribirse en minúsculas")
    
# Verifico que la cadena sea lo suficientemente larga para tener una terminación válida
elif len(verb) < 2:
    print("El verbo debe terminar en ar, er o ir")
    
else:
    stem = verb[:-2] # Separo la raíz de la palabra cortando las últimas dos letras
    ending = verb[-2:] # Extraigo solo las últimas dos letras para identificar la terminación
    
    try:
        # Busco la terminación del verbo dentro de mi diccionario
        conjugations = endings[ending]
        
        # Itero sobre los pronombres y uso el índice para emparejarlos con su conjugación correspondiente
        for index, pronombre in enumerate(pronombres):
            termination = conjugations[index]
            print(f"{pronombre} {stem}{termination}")
            
    except KeyError:
        # Atrapo la excepción por si el usuario ingresa una terminación que no existe en mi diccionario (ej. números o letras al azar)
        print("El verbo debe terminar en ar, er o ir")