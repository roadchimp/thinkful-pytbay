from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float

engine = create_engine('postgresql://action:action@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Item(Base):
  __tablename__ = "items"
  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  description = Column(String)
  start_time = Column(DateTime, default=datetime.utcnow)
 
class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True)
  username = Column(String, nullable=False)
  password = Column(String, nullable=False)

class Bid(Base):
  __tablename__ = "bids"
  id = Column(Integer, primary_key=True)
  price = Column(Float, nullable=False)
  
Base.metadata.create_all(engine)

#creates a user
# beyonce = User()
# beyonce.username = "bknowles"
# beyonce.password = "crazyinlove"
# session.add(beyonce)
# session.commit()

# Returns a list of all of the user objects
session.query(User).all() # Returns a list of all of the user objects

# Returns the first user
session.query(User).first()

# Finds the user with the primary key equal to 1
session.query(User).get(1)

# Returns a list of all of the usernames in ascending order
session.query(User.username).order_by(User.username).all()

# Returns the description of all of the basesballs
session.query(Item.description).filter(Item.name == "baseball").all()

# Return the item id and description for all baseballs which were created in the past.  Remember to import the datetime object: from datetime import datetime
session.query(Item.id, Item.description).filter(Item.name == "baseball", Item.start_time < datetime.utcnow()).all()