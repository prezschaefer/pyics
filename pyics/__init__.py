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

    def list(self):
        resp = self.client.get(self.base_url + self.path)
        resp.raise_for_status()
        return resp.json()

    def create(self, *args, **kwargs):
        data_map = {}
        for k, v in kwargs.iteritems():
            if '_' in k:
                data_map[k.title().replace('_', '')] = v
            else:
                data_map[k.title()] = v

        print data_map

        headers = {'Content-Type': 'application/json'}
        resp = self.client.post(
            url='{0}{1}'.format(self.base_url, self.path),
            json=data_map,
            headers=headers)
        resp.raise_for_status()
        return resp.json()

    def show(self, obj_id):
        path = '{0}{1}/{2}'.format(self.base_url, self.path, obj_id)
        resp = self.client.get(path)
        resp.raise_for_status()
        return resp.json()

    def delete(self, obj_id):
        path = '{0}{1}/{2}'.format(self.base_url, self.path, obj_id)
        resp = self.client.delete(path)
        resp.raise_for_status()
        return resp


class Groups(Collection):
    path = '/groups'

    def create(self, *args, **kwargs):
        # NOTE(mrodden): apparently, the API server can't handle
        # boolean type for autorecovery, has to be a string of True/False
        if 'autorecovery' in kwargs:
            normed = str(kwargs['autorecovery']).lower()
            ar_bool = normed in ('yes', 'true', 't', 1)
            kwargs['autorecovery'] = str(ar_bool)
        super(Groups, self).create(*args, **kwargs)
