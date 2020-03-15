from app.models import Base
from app import db


class Corpus(db.Model):

    # __table_args__ = {
    #     'schema': 'dbo',
    #     'useexisting': True
    # }
    # __tablename__ = 'CONFIAR-en'

    __table__ = db.Model.metadata.tables['CONFIAR-en']

    @classmethod
    def datatables(cls):
        data = cls.query.all()
        print(data)
        return {'data': data}

    def __repr__(self):
        return '<textRef = {}>'.format(self.text_ref)
