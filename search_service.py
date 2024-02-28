from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from config import get_env_variable

def get_search_client():
    """Initializes and returns the Azure SearchClient."""
    search_service_name = get_env_variable("SEARCH_SERVICE_NAME")
    index_name = get_env_variable("INDEX_NAME")
    api_key = get_env_variable("API_KEY")
    endpoint = f"https://{search_service_name}.search.windows.net/"

    credential = AzureKeyCredential(api_key)
    return SearchClient(endpoint=endpoint, index_name=index_name, credential=credential)