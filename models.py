import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

conn = sa.create_engine('sqlite:///lindylisttools.db')

Base = declarative_base()

class Band(Base):
    __tablename__ = 'bands'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    url = sa.Column(sa.String)
    # def __init__(self, name, url):
    #     self.name = name
    #     self.url = url
    def __repr__(self):
        return "<Band(id = '{}', name = '{}', url = '{}')>".format(self.id, self.name, self.url)

Base.metadata.create_all(conn)

Session = sessionmaker(bind=conn)
session = Session()

