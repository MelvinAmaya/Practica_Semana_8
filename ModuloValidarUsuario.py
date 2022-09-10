# Melvin Josué Pereira Amaya SMIS010221
# Melvin Adiel Vasquez Mejia SMIS001021


def usuario(nombre):
    
    if len(nombre) < 6:
        print("\033[1;31m"+"> El nombre de usuario no puede ser menor a 6 caracteres. "+'\033[0;m')
    elif len(nombre) > 12:
        print("\033[1;31m"+"> El nombre de usuario no puede ser mayor a 12 caracteres. "+'\033[0;m')
    elif nombre.isalnum() == False:
        print("\033[1;31m"+"> El nombre de usuario debe ser Alfanumerico. "+'\033[0;m')
    else:
        print("\033[1;32m"+"> El nombre de usuario es valido. "+'\033[0;m') 


def InicioUsuario(nombre):
    
    if len(nombre) < 6:
        resultado = False
    elif len(nombre) > 12:
        resultado = False
    elif nombre.isalnum() == False:
        resultado = False
    else:
        resultado = True

    return resultado

