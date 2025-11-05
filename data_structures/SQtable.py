import sqlite3 as sq
from pathlib import Path
# Текущие Недостатки: Класс не имеет методов для чтения данных (SELECT), что делает анализ невозможным.
# Нет обработки ошибок, параметризации запросов и эффективного управления соединениями.
# Рекомендации по Улучшению:
# Добавить методы insert, select, update, delete с параметризацией.
# Реализовать контекстный менеджер для соединений (with statement).
# Добавить типы данных для чисел (REAL, INTEGER) и валидацию.
# Интегрировать с numpy/pandas для продвинутого анализа.
# Производительность: Для больших наборов данных (тысячи записей) SQLite подходит, но для реального времени может потребоваться оптимизация.
class sqtable:

    def __init__(self, table_name, filename, path=None):
        self.table_name = table_name
        if not path:
            path = Path(__file__).parent.parent / 'datasets'
        self.file = Path(path) / (filename + '.db')
        self.file.parent.mkdir(parents=True, exist_ok=True)
        self.con = sq.connect(str(self.file))
        self.con.execute(f'''CREATE TABLE IF NOT EXISTS {self.table_name}
                         (id INTEGER PRIMARY KEY AUTOINCREMENT);''')
        self.con.commit()

    def _sqcommand(self, command=''):
        self.con.execute(command)
        self.con.commit()
        return None

    def delete_table(self, delfile=False):
         self.con.execute(f'DROP TABLE {self.table_name}')
         self.con.commit()
         if self.file.exists() and delfile:
             self.file.unlink()

    def sqinsert(self, where_add, what_add):
        if isinstance(where_add, str):
            where_add = [where_add]
        columns = ', '.join(where_add)
        placeholders = ', '.join(['?'] * len(where_add))
        sql = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        self.con.executemany(sql, what_add)
        self.con.commit()
        return None
    
    def sqreading(self):
        self._sqcommand(f'SELECT * FROM {self.table_name}')

    def sqaddcolumn(self, colname, column_type="TEXT"):
        cursor = self.con.cursor()
        cursor.execute(f"PRAGMA table_info({self.table_name})")
        columns = [row[1] for row in cursor.fetchall()]
        if colname not in columns:
            self.con.execute(f'''ALTER TABLE {self.table_name}
                                ADD COLUMN {colname} {column_type};''')
        self.con.commit()
        return None
