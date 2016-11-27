import pyics


class FileShares(pyics.Collection):
    path = 'volumes/fs'

    def get_flavors(self):
        resp = self.client.get(
            '{0}/{1}/{2}'.format(self.base_url, self.path, 'flavors/json'))
        resp.raise_for_status()
        return [type('Flavor', (pyics.Wrapper,), {})(item) for item in resp.json()]
