from validator import Validator
from database import SqlOperation


def create_meetings_info(meetings):
    """
    This method is used to create a dictionary containing as keys the meetings and as values the participants.

    :param meetings: list of meetings

    :return: meetings_info: dictionary containing as keys the meetings and as values the participants
    """
    if meetings is None:
        return None
    meetings_info = dict()
    for s_date, e_date, name, surname in meetings:
        key = s_date.strftime("%Y-%m-%d %H:%M") + " - " + e_date.strftime("%Y-%m-%d %H:%M")
        if key not in meetings_info:
            meetings_info[key] = [name + " " + surname]
        else:
            meetings_info[key].append(name + " " + surname)
    else:
        return meetings_info


class MeetingService:
    """
        This class contains all the methods used to manage the meetings.
    """

    validator = Validator()

    @staticmethod
    def insert_meeting(start_date: str, end_date: str, participants: list):
        """
        This method is used to validate the input, then to insert a meeting into the database.

        :param start_date: start date of the meeting
        :param end_date: end date of the meeting
        :param participants: list of participants

        :return: None
        """
        id_list = []
        for name, surname in participants:
            sql_result = SqlOperation.get_person(name, surname)
            if sql_result == "error":
                continue
            else:
                if sql_result is None:
                    print("Person %s %s not found." % (name, surname))
                    continue
                id_list.append(sql_result[0])
        try:
            MeetingService.validator.validate_date(start_date, end_date)
            MeetingService.validator.validate_participants(id_list)
        except ValueError as e:
            print(str(e))
        else:
            SqlOperation.insert_meeting(start_date, end_date, id_list)

    @staticmethod
    def get_meetings(start_date: str, end_date: str):
        """
        This method is used to call database layer to get meetings from the database.

        :param start_date: start date of the meeting
        :param end_date: end date of the meeting

        :return: meetings_info: meetings_info: dictionary containing as keys the meetings and as values the participants / None if error
        """
        try:
            MeetingService.validator.validate_date(start_date, end_date)
        except ValueError as e:
            print(str(e))
        else:
            meetings = SqlOperation.get_interval_meetings(start_date, end_date)
            return create_meetings_info(meetings)

    @staticmethod
    def get_all_meetings():
        """
        This method is used to call database layer to get all meetings from the database.

        :return: meetings_info: dictionary containing as keys the meetings and as values the participants / None if error
        """
        meetings = SqlOperation.get_all_meetings()
        return create_meetings_info(meetings)
