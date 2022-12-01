import psycopg2

from .Database import Database
from .SqlQuery import SqlQuery
from validator import Validator


class SqlOperation:
    """
    This class contains all the sql operations used in the application.
    """
    connection = Database.get_connection()
    validator = Validator()

    @staticmethod
    def insert_person(name: str, surname: str):
        """
        This method is used to validate the input, then insert a person into the database.

        :param name: name of the person
        :param surname: surname of the person

        :return: None
        """
        try:
            SqlOperation.validator.validate_name(name, surname)

            cursor = SqlOperation.connection.cursor()
            cursor.execute(SqlQuery.insert_person, (name, surname))
            SqlOperation.connection.commit()
        except ValueError as e:
            print(str(e))
        except psycopg2.Error:
            print("Error while inserting person.")
            SqlOperation.connection.rollback()

    @staticmethod
    def insert_meeting(start_date: str, end_date: str, participants: list):
        """
        This method is used to validate the input, then to insert a meeting into the database.

        :param start_date: start date of the meeting
        :param end_date: end date of the meeting
        :param participants: list of participants

        :return: None
        """
        cursor = SqlOperation.connection.cursor()
        id_list = []

        for name, surname in participants:
            try:
                cursor.execute(SqlQuery.select_person_id, (name, surname))
            except psycopg2.Error:
                print("Error while selecting person id.")
                continue
            else:
                if cursor.rowcount == 0:
                    print("Person %s %s not found." % (name, surname))
                    continue
                id_list.append(cursor.fetchone()[0])

        try:
            SqlOperation.validator.validate_date(start_date, end_date)
            SqlOperation.validator.validate_participants(id_list)

            cursor.execute(SqlQuery.insert_meeting, (start_date, end_date))
            SqlOperation.connection.commit()
            meeting_id = cursor.fetchone()[0]
            SqlOperation.insert_participants(meeting_id, id_list)
        except ValueError as e:
            print(str(e))
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
    def select_interval_meetings(start_date, end_date):
        """
        This method is used to select all the meetings from a given interval and print them.

        :param start_date: start date of the interval
        :param end_date: end date of the interval

        :return: None
        """
        cursor = SqlOperation.connection.cursor()
        meetings_info = dict()
        try:
            cursor.execute(SqlQuery.select_interval_meetings, (start_date, end_date))
            SqlOperation.connection.commit()
            meetings = cursor.fetchall()
            for s_date, e_date, name, surname in meetings:
                key = s_date.strftime("%Y-%m-%d %H:%M") + " - " + e_date.strftime("%Y-%m-%d %H:%M")
                if key not in meetings_info:
                    meetings_info[key] = [name+" "+surname]
                else:
                    meetings_info[key].append(name+" "+surname)
            else:
                if len(meetings_info) == 0:
                    print("No meetings found.")
                else:
                    print(meetings_info)
        except psycopg2.Error:
            print("Error while selecting meetings.")
            SqlOperation.connection.rollback()


