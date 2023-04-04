from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session


class HealthCheckRepository:
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory = session_factory

    async def get_status(self) -> bool:
        with self.session_factory() as session:
            return session.is_active
