import unittest
from unittest.mock import patch 
from employee import Employee

class TestEmployee(unittest.TestCase): 

    @classmethod
    def setUpClass(cls) -> None:
        # run at beginning of class 
        pass 

    @classmethod
    def tearDownClass(cls) -> None:
        # run at end of class 
        pass 

    def setUp(self): 
        # run before each test
        self.emp_1 = Employee('albert', 'miller', 80000)

    def tearDown(self) -> None:
        # run after each test 
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'albert.miller@gmail.com')


    def test_monthly_schedule(self): 
        # <module/file>.<thing were mocking>
        with patch('employee.requests.get') as mocked_get: 
            # happy 
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "success"
            
            schedule = self.emp_1.monthly_schedule('may')
            mocked_get.assert_called_with('http://company.com/miller/may')
            self.assertAlmostEqual(schedule, "success")
            
            # sad
            mocked_get.return_value.ok = False
            
            schedule = self.emp_1.monthly_schedule('may')
            mocked_get.assert_called_with('http://company.com/miller/may')


if __name__ == '__main__':
    unittest.main()