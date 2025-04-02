# Rest API Integration AI Agent

Use AI agents to automate the transfer of data from source to target 

## Languages
Python

## Technologies
Ollama
Uses hugging face models

Setup
https://www.w3schools.com/python/module_requests.asp
https://jsonplaceholder.typicode.com/posts
https://mockend.com
https://docs.python.org/3/library/http.client.html

You will be given the details of the target destination

Example

TARGET = https://jsonplaceholder.typicode.com/posts

You will be given the details of the source destination

Example

SOURCE = https://jsonplaceholder.typicode.com/posts

You will be given the http verb to use when retrieving data from the source destination 

You will be given the http verb to use when retrieving data from the target destination 

Example

GET

POST

PUT

DELETE

You will be given each of the fields to map from target to destination. Source will always be on the left of the = sign

Example

Firstname = Name

Lastname = Surname

Email = EmailAddress

The field on the left must transformed to the field on the right of the = sign

The input will be read from the source destination.

Example

An example of the json payload from the target destination 

Example
{

    “Firstname”:”Ash”,
    “Lastname”:”Dhevalall”,
    “Email”:”ash@test.com”
}

The output should convert to a json object and then sent to the target destination. 

An example of the json payload from the source destination 

Example
{
    “Name”:”Ash”,
    “Surname”:”Dhevalall”,
    “EmailAddress”:”ash@test.com”
}

Making GET and POST Requests Using the Python requests Module

In a rush? Here's the Python syntax for making a simple GET and POST request:

GET request

import requests

# The API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

# A GET request to the API
response = requests.get(url)

# Print the response
print(response.json())

POST request

import requests

# The API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Data to be sent
data = {
    "userID": 1,
    "title": "Making a POST request",
    "body": "This is the data we created."
}

# A POST request to the API
response = requests.post(url, json=data)

# Print the response
print(response.json())

You can also pass arguments to a Python GET request. To do this, we must slightly alter the code above. Here’s how the new code looks:

# The API endpoint
url = "https://jsonplaceholder.typicode.com/posts/"

# Adding a payload
payload = {"id": [1, 2, 3], "userId":1}

# A get request to the API
response = requests.get(url, params=payload)

# Print the response
response_json = response.json()

for i in response_json:
    print(i, "\n")

"""
{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
{'userId': 1, 'id': 2, 'title': 'qui est esse', 'body': 'est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla'}
{'userId': 1, 'id': 3, 'title': 'ea molestias quasi exercitationem repellat qui ipsa sit aut', 'body': 'et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut'}
"""

Making a POST request in Python
GET requests allow you to retrieve data; POST requests will enable you to create new data. Let’s take a look at how we can create new data on the JSONPlaceholder server.

# Define new data to create
new_data = {
    "userID": 1,
    "id": 1,
    "title": "Making a POST request",
    "body": "This is the data we created."
}



# The API endpoint to communicate with

url_post = "https://jsonplaceholder.typicode.com/posts"



# A POST request to tthe API

post_response = requests.post(url_post, json=new_data)



# Print the response

post_response_json = post_response.json()

print(post_response_json)



"""

{'userID': 1, 'id': 101, 'title': 'Making a POST request', 'body': 'This is the data we created.'}

"""



Authenticating HTTP requests



Here’s a simple workaround using the Python requests module: 



from requests.auth import HTTPBasicAuth



private_url = "https://api.github.com/user"

github_username = "username"

token = "token"



private_url_response = requests.get(

    url=private_url,

    auth=HTTPBasicAuth(github_username, token)

)



private_url_response.status_code



"""

200

"""



Handling HTTP request errors



For this demonstration, let’s return to the JSONPlaceholder API. We will start by writing some code and then explain what is happening.  



# A deliberate typo is made in the endpoint "postz" instead of "posts"

url = "https://jsonplaceholder.typicode.com/postz"



# Attempt to GET data from provided endpoint

try:

    response = requests.get(url)

    response.raise_for_status()

# If the request fails (404) then print the error.

except requests.exceptions.HTTPError as error:

  print(error)



"""

404 Client Error: Not Found for url: https://jsonplaceholder.typicode.com/postz

"""



Dealing with too many redirects

HTTP status codes with the 3xx format indicate that the client was redirected and must perform some additional actions to complete the request. However, this can occasionally lead to an infinite redirect loop.





Python’s requests module provides the TooManyRedirects object to handle this problem, as follows: 



"""

Note: The code here will not raise an error

but the structure is how you would hand a case where there

are multiple redirects

"""



url = "https://jsonplaceholder.typicode.com/posts"



try:

  response = requests.get(url)

  response.raise_for_status()

except requests.exceptions.TooManyRedirects as error:

  print(error)



Handling HTTP requests connection errors



Here’s how the code would look:  



"""

Note: The code here will not raise an error

but the structure is how you would hand a case where there

is a connection error.

"""



url = "https://jsonplaceholder.typicode.com/posts"



try:

  response = requests.get(url)

except requests.ConnectionError as error:

  print(error)



Handling HTTP requests timeout



When the API server accepts your connection but cannot finish your request within the allowed time, you will get a “timeout error.”

We will demonstrate how to handle this case by setting the timeout parameter in the requests.get() method to an extremely small number; this will raise an error, and we will handle that error using the requests.Timeout object. 



url = "https://jsonplaceholder.typicode.com/posts"



try:

  response = requests.get(url, timeout=0.0001)

except requests.Timeout as error:

  print(error)



Exception types



The following exceptions are raised as appropriate:

exception http.client.HTTPException

The base class of the other exceptions in this module. It is a subclass of Exception.

exception http.client.NotConnected

A subclass of HTTPException.

exception http.client.InvalidURL

A subclass of HTTPException, raised if a port is given and is either non-numeric or empty.

exception http.client.UnknownProtocol

A subclass of HTTPException.

exceptionhttp.client.UnknownTransferEncoding

A subclass of HTTPException.

exceptionhttp.client.UnimplementedFileMode

A subclass of HTTPException.

exception http.client.IncompleteRead

A subclass of HTTPException.

exceptionhttp.client.ImproperConnectionState

A subclass of HTTPException.

exceptionhttp.client.CannotSendRequest

A subclass of ImproperConnectionState.

exceptionhttp.client.CannotSendHeader

A subclass of ImproperConnectionState.

exceptionhttp.client.ResponseNotReady

A subclass of ImproperConnectionState.

exception http.client.BadStatusLine

A subclass of HTTPException. Raised if a server responds with a HTTP status code that we don’t understand.

exception http.client.LineTooLong

A subclass of HTTPException. Raised if an excessively long line is received in the HTTP protocol from the server.

exceptionhttp.client.RemoteDisconnected

A subclass of ConnectionResetError and BadStatusLine. Raised by HTTPConnection.getresponse() when the attempt to read the response results in no data read from the connection, indicating that the remote end has closed the connection.

Added in version 3.5: Previously, BadStatusLine('') was raised.