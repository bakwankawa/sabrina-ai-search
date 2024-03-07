from search_service import get_search_client

def search_documents(user_query: str):
    # Get the Azure SearchClient instance
    search_client = get_search_client()
    
    # Perform the search, specifying the top parameter to limit results
    results = search_client.search(search_text=user_query, top=1)

    # Process and display the results
    for result in results:
        # Assuming you want to print out a specific field from the result
        # You should replace 'field_name' with the actual name of the field you want to display
        print(result["content"])

# Example usage
if __name__ == "__main__":
    user_query = "gagal login brimo"
    search_documents(user_query)
