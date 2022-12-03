import psycopg2

from .Database import Database
from .SqlQuery import SqlQuery


class SqlOperation:
    """
    This class contains all the sql operations used in the application.
    """
    connection = Database.get_connection()

    @staticmethod
    def insert_person(name: str, surname: str):
        """
        This method is used to insert a person into the database.

        :param name: name of the person
        :param surname: surname of the person

        :return: None
        """
        try:
            cursor = SqlOperation.connection.cursor()
            cursor.execute(SqlQuery.insert_person, (name, surname))
            SqlOperation.connection.commit()
            print("Person %s %s inserted." % (name, surname))
        except psycopg2.Error:
            print("Error while inserting person.")
            SqlOperation.connection.rollback()

    @staticmethod
    def get_person(name: str, surname:str):
        """
        This method is used to get a person's id from the database.

        :param name: name of the person
        :param surname: surname of the person
/'
        :return: person: tuple / None if person not found / "error" if error
        """
        try:
            cursor = SqlOperation.connection.cursor()
            cursor.execute(SqlQuery.select_person_id, (name, surname))
            SqlOperation.connection.commit()
            person = cursor.fetchone()
            return person
        except psycopg2.Error:
            print("Error while selecting person.")
            SqlOperation.connection.rollback()
            return "error"

    @staticmethod
    def insert_meeting(start_date: str, end_date: str, participants: list):
        """
        This method is used to insert a meeting into the database.

        :param start_date: start date of the meeting
        :param end_date: end date of the meeting
        :param participants: list of participants

        :return: None
        """
        cursor = SqlOperation.connection.cursor()
        try:
            cursor.execute(SqlQuery.insert_meeting, (start_date, end_date))
            SqlOperation.connection.commit()
            meeting_id = cursor.fetchone()[0]
            SqlOperation.insert_participants(meeting_id, participants)
            print("Meeting inserted.")
        except psycopg2.Error:
            print("Error while inserting meeting.")
            SqlOperation.connection.rollback()

    @staticmethod
    def insert_participants(meeting_id, id_list):
        """
        This method is used to insert participants into the database.

        :param meeting_id: id of the meeting
        :param id_list: list of participants

        :return: None
        """
        cursor = SqlOperation.connection.cursor()
        try:
            for person_id in id_list:
                cursor.execute(SqlQuery.insert_participants, (person_id, meeting_id))
            SqlOperation.connection.commit()
        except psycopg2.Error:
            print("Error while inserting participants.")
            SqlOperation.connection.rollback()

    @staticmethod
    def get_interval_meetings(start_date, end_date):
        """
        This method is used to select all the meetings from a given interval and print them.

        :param start_date: start date of the interval
        :param end_date: end date of the interval

        :return: meetings: list of meetings / None if no meetings found / "error" if error
        """
        cursor = SqlOperation.connection.cursor()
        try:
            cursor.execute(SqlQuery.select_interval_meetings, (start_date, end_date))
            SqlOperation.connection.commit()
            meetings = cursor.fetchall()
            return meetings
        except psycopg2.Error:
            print("Error while selecting meetings.")
            SqlOperation.connection.rollback()
            return "error"

    @staticmethod
    def get_all_meetings():
        """
        This method is used to select all the meetings.

        :return: meetings: list of meetings / None if no meetings found / "error" if error
        """
        cursor = SqlOperation.connection.cursor()
        try:
            cursor.execute(SqlQuery.select_all_meetings)
            SqlOperation.connection.commit()
            meetings = cursor.fetchall()
            return meetings
        except psycopg2.Error:
            print("Error while selecting meetings.")
            SqlOperation.connection.rollback()
            return "error"
