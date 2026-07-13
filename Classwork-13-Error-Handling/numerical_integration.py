import math

try:
    a = input("Write the left endpoint of the interval: ")
    try:
        if "pi" in a:
            a = eval(a.replace("pi", str(math.pi)))
        else:
            a = float(a)
    except Exception:
        raise ValueError("The lower limit must be numeric")

    b = input("Write the right endpoint of the interval: ")
    try:
        if "pi" in b:
            b = eval(b.replace("pi", str(math.pi)))
        else:
            b = float(b)
    except Exception:
        raise ValueError("The upper limit must be numeric")

    if a >= b:
        raise ValueError("The lower limit must be less than the upper limit")

    f_x = input("Write the function to integrate: ")
    if not f_x.strip():
        raise ValueError("The entered function is invalid")

    method = input("Select integration method (LRM/RRM/MPM/TM): ")
    
    if method not in ["LRM", "RRM", "MPM", "TM"]:
        raise ValueError("Invalid integration method. Use LRM, RRM, MPM, or TM")

    # PROCESS
    area = 0.0
    n = 1000
    h = (b - a) / n
    shift = 0
    constant = 0

    if method == "RRM":
        shift = 1
        
    if method == "MPM":
        constant = h / 2

    if method == "TM":
        shift = 1

    for i in range(0 + shift, n + shift):
        xi = a + i * h + constant
        
        x = xi
        try:
            height = eval(f_x)
        except NameError:
            raise ValueError("The function must be written in terms of x")
        except SyntaxError:
            raise ValueError("The entered function is invalid")
        except ZeroDivisionError:
            raise ValueError("The function is not defined at some point in the interval")
        except Exception:
            raise ValueError("The entered function is invalid")
            
        if method == "TM":
            area += 2 * height * h
        else:
            area += height * h
            
    if method == "TM":
        x = a
        fa = eval(f_x)
        x = b
        fb = eval(f_x)
        area = (area + (fa * h) + (fb * h)) / 2
        
    # OUTPUT
    print(f"The integration of {f_x} is {area:.3f}")

except ValueError as e:
    print(e)