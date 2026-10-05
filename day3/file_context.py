
class FileManager:
    def __init__(self,path,mode):
        self.path = path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.path,self.mode,encoding="utf-8")

        return self.file

    def __exit__(self, exc_type, exc, tb):
        if self.file:
            self.file.close()


with open("data/test.txt","r",encoding="utf-8") as f:
        for line in f:
            print(line.strip())