class FileManager(object):

    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type_, value, traceback):
        self.file_obj.close()


with FileManager('test.txt', 'a+') as f:
    f.write("Hello")

with FileManager('test.txt', 'r') as f:
    result = f.read()
    print(result)
