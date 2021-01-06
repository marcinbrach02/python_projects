import requests

response = requests.get('http://www.jsystems.pl/')

#400 Bad Request
#401 Unauthorized
#403 Forbidden
#404 Not Faund
#405 Bad Method
print(response.status_code)
print(response.encoding)
print(response.headers)
print(response.text)




