from typing import Optional, TypeVar  # noqa: I001
from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from .repository import SQLAlchemyAsyncRepository  # noqa: I001
from ..models import RefreshSession, User
from api.schemas.token import RefreshSessionCreate, RefreshSessionUpdate
from api.schemas.user import UserCreate, UserUpdate
from utils.specification import ISpecification

SpecificationType = TypeVar("SpecificationType", bound=ISpecification)


@dataclass(kw_only=True)
class UserRepository(SQLAlchemyAsyncRepository[User, UserCreate, UserUpdate]):
    async def get_user_refresh_session(
        self, spec: Optional[SpecificationType] = None
    ) -> User:
        """Get a user with their associated refresh session.

        Args:
            spec (Optional[ISpecification]): A filter specification.

        Returns:
            User: The user with their associated refresh session.
        """
        return await self._session.scalar(
            select(User)
            .filter(spec.is_satisfied_by(User))
            .options(joinedload(User.refresh_session))
        )


@dataclass
class RefreshSessionRepository(
    SQLAlchemyAsyncRepository[
        RefreshSession, RefreshSessionCreate, RefreshSessionUpdate
    ]
):
    pass
