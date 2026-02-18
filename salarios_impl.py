"""
Implementación de la interface ISalarios usando Pyro5.
Expone los métodos remotos para la gestión de la matriz de salarios.
"""
import random

import Pyro5.api
from random import Random
from typing import List

from i_salarios import ISalarios


@Pyro5.api.expose
class SalariosImpl(ISalarios):
    """
    Implementación concreta de ISalarios.
    Expuesta como objeto remoto mediante Pyro5 (equivalente a RMI en Java).
    """

    def __init__(self) -> None:
        self.random: Random = Random()

    def llenarMatriz(self, num_empleados: int, meses: int) -> List[List[float]]:
        """
        Llena una matriz con salarios aleatorios entre 1,000,000 y 5,000,000
        """
        matriz = []
        for i in range(num_empleados):
            fila = []
            for j in range(meses):
                salario = random.uniform(1000000, 5000000)
                fila.append(salario)
            matriz.append(fila)
        print("Matriz de salarios generada exitosamente")
        print(matriz)
        return matriz

    def calcularTotalEmpleado(self, matriz: List[List[float]]) -> List[float]:
        totales = []
        for fila in matriz:
            total = sum(fila)
            totales.append(total)

        print("Totales por empleado calculados")
        return totales

    def calcularPromedioMes(self, matriz: List[List[float]]) -> List[float]:
        if not matriz or len(matriz) == 0:
            return []

        num_meses = len(matriz[0])
        num_empleados = len(matriz)
        promedios = []

        for j in range(num_meses):
            suma = sum(matriz[i][j] for i in range(num_empleados))
            promedio = suma / num_empleados
            promedios.append(promedio)

        print("Promedios por mes calculados")
        return promedios

    def calcularTotalGeneral(self, matriz: List[List[float]]) -> float:
        total = sum(sum(fila) for fila in matriz)

        print(f"Total general calculado: ${total:,.2f}")
        return total
