import json
import requests
import vcr
import util


class RecruitmentData(object):
    """
    Simple class to store URI, response from URI, and json data from that response, also some methods to use in tests
    """
    def __init__(self):
        self.uri = util.URI
        self.response = ""
        self.json_body = ""

    # Load data from given URI - 'http://hs-recruiting-test-resume-data.s3.amazonaws.com/allcands-full.json' by default
    def load_data(self):
        """
        Get response from URI, generate VCR cassette
        :return: HTTP return code 200 (OK) - can basically return any code you want - as long as it doesnt
        raise exceptions, its OK.
        :rtype: str
        """
        try:
            with vcr.use_cassette(util.local_cassette(util.CASSETTE_NAME), serializer=util.SERIALIZER,
                                  record_mode=util.RECORD_MODE):
                self.response = requests.get(util.URI)
        except TypeError:
            print("TypeError: No valid response was found!")

        if self.response.status_code == 200:
            self.json_body = json.loads(self.response.text)
            return "200 OK"
        else:
            raise Exception(self.response.text)

    def get_num_candidates(self):
        """
        Get number of candidates in json payload. Can also be done by email if unique
        :return:number of entities (candidates) in json payload
        :rtype: int
        """
        return len([entity for entity in self.json_body])

    def get_users_info(self):
        """
        Create a dictionary of {user:email} per each user. This is the indication that each user is verified by his
        email.
        :return: dictionary of {user1: email1, user2: email2...}
        :rtype: dict
        """
        email_to_name_dict = {}
        for entity in self.json_body:
            try:
                email = entity["contact_info"]["email"]
                name = entity["contact_info"]["name"]["formatted_name"]
                email_to_name_dict[email] = name
            except KeyError:
                print("Unable to withdraw email and/or name from JSON object!")
        return email_to_name_dict


