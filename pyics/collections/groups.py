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

    def delete(self, obj_id, *args, **kwargs):
        path = '{0}/{1}/{2}'.format(self.base_url, self.path, obj_id)
        resp = self.client.delete(url=path, params=kwargs)
        resp.raise_for_status()
        return resp.json()
