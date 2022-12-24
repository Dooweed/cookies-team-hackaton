import sqlite3
import sys


AVAILABLE_COMMANDS = ['create_tables', 'truncate']

if len(sys.argv) != 2:
    raise ValueError(f'Incorrect query. Please use manage.py followed by one of {AVAILABLE_COMMANDS}')

command = sys.argv[1]

connection = sqlite3.connect('cache.sqlite3')

if command == AVAILABLE_COMMANDS[0]:
    with open('sql/schema.sql', 'r') as file:
        connection.execute(file.read())
elif command == AVAILABLE_COMMANDS[1]:
    connection.execute("""DELETE FROM transcripts""")
else:
    raise ValueError(f'Unknown command {command}. List of available commands: {AVAILABLE_COMMANDS}')

connection.close()
