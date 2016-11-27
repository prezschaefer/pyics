import pyics


class Volumes(pyics.Collection):
    path = 'volumes'

    def share(self, obj_id):
        resp = self.client.post(
            '{0}/{1}/{2}'.format(self.base_url, self.path, obj_id))
        resp.raise_for_status()
        return self.wrapper_class(resp.json())
