#Definiendo el nombre de usuario y su contraseña
user_name:"Riwi"
user_password: 123
#Bool que valida que el usuario y contraseña
is_valid: bool = False
#Contador de intentos
attempts= 0

while is_valid == False:
    try:
        name=input("Digite el nombre de usuario: ")
        password=int(input("Digite su contraseña"))
        if (name==user_name and password==user_password):
            print("Iniciaste sesión correctamente")
            is_valid=True
        else:
            print("Usuario y/o Contraseña inválidos")

    except:
        print("Contraseña inválida")