try:
    blog_posts = [{'Photos': 3, 'Megusta': 21, 'comentarios': 2}, {'Megusta': 13, 'comentarios': 2, 'compartido': 1}, {'Photos': 5, 'Megusta': 33, 'comentarios': 8, 'compartido': 3}, {'comentarios': 4, 'compartido': 2}, {'Photos': 8, 'comentarios': 1, 'compartido': 1}, {'Photos': 3, 'Megusta': 19, 'comentarios': 3}]

    total_Megusta = 0

    for post in blog_posts:
        total_Megusta = total_Megusta + post['Megusta']

except ValueError:
    print("Error a buscar en la lista")
except KeyError:
    print("Error en el programa :)")
except:
    print("Por favor arregle el error del programa")
