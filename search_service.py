from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import os, dotenv

dotenv.load_dotenv()

def get_search_client() -> SearchClient:
    """
    Initializes and returns an instance of the Azure SearchClient.

    :return: An instance of Azure SearchClient configured with environment variables.
    """
    # search_service_name = os.getenv("SEARCH_SERVICE_NAME")
    # index_name = os.getenv("INDEX_NAME")
    # api_key = os.getenv("API_KEY")
    # endpoint = f"https://{search_service_name}.search.windows.net/"

    search_service_name = os.getenv("SEARCH_SERVICE_NAME_WISE")
    index_name = os.getenv("INDEX_NAME_WISE")
    api_key = os.getenv("API_KEY_WISE")
    endpoint = f"https://{search_service_name}.search.windows.net/"

    credential = AzureKeyCredential(api_key)
    return SearchClient(endpoint=endpoint, index_name=index_name, credential=credential)