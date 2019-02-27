import unittest
import zipfile

from splitunzipper import SplitUnzipper


class TestSplitUnzipper(unittest.TestCase):
    defaultsplitsize = 128 * 1024 * 1024

    def test_defineobject_checkdefaults(self):
        with open('z.zip', 'rb') as testzipfile:
            with SplitUnzipper(FileStream=testzipfile) as testsplitunzipper:
                assert(testsplitunzipper.splitsize == self.defaultsplitsize)
                assert(not testsplitunzipper.headerincl)

    def test_setsplitsize1k(self):
        with open('z.zip', 'rb') as testzipfile:
            with SplitUnzipper(FileStream=testzipfile, SplitSize=1024) as testsplitunzipper:
                assert(testsplitunzipper.splitsize == 1024)
                assert(not testsplitunzipper.headerincl)

    def test_setheaderincl(self):
        with open('z.zip', 'rb') as testzipfile:
            with SplitUnzipper(FileStream=testzipfile, HeaderIncl=True) as testsplitunzipper:
                assert(testsplitunzipper.splitsize == self.defaultsplitsize)
                assert(testsplitunzipper.headerincl)

    def test_exceptionnotzip(self):
        with open('splitunzipper.py', 'rb') as notzipfile:
            with self.assertRaises(zipfile.BadZipFile):
                with SplitUnzipper(notzipfile) as badsplitunzipper:
                    pass


if __name__ == '__main__':
    unittest.main()
