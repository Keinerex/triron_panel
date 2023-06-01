from sqlalchemy.orm import relationship

from db.models.base import BaseTable
from sqlalchemy import Column, VARCHAR, ForeignKey


class Triton(BaseTable):
    __tablename__ = "triton_loaded"

    model_version_id = Column(ForeignKey("versions.id"))

    model_version = relationship("Version", back_populates="is_loaded")
