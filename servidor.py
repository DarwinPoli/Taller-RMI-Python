"""
Servidor RMI usando Pyro5.
Registra el objeto remoto SalariosImpl y lo pone disponible para clientes.
"""

import Pyro5.api
import Pyro5.server

from salarios_impl import SalariosImpl


def iniciar_servidor() -> None:
    """
    Inicializa el servidor Pyro5:
    1. Crea una instancia de SalariosImpl
    2. Registra el objeto remoto en el Name Server
    3. Inicia el bucle de solicitudes (request loop)
    """
    # Crear el daemon de Pyro5
    daemon = Pyro5.server.Daemon()

    # Localizar el Name Server
    ns = Pyro5.api.locate_ns()

    # Registrar el objeto remoto en el daemon
    uri = daemon.register(SalariosImpl)

    # Registrar en el Name Server con nombre lógico
    ns.register("salarios.service", uri)

    print(f"Servidor de Salarios listo.")
    print(f"URI: {uri}")
    print("Esperando peticiones de clientes...")

    # Iniciar el bucle de solicitudes
    daemon.requestLoop()


if __name__ == "__main__":
    iniciar_servidor()
