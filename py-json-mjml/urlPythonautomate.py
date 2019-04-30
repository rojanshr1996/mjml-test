import requests
import sys

headers = {
    'X-FIGMA-TOKEN': '12406-c44f7edf-3e6d-4d84-8a8e-473d324ae18c',
}

data = sys.argv[1]
url = ('https://api.figma.com/v1/files/'+ data)
response = requests.get(url, headers=headers).json()

# for eachArg in sys.argv:
#     url = ('https://api.figma.com/v1/files/'+ eachArg)
#     response = requests.get(url, headers=headers).json()

print(response)

# To Generate JSON using figma api
# import os
# os.system("curl -H 'X-FIGMA-TOKEN: 12406-c44f7edf-3e6d-4d84-8a8e-473d324ae18c' 'https://api.figma.com/v1/files/cPNiRry51GKqelElGqLt6MLj'")
#
