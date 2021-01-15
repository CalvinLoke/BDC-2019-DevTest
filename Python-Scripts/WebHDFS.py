import requests
import urllib3
import os.path

# Supresses unverified HTTPS warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
main_url = r'https://10.10.0.104:30443/gateway/default/webhdfs/v1/'

def createDirectory(dir_name):

    params = (
        ('op', 'MKDIRS'),
    )

    url = main_url + dir_name
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

    url = main_url + path + '/' + file_name + "?filename=" + file_name
    # url = r'https://10.10.0.104:30443/gateway/default/webhdfs/v1/test_dir/test2.csv'

    # https://example.com/api/upload.json?filename=test.jpeg

    # https://10.10.0.104:30443/gateway/default/webhdfs/v1/


    response = requests.put(url, headers=headers, params=params, verify=False, auth=('admin', 'Password1234'))
    # response = requests.post()

    print(response)


def checkDirectory(folder_name):
    params = (
        ('op', 'liststatus'),
    )

    url = main_url + folder_name + "/"
    # url = 'https://10.10.0.104:30443/gateway/default/webhdfs/v1/test_dir/'
    
    response = requests.get(url, params=params, verify=False, auth=('admin', 'Password1234'))

    print(response.content)

# Main core function
def main():
    while True:
        print("Select option:")
        print("1) Create Directory")
        print("2) Upload file to directory")
        print("3) Check files in directory")
        print("4) Print WebHDFS url")
        print("5) Exit")

        user_input = input("Your option: ")
        user_input.strip() # removes trailing whitespaces

        if user_input == "1":
            dir_name = input("Please enter the desired directory name: ")
            createDirectory(dir_name)
            continue

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
            continue

        elif user_input == "3":
            dir_path = input("Please enter folder name: ")
            checkDirectory(dir_path)
            continue

        elif user_input == "4":
            print(main_url)
            continue

        elif user_input == "5":
            print("Program will now exit")
            exit()

        else:
            print("Input not recognized")
            continue


if __name__ == "__main__":
    main()


