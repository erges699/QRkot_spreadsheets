from datetime import datetime as dt

from sqlalchemy import Column, Integer, DateTime, Boolean

from app.core.db import Base


class CharityDonationBaseClass(Base):
    __abstract__ = True

    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, nullable=False, default=0)
    fully_invested = Column(Boolean, nullable=False, default=False)
    create_date = Column(DateTime, nullable=False, default=dt.now)
    close_date = Column(DateTime)
