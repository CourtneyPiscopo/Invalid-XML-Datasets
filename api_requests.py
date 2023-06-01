import requests
import time

# A class to gather a valid xml file dataset from GitHub using GitHub API.

def simpleGetRequest(url, searchQuery):
    token = 'xxxxx'

    auth_header = {'Authorization': 'token ' + token}

    response = requests.get(url, headers=auth_header)

    if response.status_code:
        return response


def download_url(url):
    print("downloading: ", url)
    # This assumes that the last segment after the '/' represents the file name
    file_name_start_pos = url.rfind("/") + 1
    file_name = url[file_name_start_pos:]

    r = requests.get(url, stream=True)
    if r.status_code == requests.codes.ok:
        with open('valid_xml_new/' + file_name, 'wb') as f:
            for data in r:
                f.write(data)


def getXmlFilesGithub(cnt):
    i = 0

    while (i < cnt):
        response = simpleGetRequest('https://api.github.com/search/code?q=extension:xml', None)


        if response.status_code == 200:
            dict = response.json()

            arr = []
            for i in dict['items']:
                arr.append(i['url'])

            for j in arr:
                response2 = simpleGetRequest(j, None)
                dict2 = response2.json()
                print("Download Link: ", dict2['download_url'])
                download_url(dict2['download_url'])

        else:
            print("Error connecting to API, check username and credentials.")
            print("Status Code: " + str(response.status_code))

        time.sleep(35)

        i = i + 1
