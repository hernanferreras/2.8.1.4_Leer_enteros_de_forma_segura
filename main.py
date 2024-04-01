def read_int(prompt, min, max):
    #
    # Escribe tu código aquí.
    #
    a = int(input(prompt))
    try:
        assert (a >= min and a <= max)
        return a
    except AssertionError:
        print("Error: el valor no está dentro del rango permitido ("+str(min)+".."+str(max)+")")
        

v = read_int("Ingresa un numero entre -10 a 10: ", -10, 10)

print("El número es:", v)
