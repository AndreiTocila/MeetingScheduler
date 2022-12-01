from datetime import datetime


class Validator:

    @staticmethod
    def validate_name(name: str, surname: str):
        """
        This method is used to validate the name and surname of a person.

        :param name: name of the person
        :param surname: surname of the person

        :return: True if the name and surname are valid, False otherwise
        """
        if not name.isalpha() or not surname.isalpha() or len(name) > 20 or len(surname) > 20 or len(name) < 2 or len(
                surname) < 2:
            raise ValueError("Name and surname must be between 2 and 20 characters long and contain only letters.")

    @staticmethod
    def validate_date(start_date: str, end_date: str):
        """
        This method is used to validate the start and end date of a meeting.

        :param start_date: start date of the meeting
        :param end_date: end date of the meeting

        :return: True if the start and end date are valid, False otherwise
        """
        s_date = None
        e_date = None
        try:
            s_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M")
            e_date = datetime.strptime(end_date, "%Y-%m-%d %H:%M")
        except ValueError:
            raise ValueError("Date format must be YYYY-MM-DD HH:MM.")

        if s_date >= e_date:
            raise ValueError("Start date must be before end date.")

    @staticmethod
    def validate_participants(participants: list):
        """
        This method is used to validate the participants of a meeting.

        :param participants: list of participants

        :return: True if the participants are valid, False otherwise
        """
        if len(participants) < 2:
            raise ValueError("A meeting must have at least 2 participants.")
