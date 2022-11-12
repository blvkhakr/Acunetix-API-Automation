import requests
import csv

params = {
    'csvSeparator': 'Comma',
}

response = requests.get('https://acunetix_api_url', params=params, auth=('user_id', 'api_token'))
if response.status_code == 200:
    with open('updated_acunetix_domains.csv', 'w') as file:
        content_lines = csv.writer(file)
        for line in response.iter_lines():
          content_lines.writerow(line.decode('utf-8').split(','))
else:
    print(response.status_code)
