class SqlQuery:
    """
    This class contains all the queries used in the application.
    """
    insert_person = 'INSERT INTO persons(name,surname) VALUES (%s, %s)'

    select_person_id = 'SELECT id FROM persons WHERE name = %s AND surname = %s'

    insert_meeting = 'INSERT INTO meetings(start_date,end_date) VALUES (%s, %s) RETURNING id'

    select_interval_meetings = 'SELECT meetings.start_date, meetings.end_date, persons.name, persons. surname FROM meetings join participants on meetings.id = participants.meeting_id join persons on persons.id = participants.person_id WHERE start_date >= %s AND end_date <= %s'

    insert_participants = 'INSERT INTO participants(person_id,meeting_id) VALUES (%s, %s)'
