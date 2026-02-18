"""
Cliente RMI usando Pyro5.
Se conecta al servidor remoto y consume los métodos expuestos por ISalarios.
"""

import Pyro5.api

from typing import List


def mostrar_menu() -> None:
    print("\n" + "=" * 60)
    print("   SISTEMA DE GESTIÓN DE SALARIOS - MENÚ PRINCIPAL")
    print("=" * 60)
    print("1. Generar nueva matriz de salarios")
    print("2. Calcular total pagado por empleado")
    print("3. Calcular promedio de salarios por mes")
    print("4. Calcular total general de la matriz")
    print("5. Mostrar matriz actual")
    print("6. Salir")
    print("=" * 60)


def iniciar_cliente() -> None:
    """
    Cliente interactivo que se conecta al objeto remoto SalariosImpl.
    """
    try:
        # Conectar al objeto remoto a través del Name Server
        salarios = Pyro5.api.Proxy("PYRONAME:salarios.service")
        
        # Verificar conexión inicial
        salarios._pyroBind()
        
        # Identificación inicial con el servidor
        print("\nConectando al servidor remoto...")
        nombre_usuario = input("Ingrese su nombre para identificarse: ")
        saludo = salarios.conectar(nombre_usuario)
        print(f"\nRespuesta del servidor: {saludo}")
        
        matriz: List[List[float]] = []
        
        while True:
            mostrar_menu()
            opcion = input("Seleccione una opción (1-6): ")
            
            if opcion == "1":
                try:
                    e = int(input("Ingrese número de empleados: "))
                    m = int(input("Ingrese número de meses: "))
                    if e <= 0 or m <= 0:
                        print("Error: Los valores deben ser mayores a cero.")
                        continue
                        
                    print(f"\nGenerando matriz de {e}x{m}...")
                    matriz = salarios.llenarMatriz(e, m)
                    print("¡Matriz generada con éxito!")
                except ValueError:
                    print("Error: Ingrese valores numéricos válidos.")
                except Exception as ex:
                    print(f"Error remoto: {ex}")

            elif opcion == "2":
                if not matriz:
                    print("\nError: Primero debe generar la matriz (Opción 1).")
                    continue
                
                print("\nCalculando total por empleado...")
                totales = salarios.calcularTotalEmpleado(matriz)
                for i, total in enumerate(totales):
                    print(f"  Empleado {i + 1}: ${total:,.2f}")

            elif opcion == "3":
                if not matriz:
                    print("\nError: Primero debe generar la matriz (Opción 1).")
                    continue
                
                print("\nCalculando promedio por mes...")
                promedios = salarios.calcularPromedioMes(matriz)
                for i, promedio in enumerate(promedios):
                    print(f"  Mes {i + 1}: ${promedio:,.2f}")

            elif opcion == "4":
                if not matriz:
                    print("\nError: Primero debe generar la matriz (Opción 1).")
                    continue
                
                total_general = salarios.calcularTotalGeneral(matriz)
                print(f"\nTotal general de la matriz: ${total_general:,.2f}")

            elif opcion == "5":
                if not matriz:
                    print("\nError: No hay una matriz generada para mostrar.")
                    continue
                
                print("\nMatriz de salarios actual:")
                for i, fila in enumerate(matriz):
                    salarios_formateados = [f"${s:,.2f}" for s in fila]
                    print(f"  Empleado {i + 1}: {salarios_formateados}")

            elif opcion == "6":
                print("\nSaliendo del sistema. ¡Hasta luego!")
                break
            
            else:
                print("\nOpción no válida. Intente de nuevo.")

    except Exception as e:
        print(f"\nError de conexión: No se pudo encontrar el servidor remoto.")
        print(f"Detalles: {e}")
        print("\nVerifique que el servidor (servidor.py) y el Name Server de Pyro5 estén corriendo.")


if __name__ == "__main__":
    iniciar_cliente()
