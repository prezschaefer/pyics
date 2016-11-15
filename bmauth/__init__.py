# Copyright 2016 Mathew Odden
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


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
