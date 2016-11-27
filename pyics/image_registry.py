import pyics


class ImageRegistry(pyics.BaseApi):
    path = 'registry/namespaces'

    def __init__(self, client):
        super(ImageRegistry, self).__init(client)
        self.wrapper_class = type('Namespace', (pyics.Wrapper,) {})

    def is_available(self, namespace):
        resp = self.client.get(
            '{0}/{1}/{2}'.format(self.base_url, self.path, namespace))
        resp.raise_for_status()
        return self.wrapper_class(resp.json())

    def set_namespace(self, namespace):
        resp = self.client.put(
            '{0}/{1}/{2}'.format(self.base_url, self.path, namespace))
        resp.raise_for_status()
        return self.wrapper_class(resp.json())

    def list(self):
        resp = self.client.get('{0}/{1}'.format(self.base_url, self.path))
        resp.raise_for_status()
        return self.wrapper_class(resp.json())
