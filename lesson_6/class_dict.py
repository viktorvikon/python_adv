class MyDict:

    def __init__(self, *args):
        if args is None:
            self._dict = {}
        else:
            self._dict = {k: v for k, v in args}

    def __getitem__(self, index):
        return self._dict[index]

    def __setitem__(self, index, value):
        self._dict[index] = value

    def set_dict(self, dict_in):
        self._dict = dict_in

    @property
    def get_dict(self):
        return self._dict

    def __add__(self, other):
        new_my_dict = MyDict()
        new_my_dict.set_dict({**self.get_dict, **other.get_dict})
        return new_my_dict

    def __str__(self):
        return f"{self._dict}"


if __name__ == "__main__":
    dict_1 = MyDict(("key_1", 1111), ("key_2", 2222))
    print(dict_1)
    dict_1["key_3"] = 3333
    print(dict_1)
    dict_2 = MyDict()
    print(dict_2)
    dict_2.set_dict({"key_4": 4444, "key_5": 5555})
    dict_3 = dict_1 + dict_2
    print(dict_3)
