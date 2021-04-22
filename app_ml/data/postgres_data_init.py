from sqlalchemy import create_engine, Table, Column, Integer, String, Float, MetaData, ForeignKey, DateTime ,insert
from app_ml.functionalities.constants import POSTGRES_URL
import sqlalchemy as sa

USERS = [
    {'firstname': 'Nikos', 'lastname': 'Vitas'},
    {'firstname': 'Marios', 'lastname': 'Lzi'},
    {'firstname': 'Vaggelis', 'lastname': 'Koutsos'},
    {'firstname': 'Akis', 'lastname': 'Mpacharakis'},
    {'firstname': 'Ntinos', 'lastname': 'Mpriasoulis'},
    {'firstname': 'Tolis', 'lastname': 'Mpriasoulis'},
    {'firstname': 'Kostis', 'lastname': 'Ioannidis'},
    {'firstname': 'Vasilis', 'lastname': 'Tzentebil'},
    {'firstname': 'Koulhs', 'lastname': 'Pizas'},
]

# lower < value <= upper 
PROFILES = [
    {'lower': -1, 'upper': 0.05, 'profile': 'NORMAL'},
    {'lower': 0.05, 'upper': 0.3, 'profile': 'SLIGHTLY AGGRESSIVE'},
    {'lower': 0.3, 'upper': 0.6, 'profile': 'FAIRLY AGGRESSIVE'},
    {'lower': 0.6, 'upper': 0.85, 'profile': 'HIGHLY AGGRESSIVE'},
    {'lower': 0.85, 'upper': 1, 'profile': 'EXTREMELY AGGRESSIVE'}
]

def drop_database():
    engine = create_engine('postgres://postgres:postgres@/postgres')
    conn = engine.connect()
    conn = conn.execution_options(autocommit=False)
    conn.execute('ROLLBACK')
    try:
        conn.execute('DROP DATABASE cars')
    except sa.exc.ProgrammingError as e:
        # Database does not exist
        conn.execute('ROLLBACK')
    except sa.exc.OperationalError as e:
        print(e)
        conn.execute('ROLLBACK')
    conn.close()
    engine.dispose()

def create_database():
    drop_database()
    engine = create_engine('postgres://postgres:postgres@/postgres')
    conn = engine.connect()
    conn.execute('COMMIT')
    conn.execute('CREATE DATABASE cars')
    conn.close()
    engine.dispose()
    print('Postgresql database created successfully')

def create_schema(engine):
    meta = MetaData()
    users = Table(
        'users', meta,
        Column('user_id', Integer, primary_key=True, nullable=False),
        Column('firstname', String(30), nullable=False),
        Column('lastname', String(30), nullable=False)
    )
    routes = Table(
        'routes', meta,
        Column('route_id', String(50), primary_key=True, nullable=False),
        Column('user_id', Integer, ForeignKey('users.user_id'), nullable=False),
        Column('date', DateTime, nullable=False),
        Column('is_active', Integer, nullable=False)
    )
    scores = Table(
        'scores', meta,
        Column('score_id', Integer, primary_key=True, nullable=False),
        Column('route_id', String(50), ForeignKey('routes.route_id'), nullable=False),
        Column('start_time', Float(5), nullable=False),
        Column('end_time', Float(5), nullable=False),
        Column('aggressive_score', Float(2), nullable=False),
        Column('normal_score', Float(2), nullable=False)
    )
    profiles = Table(
        'profiles', meta,
        Column('profile_id', Integer, primary_key=True, nullable=False),
        Column('lower', Float(5), nullable=False),
        Column('upper', Float(5), nullable=False),
        Column('profile', String(50), nullable=False)
    )
    meta.create_all(engine)

def insert_to_users(engine):
    meta = MetaData(engine)
    users = Table('users', meta, autoload=True)
    stmt = insert(users).values(USERS)
    conn = engine.connect()
    conn.execute(stmt)
    conn.execute('COMMIT')
    conn.close()

def insert_to_profiles(engine):
    meta = MetaData(engine)
    profiles = Table('profiles', meta, autoload=True)
    stmt = insert(profiles).values(PROFILES)
    conn = engine.connect()
    conn.execute(stmt)
    conn.execute('COMMIT')
    conn.close()

def main():
    create_database()
    engine = create_engine(POSTGRES_URL)
    create_schema(engine)
    insert_to_users(engine)
    insert_to_profiles(engine)
    engine.dispose()

if __name__ == '__main__':
    main()