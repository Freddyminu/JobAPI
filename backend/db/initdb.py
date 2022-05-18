import sqlite3

connection = sqlite3.connect("database.db")


connection.executescript(
    """
    DROP TABLE IF EXISTS Jobs;

    CREATE TABLE Jobs (
        id INTEGER PRIMARY KEY NOT NULL,
        title TEXT NOT NULL,
        apply_url TEXT NOT NULL,
        department TEXT NOT NULL,
        location TEXT NOT NULL,
        description TEXT NOT NULL,
        created_on TEXT NOT NULL
    );
    """
)
print("Table created successfully")

connection.commit()
connection.close()
