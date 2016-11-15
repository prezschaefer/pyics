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


import requests

import bmauth


__author__ = 'Mathew Odden'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2016 Mathew Odden'


class Client(requests.Session):

    def __init__(self, username, passwd, space_id):
        super(Client, self).__init__()
        self.space_id = space_id

        def auth():
            return bmauth.auth(username, passwd)

        token = auth()['access_token']

        self.headers.update(
            {'X-Auth-Token': token,
             'X-Auth-Project-Id': space_id})

        self.groups = Groups(self)


class Collection(object):
    base_url = 'https://containers-api.ng.bluemix.net/v3/containers'

    def __init__(self, client):
        self.client = client
        # lookup class object from global scope, or just build one on the fly

        def find_wrapper_cls():
            try:
                return globals()[self.wrapper_class_name]
            except (AttributeError, KeyError):
                return type(self.__class__.__name__[:-1], (Wrapper,), {})

        self.wrapper_class = find_wrapper_cls()

    def list(self):
        resp = self.client.get(self.base_url + self.path)
        resp.raise_for_status()
        return [self.wrapper_class(item) for item in resp.json()]

    def create(self, *args, **kwargs):
        data_map = {}
        for k, v in kwargs.iteritems():
            data_map[unpythonize(k)] = v

        headers = {'Content-Type': 'application/json'}
        resp = self.client.post(
            url='{0}{1}'.format(self.base_url, self.path),
            json=data_map,
            headers=headers)
        resp.raise_for_status()
        return self.wrapper_class(resp.json())

    def show(self, obj_id):
        path = '{0}{1}/{2}'.format(self.base_url, self.path, obj_id)
        resp = self.client.get(path)
        resp.raise_for_status()
        return self.wrapper_class(resp.json())

    def delete(self, obj_id):
        path = '{0}{1}/{2}'.format(self.base_url, self.path, obj_id)
        resp = self.client.delete(path)
        resp.raise_for_status()
        return resp.json()


class Groups(Collection):
    path = '/groups'

    def create(self, *args, **kwargs):
        # NOTE(mrodden): apparently, the API server can't handle
        # boolean type for autorecovery, has to be a string of True/False
        if 'autorecovery' in kwargs:
            normed = str(kwargs['autorecovery']).lower()
            ar_bool = normed in ('yes', 'true', 't', 1)
            kwargs['autorecovery'] = str(ar_bool)
        return super(Groups, self).create(*args, **kwargs)


class Wrapper(object):

    def __init__(self, data):
        self._body = {}
        for k, v in data.iteritems():
            self._body[pythonize(k)] = v

    def __getattr__(self, name):
        if name not in self._body:
            raise AttributeError(
                "'{0}' has no attributes '{1}'".format(self.__class__, name))
        else:
            return self._body[name]

    def __str__(self):
        attrbs = []
        for k, v in self._body.iteritems():
            attrbs.append('{0}={1}'.format(k, v))
        stringified = '<{0} {1}>'.format(
            self.__class__.__name__, ', '.join(attrbs))
        return stringified

    def __repr__(self):
        return str(self)


def pythonize(string):
    """Transforms 'SillyCamelCase' to 'silly_camel_case'"""
    normed = string[0].lower()
    for char in string[1:]:
        if char.isupper():
            normed += '_'
        normed += char.lower()
    return normed


def unpythonize(string):
    """Transforms 'some_variable_name' to 'SomeVariableName'"""
    return string.title().replace('_', '')
