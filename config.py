import os
import dotenv

dotenv.load_dotenv()

def get_env_variable(name):
    """Fetches environment variable value by name."""
    return os.getenv(name)