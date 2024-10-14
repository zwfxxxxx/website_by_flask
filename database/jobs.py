from sqlalchemy import create_engine, text
from config import get_config

mysql_url = get_config().get('mysql_url')


def get_engine():
    return create_engine(mysql_url)


engine = get_engine()


def get_jobs():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        data = result.fetchall()
        print(data)
    return data
