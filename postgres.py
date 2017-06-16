#postgres 4 python utilities
import psycopg2


class Dbmanager:

    def __init__(self, db):
        self.conn = psycopg2.connect(db)
        self.cur = self.conn.cursor()

    @staticmethod
    def as_array(l):
        l2str = ','.join('"{}"'.format(x) for x in l)
        return '{{{}}}'.format(l2str)

    #tupla: idblock, file, begin p, end p
    def create_table_entries(self):
        self.cur.execute("DROP TABLE IF EXISTS csv_tags;")
        self.cur.execute("""
            CREATE TABLE csv_tags ( idblock int,
                file int,
                begin_p int,
                end_p int,
                concept text
            );
        """)

    def new_table_entries(self):
        self.cur.execute("DROP TABLE IF EXISTS ok_tags;")
        self.cur.execute("""
            CREATE TABLE ok_tags AS
                SELECT c.idblock, c.file, c.begin_p, c.end_p,
                        array_agg(concept) as concepts
                FROM csv_tags c
                GROUP BY c.idblock, c.file, c.begin_p, c.end_p
        """)

    def insert_tags(self, idblock, f, begin_p, end_p, concept):
        self.cur.execute('INSERT INTO csv_tags (idblock, file, begin_p, end_p, concept) VALUES (%s, %s, %s, %s, %s)', (idblock, f, begin_p, end_p, concept))

    def dbend(self):
        #commit
        self.conn.commit()
        #close communication with the database
        self.cur.close()
        self.conn.close()


if __name__ == "__main__":
    db = Dbmanager("dbname=trialdb user=postgres password=luisapalma")
    db.create_table_entries()
    db.insert_tags(10, 1, 1, 5, "prova1")
    db.insert_tags(10, 1, 1, 5, "prova2")
    db.insert_tags(12, 1, 6, 10, "prova1")
    db.insert_tags(13, 2, 1, 21, "prova3")
    db.new_table_entries()
    db.dbend()
