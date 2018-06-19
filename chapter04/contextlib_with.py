import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print("file open")
    yield
    print("file end")

with file_open("TT.txt") as f_opend:
    print("file processing")
