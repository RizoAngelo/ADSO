def fecha(dias):
    if dias < 31:
        return ("enero")
    elif dias < 59:
        return ("febrero")
    elif dias < 90:
        return ("marzo")
    elif dias < 120:
        return ("abril")
    elif dias < 151:
        return ("mayo")
    elif dias < 181:
        return ("junio")
    elif dias < 212:
        return ("julio")
    elif dias < 243:
        return ("agosto")
    elif dias < 273:
        return ("septiembre")
    elif dias < 304:
        return ("octubre")
    elif dias < 334:
        return ("noviembre")
    elif dias < 365:
        return ("diciembre")
dias = int(input("digite cuantos dias "))
print(fecha(dias))