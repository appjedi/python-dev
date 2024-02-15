from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload
connection_string = "mysql+mysqlconnector://root:Jedi2023@127.0.0.1:3306/dev"
engine = create_engine(connection_string, echo=True)

Base = declarative_base()

# Our User object, mapped to the 'users' table
class User(Base):
    __tablename__ = 'users'

    # Every SQLAlchemy table should have a primary key named 'id'
    id = Column(Integer, primary_key=True)

    username = Column(String)
    password = Column(String)
    role_id = Column(Integer)
    status = Column(Integer)

    # Lets us print out a user object conveniently.
    def __repr__(self):
       return "<User(name='%s', fullname='%s', password'%s')>" % (
                               self.username, self.username, self.password)
    
Session = sessionmaker(bind=engine)
session = Session()

#ed_user = User(username='alchemy', password='Test1234', role_id=1, status=1)
#session.add(ed_user)
#session.commit()

#users = session.query(User).filter(User.id==1).update({"role_id":1})
#delUser =  session.query(User).filter(User.id==8).delete()
def getAllUsers():
    users = session.query(User).aluserl()

    list=[]
    for user in users:
        list.append({'username':user.username, 'roleId':user.role_id})

    return list
#users.role_id=2



#print(users)