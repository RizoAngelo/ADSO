def no(nota):
    if nota<=2:
        return"su calificacion es insuficiente "
    elif nota<=4:
         return"su calificacion es suficiente "
    elif nota<=6:
        return"su calificacion es biena "
    elif nota<=8:
        return "su calificacion es superior "
    elif nota<=10:
        return"su calificacion es exelente "
nota = int(input("su calificacion es "))
print(no(nota))