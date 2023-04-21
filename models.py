from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import BigInteger, Sequence

db = SQLAlchemy()

class Address(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True)
    address_id = db.Column(BigInteger, Sequence('my_table_address_id_seq'), unique=True)
    coin = db.Column(db.String, nullable=False)
    address = db.Column(db.String(2083), nullable=False)
    wallet = db.Column(db.String, nullable=False)
    pub_key = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Address {self.coin}:{self.address}>'