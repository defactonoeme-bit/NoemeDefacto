import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    name TEXT NOT NULL,
    program TEXT NOT NULL,
    year INTEGER NOT NULL,
    section TEXT NOT NULL
)
''')

cursor.execute("DELETE FROM students")

students = [
    ('2026-00101', 'Ruby Joy Molina', 'BSIT', 3, 'B'),
    ('2026-00102', 'Seth Palec', 'BSIT', 3, 'B'),
    ('2026-00103', 'Sharmaine Palencia', 'BSIT', 3, 'B'),
    ('2026-00104', 'Rochelle Ann Paclibar', 'BSIT', 3, 'B'),
    ('2026-00105', 'Francine Escultura', 'BSIT', 3, 'B'),
    
]

cursor.executemany('''
INSERT INTO students (student_id, name, program, year, section)
VALUES (?, ?, ?, ?, ?)
''', students)

conn.commit()
conn.close()

print("Database created successfully.")