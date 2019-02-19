import json


class AbstractJSONEncoder(object):

    def decodeJson(self):
        pass


class FilterJSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, AbstractJSONEncoder):
            return obj.decodeJson()
        return json.JSONEncoder.default(self, obj)
