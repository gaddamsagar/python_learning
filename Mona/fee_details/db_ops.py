import sqlite3
import config
from pandas import read_csv
from datetime import datetime


class DbOperations():
    def __init__(self):
        self.conn = sqlite3.connect(config.DB_NAME)
        self.create_tables()
        # self.insert_csv_into_tables()

    def create_tables(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS STUDENT_DETAILS (
                     HALL_TICKET CHAR(20) PRIMARY KEY     NOT NULL,
                     NAME           TEXT    NOT NULL,
                     DEPARTMENT        CHAR(50),
                     COURSE        CHAR(50),
                     YEAR           INT NOT NULL,
                     SEMESTER       INT NOT NULL
                     );''')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS PAYMENT_DETAILS (                     
                     YEAR           INT      NOT NULL,
                     SEMESTER       INT NOT NULL,
                     DEPARTMENT        CHAR(50),
                     COURSE        CHAR(50),
                     FEE INT NOT NULL
                     );''')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS PAYMENT_HISTORY (
                     HALL_TICKET CHAR(20)     NOT NULL,
                     NAME           TEXT    NOT NULL,
                     DEPARTMENT        CHAR(50),
                     COURSE        CHAR(50),
                     YEAR           INT NOT NULL,
                     SEMESTER       INT NOT NULL,
                     PAID INT NOT NULL,
                     PAID_ON DATETIME NOT NULL
                     );''')

    def insert_csv_into_tables(self):
        read_csv('PAYMENT_DETAILS.csv').to_sql('PAYMENT_DETAILS', self.conn, if_exists='replace', index=False)
        read_csv('STUDENT_DETAILS.csv').to_sql('STUDENT_DETAILS', self.conn, if_exists='replace', index=False)
        read_csv('PAYMENT_HISTORY.csv').to_sql('PAYMENT_HISTORY', self.conn, if_exists='replace', index=False)

    def get_student_details(self, hall_ticket_number):
        cursor = self.conn.execute("select * from STUDENT_DETAILS where hall_ticket = '{0}'".format(hall_ticket_number))
        return cursor.fetchall()

    def get_fee_details_for_semester(self, year, semester, course, department):
        cursor = self.conn.execute("""select FEE from PAYMENT_DETAILS where COURSE = '{0}' and 
                                            YEAR = {1} and 
                                            SEMESTER = {2} and
                                            DEPARTMENT = '{3}'""".format(course, year, semester, department))
        return cursor.fetchall()

    def get_fee_paid_for_semester(self, hall_ticket, year, semester, course, department):
        query = """select PAID, PAID_ON from PAYMENT_HISTORY where COURSE = '{0}' and 
                                            YEAR = {1} and 
                                            SEMESTER = {2} and
                                            DEPARTMENT = '{3}' and
                                            HALL_TICKET = '{4}'""".format(course, year, semester, department, hall_ticket)
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def insert_into_payment_history(self, hall_ticket, year, semester, course, department, fee, name):
        self.conn.execute("""insert into PAYMENT_HISTORY values ('{0}','{1}','{2}','{3}',{4},{5},{6},'{7}')""".format(
            hall_ticket, name, department, course, year, semester, fee, datetime.now().strftime("%b-%d-%Y")))
        self.conn.commit()


if __name__ == "__main__":
    obj = DbOperations()
