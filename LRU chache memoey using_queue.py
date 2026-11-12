class LRUCache:

    def __init__(self, cap):
        #code here
        self.cache={}
        self.capacity=cap



    def get(self, key):
        #code here
        if key in self.cache:
            new_key=key
            value_new=self.cache.pop(key)
            new_value={new_key:value_new}
            self.cache={new_key:value_new,**self.cache}
            return value_new 


        else:
            return -1


    def put(self, key, value):
        #code here
        if (len(self.cache)<self.capacity) and (key not in self.cache):
            new_value={key:value}
            self.cache={key:value,**self.cache}##adding element at the first index position


        elif key in self.cache:
            self.cache.pop(key)
            self.cache = {key: value, **self.cache}

        else:
            removed_value=self.cache.popitem()
            new_value={key:value}
            self.cache={key:value,**self.cache}
