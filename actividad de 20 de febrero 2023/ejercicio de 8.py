def codigo(mensaje):
    abecedario = {'a': 'm', 'b': 'u', 'c': 'r', 'd': 'c', 'e': 'i',
              'f': 'e', 'g': 'l', 'h': 'a', 'i': 'g', 'j': 'o',
              'k': 'p', 'l': 's', 'm': 'b', 'n': 't', 'o': 'x',
              'p': 'h', 'q': 'j', 'r': 'd', 's': 'k', 't': 'y',
              'u': 'f', 'v': 'z', 'w': 'v', 'x': 'n', 'y': 'q', 'z': 'w'}
    mensajedecifrado = ''
    for letra in mensaje:
        if letra.lower() in abecedario:
            mensajedecifrado += abecedario[letra.lower()]
        else:
            mensajedecifrado += letra
    print('El mensaje cifrado es:', mensajedecifrado)

mensaje = input('Introduce el mensaje a cifrar: ')
print(codigo(mensaje))

