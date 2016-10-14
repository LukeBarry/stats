import unittest
import cProfile

class Test(unittest.TestCase):

    def testSomething(self):
        self.DoSomethingIDontCareAbout()

        param = 'whatever'
        cProfile.runctx(
            'self.RunFunctionIThinkIsSlow(param)',
            globals(),
            locals(),
            'myProfilingFile.pstats'
        )

        self.AssertSomeStuff() # This is after all, a test

if __name__ == "__main__":
    unittest.main()
    
    