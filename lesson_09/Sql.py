from sqlalchemy import create_engine, text


class Sql:

    def __init__(self, url):
        self.db_connection_string = url
        self.db = create_engine(self.db_connection_string)
        self.connection = self.db.connect()

    def select(self):
        """Select в базе. Возвращается все строки и столбцы"""
        connection = self.db.connect()
        result = connection.execute(text("select * from subject where subject_id is not NULL"))
        rows = result.mappings().all()
        connection.close()
        return rows

    def insert(self, subj_id, subj_title):
        """Insert в базе. Добавляет новый предмет, указываются id и название предмета"""
        connection = self.db.connect()
        transaction = connection.begin()

        sql = text(f"insert into subject(subject_id, subject_title) values ({subj_id}, '{subj_title}')")
        connection.execute(sql, {subj_id: subj_title})
        transaction.commit()

        connection.close()

    def update(self, subj_id, subj_title):
        """Update в базе. Обновляет созданный предмет. Можно изменить название предмета по id"""
        connection = self.db.connect()
        transaction = connection.begin()

        sql = text(f"update subject set subject_title = '{subj_title}' where subject_id = {subj_id}")
        connection.execute(sql, {subj_id: subj_title})
        transaction.commit()

        connection.close()

    def delete(self, subj_id):
        """Delete в базе. Удаляет предмет по id"""
        connection = self.db.connect()
        transaction = connection.begin()

        sql = text(f"delete from subject where subject_id = {subj_id}")
        connection.execute(sql, {"subj_id": subj_id})
        transaction.commit()

        connection.close()
