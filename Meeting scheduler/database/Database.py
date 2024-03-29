import psycopg2


class Database:
    """
    This class is used to connect to the database
    """

    @staticmethod
    def get_connection():
        """
        This method is used to get a connection to the database

        :return: connection: psycopg2.connection
        """
        connection = None
        try:
            connection = psycopg2.connect(database="PY_PROJECT",
                                          user="postgres",
                                          password="123456789")
        except psycopg2.OperationalError:
            print("Connection failed to the database.")
            exit(1)

        return connection
