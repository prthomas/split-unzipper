import zipfile


class SplitUnzipper:
    defaultSize = 128 * 1024 * 1024

    def __init__(self, FileStream, SplitSize=defaultSize, HeaderIncl=False):
        self.zipfile = zipfile.ZipFile(FileStream)
        self.splitsize = SplitSize
        self.headerincl = HeaderIncl

    def __enter__(self):
        return self

    def __exit__(self):
        self.zipfile.close()
