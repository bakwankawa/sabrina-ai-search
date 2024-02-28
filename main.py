from document_manager import DocumentManager

# The document keys of the documents you want to delete
document_keys = [
    "aHR0cHM6Ly9zYWJyaW5hbGxtLmJsb2IuY29yZS53aW5kb3dzLm5ldC9hbGxrbm93bGVkZ2VzYWJyaW5hLXR4dC9hZGRlZEtub3dsZWRnZV9wZW5kYWZ0YXJhbktLQm1vdG9yMi50eHQ1", 
    "aHR0cHM6Ly9zYWJyaW5hbGxtLmJsb2IuY29yZS53aW5kb3dzLm5ldC9hbGxrbm93bGVkZ2VzYWJyaW5hLXR4dC9hZGRlZEtub3dsZWRnZV9wZW5kYWZ0YXJhbktLQnJlZmluYW5jaW5nMi50eHQ1",
    ]

def main():
    document_manager = DocumentManager()
    document_manager.delete_documents(document_keys)

if __name__ == "__main__":
    main()