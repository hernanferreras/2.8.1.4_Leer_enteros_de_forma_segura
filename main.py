def read_int(prompt, min, max):
    #
    # Escribe tu código aquí.
    #
    
    try:
        a = int(input(prompt))
        assert (a >= min and a <= max)
        return a
        
    except AssertionError:
        print("Error: el valor no está dentro del rango permitido ("+str(min)+".."+str(max)+")")
        read_int(prompt, min, max)
    
    except ValueError:
        print("Error: entrada incorrecta")
        read_int(prompt, min, max)
        
v = read_int("Ingresa un numero entre -10 a 10: ", -10, 10)

print("El número es:", v)
