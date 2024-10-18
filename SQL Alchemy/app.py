from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

Base = declarative_base()

class Person(Base):
    #table name
    __tablename__ = "person"

    #columns
    id = Column(Integer, primary_key = True)
    name = Column(String)
    age = Column(Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"

engine = create_engine("sqlite:///mydb.db", echo = True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()

#inserting
# Azar = Person("Azarudeen",23)
# session.add(Azar)
# session.commit()

# Query all users
# users = session.query(Person).all()
# for user in users:
#     print(user)

# # Query a single user by primary key
# user = session.query(Person).get(1)
# print(user)


#update
# Retrieve the user
# user = session.query(Person).get(3)
# user.age = 26

# # Commit the update
# session.commit()

# Retrieve the user
user = session.query(Person).get(1)

# Delete the user
session.delete(user)

# Commit the transaction
session.commit()
