import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):
    # It will run once before all tests
    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures"""
        """
        Usage:
        1. Initialize resources shared across all tests
        2. Set up database connections
        3. Load configuration settings
        4. Prepare test data that is common for all tests
        """
        print("SetupClass: Run once before all tests")

    # It will run once after all tests
    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures"""
        """
        Usage:
        1. Clean up resources initialized in setUpClass
        2. Close database connections
        3. Clear configuration settings
        4. Remove test data created for all tests
        """
        print("TearDownClass: Run once after all tests")

    # It will run before each test method
    def setUp(self):
        """Set up test fixtures"""
        """
        Usage:
        1. Initialize resources needed for each test
        2. Set up test data specific to each test
        3. Prepare mock objects
        """
        self.emp_1 = Employee('John', 'Doe', 50000)
        self.emp_2 = Employee('Jane', 'Smith', 60000)

    # It will run after each test method
    def tearDown(self):
        """Tear down test fixtures"""
        """
        Usage:
        1. Clean up resources
        2. Close database connections
        3. Reset configurations
        4. Delete test data from databases
        5. Any other necessary cleanup after each test method
        """
        pass

    def test_email(self):
        """Test the email property"""
        self.assertEqual(self.emp_1.email, 'John.Doe@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        """Test the fullname property"""
        self.assertEqual(self.emp_1.fullname, 'John Doe')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    
    def test_monthly_schedule(self):
        """Test the monthly_schedule method with mocking"""
        with patch('employee.requests.get') as mocked_get:
            # Mock a successful response
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Doe/May')
            self.assertEqual(schedule, 'Success')

            # Mock a failed response
            mocked_get.return_value.ok = False
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()