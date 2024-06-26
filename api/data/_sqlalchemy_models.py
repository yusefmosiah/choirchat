from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped, relationship
from sqlalchemy import String, Boolean, UUID, DateTime, Text, ForeignKey, Integer

import datetime
import uuid


class Base(DeclarativeBase):
    pass


class MESSAGE(Base):
    __tablename__ = "messages_table"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, index=True, default=uuid.uuid4)

    user_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("users_table.id", ondelete="CASCADE"), nullable=False)
    user: Mapped["USER"] = relationship("USER", back_populates="messages")


class USER(Base):
    """
    Represents a User in the database.
    """

    __tablename__ = "users_table"

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    full_name: Mapped[str] = mapped_column(String)
    hashed_password: Mapped[str] = mapped_column(String, index=True)
    email_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    voice: Mapped[int] = mapped_column(Integer, default=0)

    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc)
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.datetime.now(datetime.timezone.utc),
        onupdate=lambda: datetime.datetime.now(datetime.timezone.utc),
    )

    messages = relationship("MESSAGE", back_populates="user")
