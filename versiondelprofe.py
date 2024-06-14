listaDeTareas = [
    {"nombre_tarea": "Comprar leche",
        "descrip": "Ir al supermercado y comprar leche"},
    {"nombre_tarea": "Hacer ejercicio",
    "descrip": "Hacer una rutina de ejercicios de 30 minutos"},
    { "nombre_tarea": "Estudiar Python",
     "descrip": "Completar el capítulo 3 del libro de Python" }
]
def agregar_tarea(nombre, descripcion):
    tareaNueva = {
        "nombre_tarea": nombre,
        "descrip": descripcion
    }
    listaDeTareas.append(tareaNueva)

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

def ver_listado():
    for i in listaDeTareas:
        print(f"{i['nombre_tarea']} : {i['descrip']}")

def ver_opciones_menu():
    print("------ PROGRAMA DE TAREAS ---------")
    print("1) Ver listado de tareas")
    print("2) Agregar una tarea nueva")
    print("3) Editar una tarea existente")
    print("4) Eliminar una tarea de la lista")
    print("5) Salir del programa")

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
            agregar_tarea(tareaNueva_nombre, tareaNueva_descripcion)
            print("Tarea agregada con ÉXITO!")
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
