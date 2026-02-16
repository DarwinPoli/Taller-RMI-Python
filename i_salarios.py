"""
Interface remota ISalarios.
Define el contrato para la gestión de la matriz de salarios de empleados.
"""

from abc import ABC, abstractmethod
from typing import List


class ISalarios(ABC):
    """
    Interface que define las operaciones remotas disponibles
    para la gestión de salarios de empleados.
    """

    @abstractmethod
    def llenarMatriz(self, num_empleados: int, meses: int) -> List[List[float]]:
        """
        Genera y retorna una matriz de salarios con valores aleatorios.

        Args:
            num_empleados: Número de empleados (filas).
            meses: Número de meses (columnas).

        Returns:
            Matriz de salarios [empleados x meses].
        """
        pass

    @abstractmethod
    def calcularTotalEmpleado(self, matriz: List[List[float]]) -> List[float]:
        """
        Calcula el total pagado a cada empleado en todos los meses.

        Args:
            matriz: Matriz de salarios [empleados x meses].

        Returns:
            Lista con el total pagado por cada empleado.
        """
        pass

    @abstractmethod
    def calcularPromedioMes(self, matriz: List[List[float]]) -> List[float]:
        """
        Calcula el promedio de salarios pagados en cada mes.

        Args:
            matriz: Matriz de salarios [empleados x meses].

        Returns:
            Lista con el promedio de salarios por mes.
        """
        pass

    @abstractmethod
    def calcularTotalGeneral(self, matriz: List[List[float]]) -> float:
        """
        Calcula el total general de todos los salarios en la matriz.

        Args:
            matriz: Matriz de salarios [empleados x meses].

        Returns:
            Total general de la matriz.
        """
        pass
