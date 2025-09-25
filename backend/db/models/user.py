from db.base_class import Base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from db.models.blog import Blog  # noqa



class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password=Column(String, nullable=False  )
    #full_name = Column(String, index=True)
    #hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    #is_superuser = Column(Boolean, default=False)
    blogs = relationship("Blog", back_populates="owner")