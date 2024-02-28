from document_manager import DocumentManager
import yaml

def load_document_keys(yaml_file_path: str) -> list:
    """
    Loads document keys from a YAML file.

    :param yaml_file_path: The path to the YAML file containing the document keys.
    :return: A list of document keys.
    """
    with open(yaml_file_path, 'r') as file:
        data = yaml.safe_load(file)
        return data.get('keys', [])

# The document keys of the documents you want to delete
yaml_file_path = 'document_keys.yaml'
document_keys = load_document_keys(yaml_file_path)

def main() -> None:
    """
    Main function to execute the document deletion process.
    """
    document_manager = DocumentManager()
    document_manager.delete_documents(document_keys)

if __name__ == "__main__":
    main()