from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column

Base = declarative_base()

from sqlalchemy import Column, String, DateTime

class LogEntry(Base):
    __tablename__ = 'log_entries'

    id: Mapped[int] = mapped_column(primary_key=True)
    city_name = Column(String, nullable=False)
    timestamp = Column(DateTime(timezone=True), nullable=False)
    resource_address = Column(String, nullable=False)