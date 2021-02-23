import unittest

'''
 生命周期
 
    setUpClass
    setUp
    hello1
    tearDown
    setUp
    hello2
    tearDown
    tearDownClass
    
    
    TestCase - testLoader TextTestRunner TextTestResult
    
    测试报告的生成 不咋地
'''


class TestDemos(unittest.TestCase):
    def setUp(self):
        '''环境初始化'''
        "Hook method for setting up the test fixture before exercising it."
        print('setUp')
        pass

    def tearDown(self):
        '''释放资源'''
        "Hook method for deconstructing the test fixture after testing it."
        print('tearDown')
        pass

    def test_demo1(self):
        self.assertEqual(1, 1)
        print('hello1')

    def test_demo2(self):
        self.assertEqual(1, 1)
        print('hello2')

    # @unittest.skip
    @unittest.skipIf(1 + 1 == 2, "OK")
    def test_demo3(self):
        self.assertEqual(1, 1)
        print('hello2')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

        pass

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

        pass


''' '''
if __name__ == '__main__':
    # 默认执行全部的测试方法
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestDemos.test_demo2())
    # suite.addTest(TestDemos.test_demo2())

    # 方法
    # unittest.TextTestRunner.run(suite)
    # unittest.suite.TestSuite.run(suite)

    # 类
    suiteclasss = unittest.TestLoader().loadTestsFromTestCase(TestDemos)
    unitALL = unittest.TestSuite([suiteclasss])
    unittest.TextTestRunner.run(unitALL)

    # 匹配测试
    # test_dir = './test_case'
    discovery = unittest.defaultTestLoader.discover("./", 'test*.py')
    unittest.TextTestRunner.run(discovery)
