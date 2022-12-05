from validator import Validator
from database import SqlOperation


class PersonService:
    """
        This class contains all the methods used to manage the persons.
    """
    validator = Validator()

    @staticmethod
    def insert_person(name: str, surname: str):
        """
            This method is used to validate the input and call database layer to insert a person into the database.

            :param name: name of the person
            :param surname: surname of the person

            :return: None
        """
        try:
            PersonService.validator.validate_name(name, surname)
        except ValueError as e:
            print(str(e))
        else:
            if SqlOperation.get_person(name, surname) is None:
                SqlOperation.insert_person(name, surname)
            else:
                print("Person %s %s already exists." % (name, surname))
