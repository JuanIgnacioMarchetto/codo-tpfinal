from datetime import datetime

listaDeTareas = [
    {"nombre_tarea": "Comprar leche",
        "descrip": "Ir al supermercado y comprar leche",
        "fecha_vencimiento": "20/06/2024",
        "completada": False},
    {"nombre_tarea": "Hacer ejercicio",
        "descrip": "Hacer una rutina de ejercicios de 30 minutos",
        "fecha_vencimiento": "21/06/2024",
        "completada": False},
    {"nombre_tarea": "Estudiar Python",
        "descrip": "Completar el capítulo 3 del libro de Python",
        "fecha_vencimiento": "22/06/2024",
        "completada": False}
]

def agregar_tarea(nombre, descripcion, fecha_vencimiento):
    if not nombre.strip():
        print("El nombre de la tarea no puede estar vacío.")
        return
    if not descripcion.strip():
        print("La descripción de la tarea no puede estar vacía.")
        return
    try:
        datetime.strptime(fecha_vencimiento, "%d/%m/%Y")
    except ValueError:
        print("Formato de fecha inválido. Debe ser DD/MM/YYYY.")
        return
    
    tareaNueva = {
        "nombre_tarea": nombre,
        "descrip": descripcion,
        "fecha_vencimiento": fecha_vencimiento,
        "completada": False
    }
    listaDeTareas.append(tareaNueva)
    print("Tarea agregada con ÉXITO!")

def ver_listado():
    hoy = datetime.now()
    for tarea in listaDeTareas:
        estado = "Completada" if tarea["completada"] else ("Vencida" if datetime.strptime(tarea["fecha_vencimiento"], "%d/%m/%Y") < hoy else "Pendiente")
        print(f"{tarea['nombre_tarea']} : {tarea['descrip']} (Estado: {estado})")

def borrar_tarea(nombre):
    for tarea in listaDeTareas:
        if tarea["nombre_tarea"].lower() == nombre.lower():
            listaDeTareas.remove(tarea)
            print(f"Tarea: {nombre} eliminada con éxito")
            return
    print(f"Tarea con el nombre {nombre} NO ENCONTRADA")

def editar_tarea(nombre):
    for tarea in listaDeTareas:
        if tarea["nombre_tarea"].lower() == nombre.lower():
            nuevoNombre = input(f"Ingrese el nuevo nombre para reemplazar a {nombre}: ")
            nuevaDescripcion = input(f"Ingresa la nueva descripción para {nombre}: ")
            nuevaFecha = input(f"Ingresa la nueva fecha de vencimiento (DD/MM/YYYY) para {nombre}: ")
            try:
                datetime.strptime(nuevaFecha, "%d/%m/%Y")
            except ValueError:
                print("Formato de fecha inválido. Debe ser DD/MM/YYYY.")
                return
            
            tarea["nombre_tarea"] = nuevoNombre
            tarea["descrip"] = nuevaDescripcion
            tarea["fecha_vencimiento"] = nuevaFecha
            print("Descripción Actualizada con ÉXITO")
            return
    print(f"Tarea con el nombre {nombre} no encontrada")

def buscar_tarea(descripcion):
    for tarea in listaDeTareas:
        if descripcion.lower() in tarea["descrip"].lower():
            print(f"Tarea encontrada: {tarea['nombre_tarea']} : {tarea['descrip']} (Vencimiento: {tarea['fecha_vencimiento']})")
            return
    print("Tarea no encontrada")

def marcar_completada(nombre):
    for tarea in listaDeTareas:
        if tarea["nombre_tarea"].lower() == nombre.lower():
            tarea["completada"] = True
            print(f"Tarea {nombre} marcada como completada.")
            return
    print(f"Tarea con el nombre {nombre} no encontrada")

def ver_opciones_menu():
    print("------ PROGRAMA DE TAREAS ---------")
    print("1) Ver listado de tareas")
    print("2) Agregar una tarea nueva")
    print("3) Editar una tarea existente")
    print("4) Eliminar una tarea de la lista")
    print("5) Buscar una tarea por descripción")
    print("6) Marcar tarea como completada")
    print("7) Salir del programa")
    
def login():
    usuario_correcto = "Marcos"
    contrasena_correcta = "1234"
    intentos = 3
    
    while intentos > 0:
       
        usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")
        
        if usuario == usuario_correcto and contrasena == contrasena_correcta:
            print("Inicio de sesión exitoso")
            return
        else:
            intentos -= 1
            print(f"Nombre de usuario o contraseña incorrectos. Intentos restantes: {intentos}")
    
    print("Se han agotado los intentos. Acceso denegado.")
    exit()


login()

ejecutarPrograma = True

while ejecutarPrograma:
    ver_opciones_menu()
    opcion = int(input("Elige una opción: "))
    
    match opcion:
        case 1:
            ver_listado()
        case 2:
            tareaNueva_nombre = input("Ingrese el nombre de la nueva tarea: ")
            tareaNueva_descripcion = input("Ingresa la descripción de la nueva tarea: ")
            tareaNueva_fecha = input("Ingresa la fecha de vencimiento (DD/MM/YYYY): ")
            agregar_tarea(tareaNueva_nombre, tareaNueva_descripcion, tareaNueva_fecha)
        case 3:
            tarea_a_editar = input("Ingrese el nombre de la tarea a EDITAR: ")
            editar_tarea(tarea_a_editar)
        case 4:
            tarea_a_borrar = input("Ingrese el nombre de la tarea que quieras borrar: ")
            borrar_tarea(tarea_a_borrar)
        case 5:
            tarea_a_buscar = input("Ingrese la descripción de la tarea a buscar: ")
            buscar_tarea(tarea_a_buscar)
        case 6:
            tarea_a_completar = input("Ingrese el nombre de la tarea a marcar como completada: ")
            marcar_completada(tarea_a_completar)
        case 7:
            print("Saliendo del programa")
            ejecutarPrograma = False
        case _:
            print("Selecciona una opción válida")
