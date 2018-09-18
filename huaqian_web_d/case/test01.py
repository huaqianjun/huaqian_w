import unittest

class IntegerArithmeticTestCase(unittest.TestCase):

    def test_1(self):  # test method names begin with 'test'
        '''用例说明：111'''
        print("11111111111111")
        a = "admin"   # 实际结果
        b = "admin1"   # 期望结果
        self.assertNotIn(a, b)
        # self.assertNotEqual(a, b)
        # self.assertTrue(a != b)

    def setUp(self):
        # 每个用例执行之前，先执行一次
        print("先打开浏览器")

    @classmethod
    def setUpClass(cls):
        print("用例前，只执行一次")

    def test_a(self):
        '''用例说明：aaaaa'''
        print("222222222")
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

    def test_A(self):
        '''用例说明：AAAA'''
        print("333333")
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

if __name__ == '__main__':
    unittest.main()
