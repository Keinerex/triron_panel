from sqlalchemy.orm import relationship

from db.models.base import BaseTable
from sqlalchemy import Column, VARCHAR, ForeignKey


class Version(BaseTable):
    __tablename__ = "versions"

    name = Column(VARCHAR, unique=True)
    model_id = Column(ForeignKey("models.id"))

    model = relationship("Model", back_populates="versions")
    is_loaded = relationship("Triton", back_populates="model_version")
