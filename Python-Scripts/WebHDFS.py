import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def createDirectory(dir_name):

    params = (
        ('op', 'MKDIRS'),
    )

    # url = r'https://10.10.0.104:30443/gateway/default/webhdfs/v1/' + dir_name
    url = r'https://10.10.0.104:30443/gateway/default/webhdfs/v1/test_dir'

    response = requests.put(url, params=params, verify=False, auth=('admin', 'Password1234'))
    
    print(response)


def uploadFile():

    headers = {
        'Content-Type': 'application/octet-stream',
    }

    params = (
        ('op', 'create'),
    )

    response = requests.put('https://10.10.0.104:30443/gateway/default/webhdfs/v1/test_dir/test2.csv', headers=headers, params=params, verify=False, auth=('admin', 'Password1234'))

    print(response)


def checkDirectory(path_to_dir):
    params = (
        ('op', 'liststatus'),
    )

    response = requests.get('https://10.10.0.104:30443/gateway/default/webhdfs/v1/test_dir/', params=params, verify=False, auth=('admin', 'Password1234'))

    print(response.content)


checkDirectory("null")
