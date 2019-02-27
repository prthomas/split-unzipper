class SplitUnzipper:
    defaultSize = 128 * 1024 * 1024
    def __init__(self, ZipFile, SplitSize=defaultSize, HeaderIncl=False):
        self.splitsize = SplitSize
        self.headerincl = HeaderIncl

