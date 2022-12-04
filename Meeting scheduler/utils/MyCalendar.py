import re
import os
from icalendar import Calendar, Event
from datetime import datetime
from service import MeetingService, PersonService


class MyCalendar:
    """
        This class contains all the methods used to manage the calendar.
    """

    @staticmethod
    def export_calendar():
        """
        This method is used to export the meetings to a calendar file.

        :return: None
        """
        cal = Calendar()
        cal.add('prodid', '-//PyProject//PyProject//EN')
        cal.add('version', '2.0')

        meetings = MeetingService.get_all_meetings()
        if meetings is None:
            print("Could not export the meetings.")
        elif meetings != "error":
            for date, participants in meetings.items():
                start_date, end_date = date.split(" - ")
                event = Event()
                event.add('dtstart', datetime.strptime(start_date, "%Y-%m-%d %H:%M"))
                event.add('dtend', datetime.strptime(end_date, "%Y-%m-%d %H:%M"))

                for participant in participants:
                    event.add('attendee', participant)

                cal.add_component(event)

            with open(os.path.join("calendars", 'meetings.ics'), 'wb') as file:
                file.write(cal.to_ical())

    @staticmethod
    def import_calendar(path: str):
        """
        This method is used to import a calendar file.

        :param path: path of the calendar file

        :return: None
        """
        with open(path, 'rb') as file:
            cal = Calendar.from_ical(file.read())
            for component in cal.walk():
                if component.name == "VEVENT":
                    start_date = datetime.strftime(component.get('dtstart').dt, "%Y-%m-%d %H:%M")
                    end_date = datetime.strftime(component.get('dtend').dt, "%Y-%m-%d %H:%M")
                    participants = []
                    for attendee in component.get('attendee'):
                        name, surname = re.sub(r'CN=|MAILTO:|@.*', '', attendee).split(" ")
                        PersonService.insert_person(name, surname)
                        participants.append((name, surname))
                    MeetingService.insert_meeting(start_date, end_date, participants)

