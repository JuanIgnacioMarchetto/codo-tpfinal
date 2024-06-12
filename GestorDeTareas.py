"""CONSULTAR AL PROFE SI NOS PERMITE AGREGAR UN HTML Y CSS PPARA DARLE MAS ONDA A LA APP"""

""" 
Variables y Tipos Simples
Definir una lista para almacenar las tareas.

Funciones
Mostrar Menú:
Crear una función para mostrar el menú de opciones y tomar la elección del usuario.

Agregar Tarea:
Función para q el  usuario ingrese una tarea nueva con descripción y fecha de vencimiento.

Listar Tareas:
Función para mostrar todas las tareas,mostrando si están completadas o vencidas.

buscar Tarea:
Función para permitir al usuario buscar una tarea por  descripción.

Eliminar Tarea:
Función para  eliminar una tarea  .

Marcar Tarea como Completada:
Función paramarcar una tarea como completada .

Bucle Principal
Bucle que muestre el menú y ejecute la acción elegida.

Validación de Datos
Implementar validaciones para asegurarse de que las entradas  sean correctas (descripcion no vacía, formato de fecha).

 """
 
tasks = []
 
def mostrar_menu():
    print("\nMenu de Opciones:")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Buscar tarea")
    print("4. Eliminar tarea")
    print("5. Marcar tarea como completada")
    print("6. Salir")
    return input("Seleccione una opcion: ")
def agregar_tarea():
    descripcion = input("Ingresa una tarea: ").strip()
    if not descripcion:
        print("La descripción no puede estar vacía.")
        return
    
    fecha_vencimiento = input("Ingresa una fecha de vencimiento (YYYY-MM-DD): ")
    try:
        datetime.strptime(fecha_vencimiento, '%Y-%m-%d')
    except ValueError:
        print("Formato inválido.")
        return
    
    tarea = {'descripcion': descripcion, 'fecha_vencimiento': fecha_vencimiento, 'completada': False}
    tasks.append(tarea)
    print("Genial Tarea agregada .")

