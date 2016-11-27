import pyics


class Containers(pyics.Collection):
    path='containers'

    def list(self, *args, **kwargs):
        path = '{0}/{1}/{2}'.format(self.base_url, self.path, 'json')
        resp = self.client.get(url=path, params=kwargs)
        resp.raise_for_status()
        return [self.wrapper_class(item) for item in resp.json()]

    def delete(self, obj_id, *args, **kwargs):
        path = '{0}/{1}/{2}'.format(self.base_url, self.path, obj_id)
        resp = self.client.delete(url=path, params=kwargs)
        resp_raise_for_status()
        return resp.json()

    def status(self, obj_id):
        path = '{0}/{1}/{2}/{3}'.format(
            self.base_url, self.path, obj_id, 'status')
        resp = self.client.get(path)
        resp.raise_for_status()
        return self.wrapper_class(resp.json())

    def show(self, obj_id):
        path = '{0}/{1}/{2}/{3}'.format(
            self.base_url, self.path, obj_id, 'json')
        resp = self.client.get(path)
        resp.raise_for_status()
        return self.wrapper_class(resp.json())

    def start(self, obj_id):
        path = '{0}/{1}/{2}/{3}'.format(
            self.base_url, self.path, obj_id, 'start')
        resp = self.client.post(path)
        resp.raise_for_status()
        return resp.json()

    def stop(self, obj_id, *args, **kwargs):
        path = '{0}/{1}/{2}/{3}'.format(
            self.base_url, self.path, obj_id, 'stop')

        resp = self.client.post(url=path, params=kwargs)
        resp.raise_for_status()
        return resp.json()

    def restart(self, obj_id, *args, **kwargs):
        path = '{0}/{1}/{2}/{3}'.format(
            self.base_url, self.path, obj_id, 'stop')

        resp = self.client.post(url=path, params=kwargs)
        resp.raise_for_status()
        return resp.json()

    def pause(self, obj_id):
        path = '{0}/{1}/{2}/{3}'.format(
            self.base_url, self.path, obj_id, 'pause')
        resp = self.client.post(path)
        resp.raise_for_status()
        return resp.json()

    def unpause(self, obj_id):
        path = '{0}/{1}/{2}/{3}'.format(
            self.base_url, self.path, obj_id, 'unpause')
        resp = self.client.post(path)
        resp.raise_for_status()
        return resp.json()

    def rename(self, obj_id, *args, **kwargs):
        path = '{0}/{1}/{2}/{3}'.format(
            self.base_url, self.path, obj_id, 'rename')

        resp = self.client.post(url=path, params=kwargs)
        resp.raise_for_status()
        return resp.json()
