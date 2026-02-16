"""
Cliente RMI usando Pyro5.
Se conecta al servidor remoto y consume los métodos expuestos por ISalarios.
"""

import Pyro5.api

from typing import List


def iniciar_cliente() -> None:
    """
    Cliente que se conecta al objeto remoto SalariosImpl:
    1. Localiza el objeto remoto a través del Name Server
    2. Invoca los métodos remotos:
       - llenarMatriz()
       - calcularTotalEmpleado()
       - calcularPromedioMes()
       - calcularTotalGeneral()
    3. Muestra los resultados al usuario
    """
    # Configuración
    num_empleados: int = 5
    num_meses: int = 12

    # Conectar al objeto remoto a través del Name Server
    salarios = Pyro5.api.Proxy("PYRONAME:salarios.service")

    print("=" * 60)
    print("   SISTEMA DE GESTIÓN DE SALARIOS - CLIENTE RMI")
    print("=" * 60)

    # 1. Generar la matriz de salarios
    print(f"\nGenerando matriz de salarios ({num_empleados} empleados x {num_meses} meses)...")
    matriz: List[List[float]] = salarios.llenarMatriz(num_empleados, num_meses)

    print("\nMatriz de salarios:")
    for i, fila in enumerate(matriz):
        salarios_formateados = [f"${s:,.2f}" for s in fila]
        print(f"  Empleado {i + 1}: {salarios_formateados}")

    # 2. Total por empleado
    print("\n" + "-" * 60)
    totales: List[float] = salarios.calcularTotalEmpleado(matriz)
    print("Total pagado por empleado:")
    for i, total in enumerate(totales):
        print(f"  Empleado {i + 1}: ${total:,.2f}")

    # 3. Promedio por mes
    print("\n" + "-" * 60)
    promedios: List[float] = salarios.calcularPromedioMes(matriz)
    print("Promedio de salarios por mes:")
    for i, promedio in enumerate(promedios):
        print(f"  Mes {i + 1}: ${promedio:,.2f}")

    # 4. Total general
    print("\n" + "-" * 60)
    total_general: float = salarios.calcularTotalGeneral(matriz)
    print(f"Total general de la matriz: ${total_general:,.2f}")

    print("\n" + "=" * 60)
    print("   Operaciones completadas exitosamente")
    print("=" * 60)


if __name__ == "__main__":
    iniciar_cliente()
