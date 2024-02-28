from search_service import get_search_client

class DocumentManager:
    def __init__(self) -> None:
        """
        Initializes the DocumentManager with a SearchClient instance.
        """
        self.client = get_search_client()

    def delete_documents(self, document_keys: list) -> None:
        """
        Deletes documents by keys from the Azure Search index.

        :param document_keys: A list of document keys to be deleted.
        """
        delete_actions = [
            {"@search.action": "delete", "metadata_storage_path": key}
            for key in document_keys
        ]
        self.client.delete_documents(documents=delete_actions)
        print("Documents deleted successfully.")