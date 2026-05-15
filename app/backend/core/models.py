from sqlalchemy import Column, String, Float, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class ReceiptAudit(Base):
    __tablename__ = "receipt_audits"
    
    id = Column(Integer, primary_key=True)
    tx_hash = Column(String, unique=True, index=True)
    sender_address = Column(String, index=True)
    amount_mon = Column(Float)
    risk_score = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)