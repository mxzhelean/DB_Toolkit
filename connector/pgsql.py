import psycopg2
import pandas as pd
import Config
from ..util.wrangler import cache_to_file

config = Config('pgsql', ['user', 'password', 'host', 'database'])

@cache_to_file
def get_data(sql_string, *, db_name='test', filename=None, force=False):
    config.load(db_name)
    conn = psycopg2.connect("host={host} dbname={database} user={user} password={password}".format(**config.values))

    colnames = []
    rows = []
    try:
        cur = conn.cursor()
        cur.execute(sql_string)
        colnames = [desc[0] for desc in cur.description]
        rows = cur.fetchall()
    except Exception as e:
        raise e
    conn.close()
    if rows:
        return pd.DataFrame(rows, columns=colnames)
    return None
