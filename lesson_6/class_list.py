class MyList:

    def __init__(self, *args):
        self._my_list = [*args]

    def __iter__(self):
        for elem in self._my_list:
            yield elem

    def __getitem__(self, index):
        return self._my_list[index]

    def __setitem__(self, index, value):
        self._my_list[index] = value

    def set_list(self, list_in):
        self._my_list = list_in[:]

    def length(self):
        len_ = 0
        for _ in self._my_list:
            len_ += 1
        return len_

    def append(self, value):
        appended_list = self._my_list[:] + [value]
        self._my_list = appended_list[:]
        return self._my_list

    def insert(self, position, value):
        inserted_list = self._my_list[:position] + [value] + self._my_list[position:]
        self._my_list = inserted_list[:]
        return self._my_list

    def pop(self, position=-1):
        popped_item = self._my_list[position]
        popped_list = [item for item in self._my_list if item != popped_item]
        self._my_list = popped_list[:]
        return popped_item

    def remove(self, value):
        if value in self._my_list:
            value_first_index = 0
            for index, item in enumerate(self._my_list):
                if item == value:
                    value_first_index = index
                    break
            new_list = [item for item in self._my_list if item != self._my_list[value_first_index]]
            self._my_list = new_list[:]
        return self._my_list

    def clear(self):
        self._my_list = []
        return self._my_list

    def __add__(self, other):
        new_my_list = MyList()
        total_list = self._my_list[:] + other[:]
        new_my_list.set_list(total_list)
        return new_my_list

    def __str__(self):
        return f"{self._my_list}"


if __name__ == "__main__":
    list_1 = MyList(15, 4, "call")
    print(list_1)
    list_1.append(1)
    list_1.append(9)
    print(list_1)
    list_1[0] = 4
    print(list_1)
    list_1.insert(2, 7)
    print(list_1)
    list_1.remove(1)
    list_2 = MyList(5)
    new_lst = list_1 + list_2
    print(new_lst)
