import base64
import getpass

import requests

api_endpoint = 'https://login.ng.bluemix.net/UAALoginServerWAR'
oauth_path = '/oauth/token'


def auth(username, password):
    url = api_endpoint + oauth_path

    headers = {'Authorization': 'Basic ' + base64.b64encode('cf:'),
               'Accept': 'application/json'}

    data = {'grant_type': 'password',
            'scope': '',
            'username': username,
            'password': password}

    resp = requests.post(url, headers=headers, data=data)

    resp.raise_for_status()

    return resp.json()


def main():

    username = raw_input('Username:')
    passwd = getpass.getpass('Password:')

    resp = auth(username, passwd)
    print resp


if __name__ == '__main__':
    main()
