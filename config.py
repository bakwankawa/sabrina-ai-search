import os
import dotenv

dotenv.load_dotenv()

def get_env_variable(name: str) -> str:
    """
    Fetches the value of an environment variable.

    :param name: The name of the environment variable to fetch.
    :return: The value of the specified environment variable as a string.
    """
    return os.getenv(name)