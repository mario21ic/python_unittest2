import unittest2

def suite():
    suite = unittest.TestSuite()
    suite.addTest(ArithTest())
    suite.addTest(ArithTestFail())
    return suite

if __name__ == '__main__':
    loader = unittest2.TestLoader()
    tests = loader.discover('./tests/')
    #tests = suite()
    #runner.run (test_suite)
    runner = unittest2.runner.TextTestRunner()
    runner.run(tests)

