import gzip
import zipfile


class SplitUnzipper:
    defaultSize = 128 * 1024 * 1024

    def __init__(self, FileStream, SplitSize=defaultSize, HeaderIncl=False):
        self.zipfile = zipfile.ZipFile(FileStream)
        self.splitsize = SplitSize
        self.headerincl = HeaderIncl

    def __enter__(self):
        return self

    def __exit__(self, exceptiontype, exceptionvalue, traceback):
        self.zipfile.close()

    def unzipandgz(self):
        for filename in self.zipfile.namelist():
            print(filename)
            with self.zipfile.open(filename) as zefile:
                fout = gzip.open(f"{filename}.gz", 'wb')
                for line in zefile:
                    fout.write(line)

                fout.flush()
                fout.close()
