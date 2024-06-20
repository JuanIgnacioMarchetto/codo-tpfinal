"""
****Agregar Tarea con Fecha de Vencimiento:
Modificar la función agregar_tarea para incorporar fecha de vencimiento.

****Listar Tareas con Estado:
Cambiar la función ver_listado para mostrar si las tareas están completadas o vencidas.

****Buscar Tarea por Descripción:
agregar una función para buscar una tarea por descripción.

Marcar Tarea como Completada:
Crear una función q marque una tarea como completada.

Validación de Datos:
poner validaciones  (descripción no vacía, formato de fecha válido).

Actualizar el Menú:
agregar nuevas opciones en el menú de opciones.

Actualizar el Bucle Principal:
Incluir los nuevos casos en el bucle principal para ejecutar las acciones adecuadas.
"""

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
            tarea["nombre_tarea"] = nuevoNombre
            tarea["descrip"] = nuevaDescripcion
            print("Descripción Actualizada con ÉXITO")
            return
    print(f"Tarea con el nombre {nombre} no encontrada")

def buscar_tarea(descripcion):
    for tarea in listaDeTareas:
        if descripcion.lower() in tarea["descrip"].lower():
            print(f"Tarea encontrada: {tarea['nombre_tarea']} : {tarea['descrip']} (Vencimiento: {tarea['fecha_vencimiento']})")
            return
    print("Tarea no encontrada")

def ver_opciones_menu():
    print("------ PROGRAMA DE TAREAS ---------")
    print("1) Ver listado de tareas")
    print("2) Agregar una tarea nueva")
    print("3) Editar una tarea existente")
    print("4) Eliminar una tarea de la lista")
    print("5) Salir del programa")
    
def login():
    # Credenciales predefinidas
    usuario_correcto = "Marcos"
    contrasena_correcta = "1234"
    intentos = 3
    
    while intentos > 0:
        # Solicitar nombre de usuario y contraseña
        usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")
        
        # Verificar las credenciales
        if usuario == usuario_correcto and contrasena == contrasena_correcta:
            print("Inicio de sesión exitoso")
            return
        else:
            intentos -= 1
            print(f"Nombre de usuario o contraseña incorrectos. Intentos restantes: {intentos}")
    
    print("Se han agotado los intentos. Acceso denegado.")
    
#----ESTRUCTURA PRINCIPAL DEL PROGRAMA-----
    
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
            print("Saliendo del programa")
            ejecutarPrograma = False
        case _:
            print("Selecciona una opción válida")