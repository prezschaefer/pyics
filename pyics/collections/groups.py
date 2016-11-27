import pyics


class Groups(pyics.Collection):
    path = 'containers/groups'

    def list(self):
        resp = self.client.get('{0}{1}'.format(self.base_url, self.path))
        resp.raise_for_status()
        return [self.wrapper_class(item) for item in resp.json()]

    def create(self, *args, **kwargs):
        # NOTE(mrodden): apparently, the API server can't handle
        # boolean type for autorecovery, has to be a string of True/False
        if 'autorecovery' in kwargs:
            normed = str(kwargs['autorecovery']).lower()
            ar_bool = normed in ('yes', 'true', 't', 1)
            kwargs['autorecovery'] = str(ar_bool)
        return super(Groups, self).create(*args, **kwargs)

    def show(self, obj_id):
        # NOTE(cjschaef): the show for groups does not append 'json' at the
        # end of the path like the other collections do
        resp = self.client.get(
            '{0}/{1}/{2}'.format(self.base_url, self.path, obj_id)
        resp.raise_for_status()
        return self.wrapper_class(resp.json())        

    def delete(self, obj_id, *args, **kwargs):
        path = '{0}/{1}/{2}'.format(self.base_url, self.path, obj_id)
        resp = self.client.delete(url=path, params=kwargs)
        resp.raise_for_status()
        return resp.json()

    def update(self, obj_id, *args, **kwargs):
        path = '{0}/{1}/{2}'.format(self.base_url, self.path, obj_id)
        data_map = {}
        for k, v in kwargs:
            data_map[pyics.unpythonize(k)] = v

        resp = self.client.patch(
            url=path, headers=self.json_header, json=data_map)
        resp.raise_for_status()
        return resp.json()

    def map_route(self, obj_id, *args, **kwargs):
        path = '{0}/{1}/{2}/{3}'.format(
            self.base_url, self.path, obj_id, 'maproute')
        data_map = {}
        for k, v in kwargs:
            data_map[pyics.unpythonize(k)] = v

        resp = self.client.post(
            url=path, headers=self.json_header, json=data_map)
        resp.raise_for_status()
        return type('MapStatus', (pyics.Wrapper,), {})(resp.json())

    def unmap_route(self, obj_id, *args, **kwargs):
        path = '{0}/{1}/{2}/{3}'.format(
            self.base_url, self.path, obj_id, 'unmaproute')
        data_map = {}
        for k,v in kwargs:
            data_map[pyics.unpythonize(k)] = v

        resp = self.client.post(
            url=path, headers=self.json_header, json=data_map)
        resp.raise_for_status()
        return type('MapStatus', (pyics.Wrapper,), {})(resp.json())
