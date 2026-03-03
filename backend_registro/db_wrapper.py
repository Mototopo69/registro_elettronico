import pymysql

class DBWrapper:
    def __init__(self):
        # Modifica questi parametri con le tue credenziali MySQL
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'tua_password_mysql'
        self.db = 'registro_db'

    def get_connection(self):
        return pymysql.connect(
            host=self.host, 
            user=self.user, 
            password=self.password, 
            database=self.db, 
            cursorclass=pymysql.cursors.DictCursor
        )

    def inserisci_voto(self, studente, materia, voto):
        connection = self.get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO voti (studente, materia, voto) VALUES (%s, %s, %s)"
                cursor.execute(sql, (studente, materia, voto))
            connection.commit()
        finally:
            connection.close()

    def get_tutti_voti(self):
        connection = self.get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM voti"
                cursor.execute(sql)
                return cursor.fetchall()
        finally:
            connection.close()

    def get_voti_studente(self, studente):
        connection = self.get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM voti WHERE studente = %s"
                cursor.execute(sql, (studente,))
                return cursor.fetchall()
        finally:
            connection.close()