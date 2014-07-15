from Nitansh_2 import CompanyInfo, MainHandler
import unittest

class TestCompanyInfoFunctions(unittest.TestCase):

    def setUp(self):
        self.my_object = CompanyInfo('nitansh')

    def test_add_info(self):
        self.my_object.add_info('2010', 'feb', '100')
        local_string = self.my_object.share_info()
        self.assertEqual('nitansh ---> the peak time is 2010 feb  and Share at that time is 100 ', local_string)        

    def test_share_peak_info(self):
        self.my_object.add_info('2010', 'feb', '150')
        self.my_object.add_info('2011', 'feb', '200')
        self.assertEqual(('2011 feb ', '200'), self.my_object.find_peak_share_time())
        self.my_object.add_info('2011', 'jan', '200')
        self.assertEqual(('2011 feb 2011 jan ', '200'), self.my_object.find_peak_share_time())
        
class TestMainHandler(unittest.TestCase):
    def setUp(self):
        self.my_object = MainHandler()

    def test_add_company(self):
        self.my_object.add_company('nitansh')
        self.assertEqual(1 , len(self.my_object.company_list))

    def test_read_from_file(self):
        self.my_object.read_from_file('sample.csv')
        self.assertEqual(5, len(self.my_object.company_list))


if __name__ == '__main__':
    unittest.main()