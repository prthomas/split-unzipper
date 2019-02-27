import unittest
import zipfile

from splitunzipper import SplitUnzipper


class TestSplitUnzipper(unittest.TestCase):
    defaultsplitsize = 128 * 1024 * 1024


    def test_defineobject_checkdefaults(self):
        testsplitunzipper = SplitUnzipper(ZipFile='')
        assert(testsplitunzipper.splitsize == self.defaultsplitsize)
        assert(not testsplitunzipper.headerincl)

    def test_setsplitsize1k(self):
        testsplitunzipper = SplitUnzipper(ZipFile='', SplitSize=1024)
        assert(testsplitunzipper.splitsize == 1024)
        assert(not testsplitunzipper.headerincl)

    def test_setheaderincl(self):
        testsplitunzipper = SplitUnzipper(ZipFile='', HeaderIncl=True)
        assert(testsplitunzipper.splitsize == self.defaultsplitsize)
        assert(testsplitunzipper.headerincl)

    def test_exceptionnotzip(self):
         with open('splitunzipper.py', 'rb') as notzipfile:
            self.assertRaises(zipfile.BadZipFile,
                              SplitUnzipper(notzipfile))

if __name__ == '__main__':
    unittest.main()
