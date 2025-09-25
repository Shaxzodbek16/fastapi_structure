from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from sqlalchemy import Integer, DateTime, func
from datetime import datetime

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, index=True, unique=True
    )


class TimestampMixin:
    __abstract__ = True
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=True, onupdate=func.now()
    )
