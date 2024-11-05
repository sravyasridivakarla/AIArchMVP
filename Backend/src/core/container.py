from dependency_injector import containers, providers
from ...src.repositories.vector_repository import VectorRepository

class Container(containers.DeclarativeContainer):
    vector_repository = providers.Singleton(VectorRepository)

    # Wire the container to these modules
    wiring_config = containers.WiringConfiguration(
        modules=[
            "Backend.src.api.routes"
        ]
    )