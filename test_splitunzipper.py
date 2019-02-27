import unittest

from splitunzipper import SplitUnzipper

class TestSplitUnzipper(unittest.TestCase):
  def test_defineobject_checkdefaults(self):
    testsplitunzipper = SplitUnzipper(ZipFile="")
    assert(testsplitunzipper.splitsize == 128 * 1024 * 1024)
    assert(testsplitunzipper.headerincl == False)

if __name__ == '__main__':
    unittest.main()
