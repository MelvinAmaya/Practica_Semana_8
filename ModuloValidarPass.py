# Melvin Josué Pereira Amaya SMIS010221
# Melvin Adiel Vasquez Mejia SMIS001021


def valicontra(contra):
    logcontra = len(contra)
    space = contra.isspace()
    if logcontra >= 8:
        for i in range(len(contra)):
            if contra[i] == " ":
                space = True
                break
            else:
                space = False
        if space == False:
            print("\033[1;32m"+"> Contrasenia valida. "+'\033[0;m')
        else:
            print("\033[1;31m"+"> La contrasenia elegida no es segura. "+'\033[0;m')    
    else:
        print("\033[1;31m"+"> Minimo 8 caracteres. "+'\033[0;m')

def InicioValicontra(contra):
    logcontra = len(contra)
    space = contra.isspace()
    if logcontra >= 8:
        for i in range(len(contra)):
            if contra[i] == " ":
                space = True
                break
            else:
                space = False
        if space == False:
            resutado = True
        else:
            resutado = False   
    else:
        resutado = False
    return resutado