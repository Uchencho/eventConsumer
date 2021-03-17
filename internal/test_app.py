from unittest import TestCase
import pandas as pd
from internal.app import App


class MockS3Client:

    def read_prev_data_updates(self, file_read_name):

        data = {'year': [2014, 2018,2020,2017], 
            'make': ["toyota", "honda","hyndai","nissan"],
            'model':["corolla", "civic","accent","sentra"]
        }

        return pd.DataFrame(data)



class TestRenewals(TestCase):

    expected_number_of_rows = 4

    def test_renewals_returns_expected_number_of_rows(self):
        a = App("testApp", MockS3Client())
        result = a.consume('renewals')
        self.assertEqual(self.expected_number_of_rows, result)
        

    def test_renewals_raises_error_with_invalid_df(self):
        
        with self.assertRaises(EnvironmentError):
            a = App("testApp")
            a.consume('renewals')


