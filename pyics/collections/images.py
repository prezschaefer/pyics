import pyics


class Images(pyics.Collection):
    path = 'images'

    def create(self, *args, **kwargs):
        path = '{0}/{1}'.format(self.base_url, 'build')
        data_header = {'Content-Type': 'multipart/form-data')
        param_map = {}
        # NOTE(cjschaef): remove the 'file' and add it to formdata
        form_map = {'file': kwargs.pop('file')}

        for k,v in kwargs:
            param_map[k] = v

        resp = self.client.post(
            url=path, headers=data_header, params=param_map, data=form_map)
        resp.raise_for_status()
        return resp.json()
