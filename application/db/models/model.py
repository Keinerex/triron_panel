from sqlalchemy.orm import relationship

from db.models.base import BaseTable
from sqlalchemy import Column, VARCHAR


class Model(BaseTable):
    __tablename__ = "models"

    name = Column(VARCHAR, unique=True)

    versions = relationship("Version", back_populates="model")
