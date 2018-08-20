import requests
from io import StringIO
r = requests.get('https://www.doviz.com/api/v1/currencies/USD/latest')
data = r.json()
selling = data['selling']
name = data['name']
selling = str(selling)
print("bir "  + name + " " + selling + " Türk Lirası")