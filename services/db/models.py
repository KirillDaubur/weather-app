from sqlmodel import SQLModel, Field


class LogEntry(SQLModel, table=True):
    id: int = Field(primary_key=True)
    city: str
    timestamp: int
    resource_address: str