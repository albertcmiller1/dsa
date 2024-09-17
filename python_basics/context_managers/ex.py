class OpenFile: 
    def __init__(self, file_name, mode): 
        self._file_name = file_name
        self._mode = mode
    
    def __enter__(self): 
        self._file = open(self._file_name, self._mode)
        return self._file

    def __exit__(self, exc_type, exc_val, traceback): 
        self._file.close()
    
with OpenFile('sample.txt', "w") as f: 
    f.write("Testing...")

# print(f.closed)