import time

# =================== DATOS INICIALES ===================

USUARIO = "admin"
CONTRASENA = "1234"
memoria_total = 8192  # MB
memoria_disponible = memoria_total

# Cada proceso tiene: nombre, prioridad, uso de memoria (MB), estado
procesos = [
    {"nombre": "Proceso 1", "prioridad": 3, "memoria": 1024, "activo": False},
    {"nombre": "Proceso 2", "prioridad": 2, "memoria": 512, "activo": False},
    {"nombre": "Proceso 3", "prioridad": 5, "memoria": 2048, "activo": False},
    {"nombre": "Proceso 4", "prioridad": 1, "memoria": 256, "activo": False},
    {"nombre": "Proceso 5", "prioridad": 4, "memoria": 1536, "activo": False},
    {"nombre": "Proceso 6", "prioridad": 3, "memoria": 1024, "activo": False},
    {"nombre": "Proceso 7", "prioridad": 2, "memoria": 512, "activo": False},
    {"nombre": "Proceso 8", "prioridad": 5, "memoria": 2048, "activo": False}
]

# =================== FUNCIONES ===================

def iniciarSistema():
    print("Iniciando sistema operativo experimental...")
    for mensaje in ["Cargando kernel...", "Inicializando módulos...", "Verificando memoria...", "Sistema listo."]:
        print(mensaje)
        time.sleep(0.5)
    
    while True:
        usuario = input("Usuario: ")
        clave = input("Contraseña: ")
        if usuario == USUARIO and clave == CONTRASENA:
            print("Acceso concedido.\n")
            break
        else:
            print("Usuario o contraseña incorrectos. Intente de nuevo.\n")

def mostrarMenu():
    print("\n==== MENÚ DEL SISTEMA ====")
    print("1. Iniciar procesos")
    print("2. Modificar procesos")
    print("3. Aumentar memoria")
    print("4. Ver procesos activos")
    print("5. Apagar sistema")

def iniciarProcesos():
    global memoria_disponible
    print("\nProcesos disponibles:")
    for i, p in enumerate(procesos):
        estado = "Activo" if p["activo"] else "Inactivo"
        print(f"{i+1}. {p['nombre']} (Prioridad: {p['prioridad']}, Memoria: {p['memoria']} MB) - {estado}")
    
    seleccion = input("Ingrese los números de los procesos a iniciar (separados por coma): ")
    try:
        indices = sorted(set(int(x.strip()) - 1 for x in seleccion.split(",")))
    except:
        print("Entrada no válida.")
        return

    seleccionados = []
    for i in indices:
        if 0 <= i < len(procesos):
            if not procesos[i]["activo"]:
                seleccionados.append(procesos[i])
            else:
                print(f"{procesos[i]['nombre']} ya está activo. Saltando.")
        else:
            print(f"Índice {i+1} fuera de rango.")

    seleccionados.sort(key=lambda x: x["prioridad"], reverse=True)

    for p in seleccionados:
        if p["memoria"] <= memoria_disponible:
            memoria_disponible -= p["memoria"]
            p["activo"] = True
            print(f"{p['nombre']} iniciado. Memoria restante: {memoria_disponible} MB")
        else:
            print(f"No hay suficiente memoria para iniciar {p['nombre']}.")
            print("1. Cerrar procesos")
            print("2. Aumentar memoria")
            print("3. Cancelar")
            opcion = input("Elija una opción: ")
            if opcion == "1":
                cerrarProcesos()
            elif opcion == "2":
                aumentarMemoria()
            break

def cerrarProcesos():
    global memoria_disponible
    activos = [p for p in procesos if p["activo"]]
    if not activos:
        print("No hay procesos activos.")
        return
    print("Procesos activos:")
    for i, p in enumerate(activos):
        print(f"{i+1}. {p['nombre']} (Memoria: {p['memoria']} MB)")
    try:
        indice = int(input("Ingrese el número del proceso a cerrar: ")) - 1
        proceso = activos[indice]
        proceso["activo"] = False
        memoria_disponible += proceso["memoria"]
        print(f"{proceso['nombre']} cerrado. Memoria disponible: {memoria_disponible} MB")
    except:
        print("Selección inválida.")

def modificarProceso():
    print("\nModificar procesos:")
    for i, p in enumerate(procesos):
        print(f"{i+1}. {p['nombre']} (Prioridad: {p['prioridad']}, Memoria: {p['memoria']} MB)")
    try:
        i = int(input("Seleccione el número del proceso: ")) - 1
        if 0 <= i < len(procesos):
            nueva_prioridad = int(input("Nueva prioridad: "))
            nueva_memoria = int(input("Nuevo uso de memoria (MB): "))
            procesos[i]["prioridad"] = nueva_prioridad
            procesos[i]["memoria"] = nueva_memoria
            print(f"{procesos[i]['nombre']} actualizado.")
        else:
            print("Número inválido.")
    except:
        print("Entrada inválida.")

def aumentarMemoria():
    global memoria_total, memoria_disponible
    try:
        extra = int(input("Cantidad de memoria a agregar (MB): "))
        memoria_total += extra
        memoria_disponible += extra
        print(f"Memoria total: {memoria_total} MB | Memoria disponible: {memoria_disponible} MB")
    except:
        print("Entrada inválida.")

def verProcesosActivos():
    print("\nProcesos activos:")
    activos = [p for p in procesos if p["activo"]]
    if not activos:
        print("Ninguno.")
    for p in activos:
        print(f"{p['nombre']} (Prioridad: {p['prioridad']}, Memoria: {p['memoria']} MB)")

def apagarSistema():
    print("\nCerrando procesos...")
    time.sleep(0.5)
    print("Liberando memoria...")
    time.sleep(0.5)
    print("Apagando sistema...")
    time.sleep(0.5)
    print("Sistema apagado. ¡Hasta luego!")
    exit()

# =================== PROGRAMA PRINCIPAL ===================

def main():
    iniciarSistema()
    while True:
        mostrarMenu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            iniciarProcesos()
        elif opcion == "2":
            modificarProceso()
        elif opcion == "3":
            aumentarMemoria()
        elif opcion == "4":
            verProcesosActivos()
        elif opcion == "5":
            apagarSistema()
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
