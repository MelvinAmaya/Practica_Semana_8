# Melvin Josué Pereira Amaya SMIS010221
# Melvin Adiel Vasquez Mejia SMIS001021


from queue import Empty
from ModuloValidarUsuario import usuario,InicioUsuario
from ModuloValidarPass import valicontra,InicioValicontra


usuarioo = Empty
passwordd = Empty
usu = Empty
passwor = Empty
ingresoUsu = False
ingresopass = False


while True:
    
    print("\033[1;33m"+"--------------------------------------------------------------"+'\033[0;m')
    print("\033[1;33m"+"--------------------------Bienvenid@--------------------------"+'\033[0;m') 
    print("\033[1;33m"+"-----------------------1. Registrarse-------------------------"+'\033[0;m') 
    print("\033[1;33m"+"-----------------------2. Iniciar sesion----------------------"+'\033[0;m') 
    print("\033[1;33m"+"-----------------------3. Salir-------------------------------"+'\033[0;m') 
    print("\033[1;33m"+"--------------------------------------------------------------"+'\033[0;m') 

    try:
        opcion = int(input("\033[1;36m"+"> Ingrese su opcion: "+'\033[0;m'))
        print("\033[1;33m"+"--------------------------------------------------------------"+'\033[0;m')
        if opcion == 1:
            for i in range(3):
                usu = input("\033[1;36m"+"> Ingrese el nombre de usuario: "+'\033[0;m')
                usuario(usu)
                ingresoUsu = InicioUsuario(usu)
                if ingresoUsu == True:
                    passwor = input("\033[1;36m"+"> Ingrese su contraseña: "+'\033[0;m')
                    valicontra(passwor)
                    ingresopass = InicioValicontra(passwor)
                if ingresopass == True and ingresoUsu == True:
                    break
                else:
                    print("\033[1;36m"+f"> Tienes {3-(i+1)} intentos"+'\033[0;m')

        elif opcion == 2:
            for i in range(3):
                if ingresopass == True and ingresoUsu == True:
                    usuarioo = input("\033[1;36m"+"> Ingrese su Usario: "+'\033[0;m')
                    passwordd = input("\033[1;36m"+"> Ingrese su Contraseña: "+'\033[0;m')
                    if usuarioo == usu and passwordd == passwor:
                        print("\033[1;32m"+"> Inicio de Sesion Exitoso "+'\033[0;m')
                        print("\033[1;32m"+f"> BIENVENIDO {usuarioo} "+'\033[0;m')
                        break
                    else:
                        print("\033[1;31m"+"> Credenciales incorrectas. "+'\033[0;m')
                        print("\033[1;36m"+f"> Tienes {3-(i+1)} intentos"+'\033[0;m')
                        print("\033[1;33m"+"--------------------------------------------------------------"+'\033[0;m')
                else:
                    print("\033[1;31m"+"> Necesita registrarse. "+'\033[0;m')
                    break
            
        elif opcion == 3:
            break
        else:
            print("\033[1;31m"+"> Opcion Invalida. "+'\033[0;m')

    except:
        print("\033[1;31m"+"> Ingrese el numero de la opcion. "+'\033[0;m')