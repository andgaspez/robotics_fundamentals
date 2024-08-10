import requests, json

# Replace with your actual access token
access_token = ''

# Set up the headers with the access token
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Make a request to get documents from your library
#response = requests.get('https://api.mendeley.com/documents', headers=headers)

tag_name = 'dance'
response = requests.get(f'https://api.mendeley.com/documents?tag={tag_name}', headers=headers)

# Check if the request was successful
# if response.status_code == 200:
#     documents = response.json()
#     for doc in documents:
#         print(f"Title: {doc['title']}, ID: {doc['id']}")
# else:
#     print(f"Failed to fetch documents: {response.status_code} - {response.text}")

if response.status_code == 200:
    documents = response.json()
    print(json.dumps(documents, indent=2))
    for doc in documents:
        
        authors = doc.get('authors', [])

        author_names = ', '.join([author.get('first_name', '') + ' ' + author.get('last_name', '') for author in authors])

        print(f"Title: {doc['title']}, Authors: {author_names}")
else:
    print(f"Failed to fetch documents with tag {tag_name}: {response.status_code} - {response.text}")
