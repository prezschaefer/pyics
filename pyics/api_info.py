import pyics


class ApiInfo(pyics.BaseApi):
    path = 'containers'

    def get_messages(self):
        resp = self.client.get(
            '{0}/{1}/{2}'.format(self.base_url, self.path, 'messages'))
        resp.raise_for_status()
        return [type(
            'Message', (pyics.Wrapper,), {})(item) for item in resp.json()]

    def get_version(self):
        resp = self.client.get(
            '{0}/{1}/{2}'.format(self.base_url, self.path, 'version'))
        resp.raise_for_status()
        return type('Version', (pyics.Wrapper,), {})(resp.json())
