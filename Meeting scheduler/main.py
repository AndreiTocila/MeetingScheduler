from SqlOperation import SqlOperation

# SqlOperation.insert_person('Popescu', 'Ion')
# SqlOperation.insert_person('Ana', 'Maria')
# SqlOperation.insert_person('Smith', 'Andrei')
# SqlOperation.insert_person('Patrat', 'Ionut')
#
# SqlOperation.insert_meeting('2020-01-01 08:00', '2020-01-01 08:30', [('Popescu', 'Ion'), ('Anaa', 'Maria')])
# SqlOperation.insert_meeting('2020-01-03 10:30', '2020-01-03 11:00', [('Smith', 'Andrei'), ('Patrat', 'Ionut')])
# SqlOperation.insert_meeting('2020-01-06 21:15', '2020-01-06 21:30', [('Popescu', 'Ion'), ('Patrat', 'Ionut')])

SqlOperation.select_interval_meetings('2020-01-01 00:00', '2020-01-07 00:00')


