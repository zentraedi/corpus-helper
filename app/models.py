from app import db


# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.BigInteger)
    text_ref = db.Column('textRef', db.String(8000), nullable=False)
