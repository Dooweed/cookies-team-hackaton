import json
import sqlite3
from timeit import default_timer

from flask import request


def db_cache(f):

    def wrapper():
        with sqlite3.connect('cache.sqlite3') as connection:
            url = request.args.get('link', None)

            if url is None:
                raise ValueError('`link` query parameter is not passed')

            start = default_timer()
            cursor = connection.execute("""SELECT data FROM transcripts WHERE url=?;""", (url,))
            data = cursor.fetchone()

            if data is not None:
                print(f'{default_timer() - start:.2f}s: Using cached data')
                return json.loads(data[0])

            result = f()
            data = result if isinstance(result, str) else json.dumps(result)

            connection.execute("""INSERT INTO transcripts VALUES (?, ?)""", (url, data))
            connection.commit()

            print(f'{default_timer() - start:.2f}s: New url, successfully cached new data')
            return result

    return wrapper
