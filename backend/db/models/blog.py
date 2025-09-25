from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.base_class import Base



class Blog(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="blogs")
    slug=Column(String, unique=True, index=True)