from validator import Validator
from database import SqlOperation


class PersonService:
    validator = Validator()

    @staticmethod
    def insert_person(name: str, surname: str):
        """
            This method is used to validate the input and call database layer to insert a person into the database.
        """
        try:
            PersonService.validator.validate_name(name, surname)
        except ValueError as e:
            print(str(e))
        else:
            SqlOperation.insert_person(name, surname)
