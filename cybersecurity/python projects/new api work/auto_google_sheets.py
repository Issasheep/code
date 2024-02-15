import requests
# get the link to the google sheets api
link = 'https://www.googleapis.com/auth/spreadsheets'
# send a get request to the google sheets api
response = requests.get(link)
# print the response status code
print (response.status_code) 
#link response to the google sheets api
response = requests.get('jordan@signin-database-414023.iam.gserviceaccount.com')
print (response.status_code)