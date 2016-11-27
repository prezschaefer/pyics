import pyics

class IpAddresses(pyics.BaseApi):
    path = 'containers'
    fip_path = 'floating_ips'
    suffix_count = 2

    def list(self, *args, **kwargs):
        path = '{0}/{1}/{2}'.format(self.base_url, self.path, self.fip_path))

        resp = self.client.get(url=path, params=kwargs)
        resp.raise_for_status()
        return [self.wrapper_class(item) for item in resp.json()]

    def bind(self, obj_id, ip):
        resp = self.client.post(
            '{0}/{1}/{2}/{3}/{4}'.format(self.base_url, self.path, obj_id,
            self.fip_path, ip, 'bind'))
        resp.raise_for_status()
        return resp.json()

    def unbind(self, obj_id, ip):
        resp = self.client.post(
            '{0}/{1}/{2}/{3}/{4}'.format(self.base_url, self.path, obj_id,
            self.fip_path, ip, 'unbind'))
        resp.raise_for_status()
        return resp.json()

    def request(self):
        resp = self.client.post(
            '{0}/{1}/{2}/{3}'.format(self.base_url, self.path, self.fip_path,
            'request'))
        resp.raise_for_status()
        return resp.json()

    def release(self, ip):
        resp = self.client.post(
            '{0}/{1}/{2}/{3}/{4}'.format(self.base_url, self.path,
            self.fip_path, ip, 'release'))
        resp.raise_for_status()
        return resp.json()
