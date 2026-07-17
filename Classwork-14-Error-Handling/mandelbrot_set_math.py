config = {}
hubo_error = False

# CASOS 2 y 3: Atrapar FileNotFoundError si no existe el archivo y ValueError si le falta el "="
try:
    file = open("config.txt", "r")
    for line in file:
        line = line.strip()
        if not line:
            continue
            
        try:
            parameter, value = line.split("=")
            config[parameter] = float(value) if "." in value else int(value)
        except ValueError:
            print("Error: El archivo de configuración está mal formado.")
            hubo_error = True
            break
            
    if not hubo_error:
        file.close()
except FileNotFoundError:
    print("Error: No se encontró el archivo config.txt")
    hubo_error = True

# CASO 4: Atrapar KeyError si falta una de las llaves en el diccionario
if not hubo_error:
    try:
        width = config["ancho"]
        height = config["alto"]
        max_iter = config["max_iter"]
        real_min = config["real_min"]
        real_max = config["real_max"]
        imag_min = config["imag_min"]
        imag_max = config["imag_max"]
    except KeyError as e:
        print(f"Error: Falta el parámetro {e} en config.txt")
        hubo_error = True

# CASO 5: Atrapar TypeError si "ancho" o "alto" tienen decimales y rompen el range()
if not hubo_error:
    try:
        output = open("mandelbrot.csv", "w")
        output.write("row,column,iterations\n")

        for row in range(height):
            for column in range(width):
                real = real_min + (column / width) * (real_max - real_min)
                imag = imag_min + (row / height) * (imag_max - imag_min)
                c = complex(real, imag)
                
                z = 0 + 0j
                iterations = 0
                
                while (abs(z) <= 2) and (iterations < max_iter):
                    z = z * z + c
                    iterations += 1
                
                output.write(f"{row},{column},{iterations}\n")
                
        output.close()
    except TypeError:
        print("Error: 'ancho' y 'alto' deben ser números enteros.")
        hubo_error = True