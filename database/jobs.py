from sqlalchemy import create_engine, text
from config import get_config

mysql_url = get_config().get('mysql_url')


def get_engine():
    try:
        return create_engine(mysql_url)
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None


engine = get_engine()


def get_job_list():
    if not engine:
        return None
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        data = result.fetchall()
    return data


def get_job_info_by_id(job_id):
    if not engine:
        return None
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :job_id"), {'job_id': job_id})
        data = result.fetchone()
        if not data:
            print("Job not found")
            return None
        job_info = data._asdict()

    return job_info
