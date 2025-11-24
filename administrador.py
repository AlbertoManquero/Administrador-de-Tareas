import psutil
import os

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_procesos_ordenados_por_ram():
    procesos = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            procesos.append(proc)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    procesos.sort(key=lambda p: p.info['memory_info'].rss, reverse=True)
    return procesos

def mostrar_procesos(procesos, limite=None):
    for i, p in enumerate(procesos[:limite] if limite else procesos):
        mem_mb = p.info['memory_info'].rss / (1024 * 1024)
        print(f"{i + 1}.- {p.info['name']} (PID: {p.info['pid']}, RAM: {mem_mb:.2f} MB)")

def detener_proceso(pid):
    try:
        p = psutil.Process(pid)
        p.terminate()
        p.wait(timeout=3)
        print(f"Proceso {pid} detenido.")
    except Exception as e:
        print(f"No se pudo detener el proceso: {e}")

def menu_principal():
    while True:
        limpiar()
        print("Iniciando gestor...\n")
        print("1.- Tareas principales")
        print("2.- Todas las tareas")
        print("Q - Salir")

        opcion = input("Seleccione una opción: ").strip().lower()

        if opcion == '1':
            menu_top_procesos()
        elif opcion == '2':
            menu_todos_procesos()
        elif opcion == 'q':
            break

def menu_top_procesos():
    procesos = obtener_procesos_ordenados_por_ram()
    while True:
        limpiar()
        print("Top 10 procesos que consumen más RAM:\n")
        mostrar_procesos(procesos, limite=10)

        print("\nEscriba el número del proceso que desee detener.")
        print("Q - Volver al inicio")
        opcion = input("Opción: ").strip().lower()

        if opcion == 'q':
            break
        elif opcion.isdigit() and 1 <= int(opcion) <= 10:
            idx = int(opcion) - 1
            pid = procesos[idx].info['pid']
            detener_proceso(pid)
            input("Presione Enter para continuar...")

def menu_todos_procesos():
    procesos = obtener_procesos_ordenados_por_ram()
    while True:
        limpiar()
        print("Lista de todos los procesos:\n")
        mostrar_procesos(procesos[:30])  # Mostrar solo 30 por defecto

        print("\nEscriba el número del proceso que desee detener.")
        print("E - Buscador [\"Lo que escriba el usuario tiene que verse así\"]")
        print("Q - Volver al inicio")
        opcion = input("Opción: ").strip().lower()

        if opcion == 'q':
            break
        elif opcion == 'e':
            buscar = input("Buscador [\"Nombre del proceso\"]: ").strip().lower()
            resultados = [p for p in procesos if buscar in p.info['name'].lower()]
            limpiar()
            print(f"Resultados para \"{buscar}\":\n")
            mostrar_procesos(resultados)
            input("\nPresione Enter para volver...")
        elif opcion.isdigit():
            idx = int(opcion) - 1
            if 0 <= idx < len(procesos):
                pid = procesos[idx].info['pid']
                detener_proceso(pid)
                input("Presione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
