from .core import Base, engine
from sqlalchemy.orm import sessionmaker
from .statistics import Statistics

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

