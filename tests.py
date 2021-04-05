import unittest
from recruitmentData import RecruitmentData


class MyTests(unittest.TestCase):
    def setUp(self):
        self.recruitmentObj = RecruitmentData()
        self.recruitmentObj.load_data()

    def test_response_code(self):
        """testing response code of the request"""
        self.assertEqual(200, self.recruitmentObj.response.status_code)

    def test_num_candidates(self):
        """testing a number of candidates is expected"""
        self.assertEqual(4, self.recruitmentObj.get_num_candidates())

    def test_candidates_identified_by_email(self):
        """testing a candidate with user and email"""
        expected_result = {'captainamerica@yahoo.com': 'Clark L Kent',
                          'bruce-wayne-batman@verizon.net': 'Bruce Wayne',
                          'Peter.Parker@Spidermantech.com': 'Peter Parker',
                          'Heisenberg@hotmail.com': 'Walter White'}

        self.assertEqual(expected_result, self.recruitmentObj.get_users_info())