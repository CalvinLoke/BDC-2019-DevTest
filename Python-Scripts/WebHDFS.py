import requests
import urllib3
import os.path
import json


# Supresses unverified HTTPS warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
main_url = r'https://10.10.0.104:30443/gateway/default/webhdfs/v1/'


def createDirectory(dir_name):
    params = ( ('op', 'MKDIRS'), )
    url = main_url + dir_name

    try: 
        response = requests.put(url, params=params, verify=False, auth=('admin', 'Password1234'))
        if response.status_code == 200:
            print("HTTP Code 200:")
            print("Directory created successfully")
            print(response.text)
            print("=======================================================")
        
    except Exception as e:
        print("An error has occured, directory failed to create")
        print(response.text)
        print("Error message:")
        print(e)        
        print("=======================================================")


def uploadFile(path, file_name):
    headers = {
        'Content-Type': 'application/octet-stream',
        'Connection': 'keep-alive'
    }
    params = ( ('op', 'create'), )
    url = main_url + path + "/" + file_name

    try:    
        response = requests.put(url, headers=headers, params = params, verify=False, data=open(file_name,'rb'), auth=('admin', 'Password1234'))
        if response.status_code == 201:
            print("HTTP Code 201:")
            print("File Uploaded successfully")
            print(response.text)
            print("=======================================================")

    except Exception as e:
        print("An error has occured, file not uploaded.")
        print("Error message:")
        print(e)
        print("=======================================================")


def rootDirectory():
    params = ( ('op', 'liststatus'),)
    url = main_url
    try:
        response = requests.get(url, params=params, verify=False, auth=('admin', 'Password1234'))
        pretty_json = json.loads(response.text)
        print(json.dumps(pretty_json, indent=2))

    except Exception as e:
        print("An error has occured.")
        print("Error message:")
        print(e)
        print("=======================================================")

        
def checkDirectory(folder_name):
    params = ( ('op', 'liststatus'),)
    url = main_url + folder_name + "/"
    try:
        response = requests.get(url, params=params, verify=False, auth=('admin', 'Password1234'))
        pretty_json = json.loads(response.text)
        print(json.dumps(pretty_json, indent=2))

    except Exception as e:
        print("An error has occured.")
        print("Error message:")
        print(e)
        print("=======================================================")


def readFile(folder_name, file_name):
    params = ( ('op', 'open'), )
    url = main_url + folder_name + "/" + file_name
    try:
        response = requests.get(url, params=params, verify=False, auth=('admin', 'Password1234'))
        print("File content: ")
        print(response.text)

    except Exception as e:
        print("An error has occured.")
        print("Error message:")
        print(e)        
        print("=======================================================")
    

# Main core function
def main():
    while True:
        print("=======================================================")
        print("Select option:")
        print("1) Create Directory")
        print("2) Upload file to directory")
        print("3) List files in root directory")
        print("4) Check files in target directory")
        print("5) Read file from directory")
        print("6) Print WebHDFS url")
        print("7) Exit")
        print("=======================================================")

        user_input = input("Your option: ")
        user_input.strip() # removes trailing whitespaces

        if user_input == "1":
            dir_name = input("Please enter the desired directory name: ")
            createDirectory(dir_name)
            continue

        elif user_input == "2":
            dest_folder = input("Please enter the folder name: ")
            file_name = input("Please enter the file to upload: ")
            print("Checking if file exists in current directory...")
            # Code block to check if file exists
            if os.path.isfile(file_name):
                print("\rFile exists")
                uploadFile(dest_folder, file_name)
            else:
                print("\rWarning: File does not exist")
            # uploadFile(dest_folder, file_name)
            continue

        elif user_input == "3":
            rootDirectory()
            continue

        elif user_input == "4":
            dir_path = input("Please enter folder name: ")
            checkDirectory(dir_path)
            continue
        
        elif user_input == "5":
            dir_path = input("Please enter folder name: ")
            file_name = input("Please enter the file name: ")
            readFile(dir_path, file_name)
            continue

        elif user_input == "6":
            print(main_url)
            continue

        elif user_input == "7":
            print("Program will now exit")
            exit()

        else:
            print("Input not recognized")
            continue


if __name__ == "__main__":
    main()


