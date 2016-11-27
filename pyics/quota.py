import pyics


class Quota(pyics.BaseApi):
    path = 'containers'

    def show_usage(self):
        resp = self.client.get(
            '{0}/{1}/{2}'.format(self.base_url, self.path, 'usage'))
        resp.raise_for_status()
        return type('Usage', (pyics.Wrapper,), {})(resp.json())

    def show(self):
        resp = self.client.get(
            '{0}/{1}/{2}'.format(self.base_url, self.path, 'quota'))
        resp.raise_for_status()
        return self.wrapper_class(resp.json())

    def update(self, *args, **kwargs):
        path = '{0}/{1}/{2}'.format(self.base_url, self.path, 'quota'))
        data_map = {}
        for k, v in kwargs.iteritems():
            data_map[pyics.unpythonize(k)] = v

        resp = self.client.put(
            url=path, headers=self.json_header, json=data_map)
        resp.raise_for_status()
        return resp.json()
