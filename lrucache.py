from collections import OrderedDict


class lrucache:
    def __init__(self, size):
        super().__init__()
        self.cache = OrderedDict
        self.size = size

    def put(self, key, value):
        if self.get(key) == -1:
            if len(self.cache) < self.size:
                self.cache[key] = value
            else:
                self.cache.popitem(last=False)
                self.cache[key] = value
        else:
            self.cache[key] = value

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            val = self.cache[key]
        else:
            val = -1
        return val

    def get_cache(self):
        return self.cache
