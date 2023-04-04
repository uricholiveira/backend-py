from src.repositories.health_check import HealthCheckRepository


class HealthCheckService:
    def __init__(self, health_check_repository: HealthCheckRepository) -> None:
        self._repository: HealthCheckRepository = health_check_repository

    async def get_status(self) -> bool:
        return await self._repository.get_status()
