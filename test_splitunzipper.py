import unittest

from splitunzipper import SplitUnzipper

class TestSplitUnzipper(unittest.TestCase):
  def test_defineobject(self):
    testsplitunzipper = SplitUnzipper(ZipFile="")

if __name__ == '__main__':
    unittest.main()
