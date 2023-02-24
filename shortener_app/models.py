# This file declares how your data should be stored in the database
# shortener_app.models.py

from sqlalchemy import Boolean, Column, Integer, String

from .database import base

class URL(base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, index=True)
    secret_key = Column(String, unique=True, index=True)
    target_url = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    clicks = Column(Integer, default=0)