import pyics


class Authentication(pyics.BaseApi):
    path = 'tlskey'

    def __init__(self, client):
        super(Authentication, self).__init__(client)
        self.wrapper_class = type('Certificate', (pyics.Wrapper,), {})

    def get_certificate(self):
        resp = self.client.get('{0}/{1}'.format(self.base_url, self.path))
        resp.raise_for_status()
        return self.wrapper_class(resp.json())

    def refresh_certificate(self):
        resp = self.client.put(
            '{0}/{1}/{2}'.format(self.base_url, self.path, 'refresh'))
        resp.raise_for_status()
        return self.wrapper_class(resp.json())
