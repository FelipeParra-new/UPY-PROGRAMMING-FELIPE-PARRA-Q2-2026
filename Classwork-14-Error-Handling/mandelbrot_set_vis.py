from PIL import Image

config = {}
hubo_error = False

# CASO 2: Manejo de error si no existe config.txt
try:
    file = open("config.txt", "r")
    lines = file.readlines()
    for line in lines:
        parameter, value = line.strip().split("=")
        config[parameter] = float(value) if "." in value else int(value)
    file.close()
    print(config)
except FileNotFoundError:
    print("Error: No se encontró el archivo config.txt")
    hubo_error = True

# Si el config.txt se leyó bien, intentamos con el csv
if not hubo_error:
    # CASO 3: Manejo de error si no existe mandelbrot.csv
    try:
        archivo = open("mandelbrot.csv", "r")
        lineas = archivo.readlines()
        archivo.close()
    except FileNotFoundError:
        print("Error: No se encontró el archivo mandelbrot.csv")
        hubo_error = True

# Si ambos archivos se leyeron bien, procesamos la imagen
if not hubo_error:
    # Evitar error si el archivo csv está vacío
    if len(lineas) > 0:
        lineas.pop(0)

    max_iter = config["max_iter"]
    ancho, alto = int(config["ancho"]), int(config["alto"])

    img = Image.new("HSV", (ancho, alto))

    for linea in lineas:
        # CASO 5: Fila de csv mal formada
        try:
            row, column, iterations = linea.strip().split(",")
            iterations = int(iterations)
            row = int(row)
            column = int(column)
        except ValueError:
            print("Error: El archivo mandelbrot.csv está mal formado (formato incorrecto en al menos una fila).")
            hubo_error = True
            break  # Detiene el ciclo for inmediatamente
        
        if iterations == max_iter:
            brillo = 0
        else:
            brillo = int((iterations / max_iter) * 255)
            
        # CASO 4: Coordenada fuera del tamaño de la imagen
        try:
            img.putpixel((column, row), (brillo, 255, 255))
        except IndexError:
            print("Error: El archivo csv no es consistente con el ancho y alto del config.txt (índice fuera de rango).")
            hubo_error = True
            break  # Detiene el ciclo for inmediatamente

# Si completamos todo sin activar la bandera de error, guardamos el PNG
if not hubo_error:
    img_rgb = img.convert("RGB")
    img_rgb.save("mandelbrot.png")
    print("DONE")