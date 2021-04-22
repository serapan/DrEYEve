from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgres://postgres:postgres@localhost/cars', convert_unicode=True, echo=False)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.metadata.reflect(engine)
Base.query = db_session.query_property()

################################
#                              #
# user_id, firstname, lastname #
#                              #
################################

class User(Base):
    __table__ = Base.metadata.tables['users']

###########################
#                         #
# route_id, user_id, date #
#                         #
###########################

class Route(Base):
    __table__ = Base.metadata.tables['routes']

############################################################################
#                                                                          #
# score_id, route_id, start_time, end_time, aggressive_score, normal_score #
#                                                                          #
############################################################################

class Score(Base):
    __table__ = Base.metadata.tables['scores']

#########################
#                       #
# lower, upper, profile #
#                       #
#########################

class Profile(Base):
    __table__ = Base.metadata.tables['profiles']