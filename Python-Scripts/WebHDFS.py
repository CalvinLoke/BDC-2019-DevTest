import requests
import urllib3
import os.path

# Supresses unverified HTTPS warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def createDirectory(dir_name):

    params = (
        ('op', 'MKDIRS'),
    )

    url = r'https://10.10.0.104:30443/gateway/default/webhdfs/v1/' + dir_name
    # url = r'https://10.10.0.104:30443/gateway/default/webhdfs/v1/test_dir'

    response = requests.put(url, params=params, verify=False, auth=('admin', 'Password1234'))
    
    print(response)


def uploadFile(path, file_name):

    headers = {
        'Content-Type': 'application/octet-stream',
    }

    params = (
        ('op', 'create'),
    )

    # url = r'https://10.10.0.104:30443/gateway/default/webhdfs/v1/test_dir/test2.csv'
    url = r'https://10.10.0.104:30443/gateway/default/webhdfs/v1/' + path + '/' + file_name

    response = requests.put(url, headers=headers, params=params, verify=False, auth=('admin', 'Password1234'))

    print(response)


def checkDirectory(folder_name):
    params = (
        ('op', 'liststatus'),
    )

    # url = 'https://10.10.0.104:30443/gateway/default/webhdfs/v1/test_dir/'
    url = r'https://10.10.0.104:30443/gateway/default/webhdfs/v1/' + folder_name + "/"
    response = requests.get(url, params=params, verify=False, auth=('admin', 'Password1234'))

    print(response.content)


print("Select option:")
print("1) Create Directory")
print("2) Upload file to directory")
print("3) Check files in directory")
print("4) Exit")

user_input = input("Your option: ")
user_input.strip() # removes trailing whitespaces


if user_input == "1":
    dir_name = input("Please enter the desired directory name: ")
    createDirectory(dir_name)

elif user_input == "2":
    dest_folder = input("Please enter the folder name: ")
    file_name = input("Please enter the file to upload: ")
    # Code block to check if file exists
    if os.path.isfile(file_name):
        print("File exists")
        uploadFile(dest_folder, file_name)
    else:
        print("Warning: File does not exist")
    # uploadFile(dest_folder, file_name)

elif user_input == "3":
    dir_path = input("Please enter folder name: ")
    checkDirectory(dir_path)

elif user_input == "4":
    print("Program will now exit")
    exit()



