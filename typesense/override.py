from .api_call import ApiCall


class Override(object):
    def __init__(self, config, collection_name, override_id):
        self.config = config
        self.collection_name = collection_name
        self.override_id = override_id
        self.api_call = ApiCall(config)

    def _endpoint_path(self):
        from .overrides import Overrides
        from .collections import Collections
        return u"{0}/{1}/{2}/{3}".format(Collections.RESOURCE_PATH, self.collection_name, Overrides.RESOURCE_PATH,
                                         self.override_id)

    def retrieve(self):
        return self.api_call.get(self._endpoint_path())

    def delete(self):
        return self.api_call.delete(self._endpoint_path())
