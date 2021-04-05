import json
import requests
import vcr
import util


class RecruitmentData(object):
    def __init__(self):
        self.uri = util.URI
        self.response = ""
        self.json_body = ""

    def load_data(self):
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

    def get_candidate_emails(self):
        return [entity.get('email') for entity in self.json_body]

    def get_num_candidates(self):
        return len([entity.get('email') for entity in self.json_body])

    def get_users_info(self):
        # Create dict with users email and name e.g. {asd"
        email_to_name_dict = {}
        for entity in self.json_body:
            try:
                email = entity["contact_info"]["email"]
                name = entity["contact_info"]["name"]["formatted_name"]
                email_to_name_dict[email] = name
            except KeyError:
                print("Unable to withdraw email and/or name from JSON object!")
        return email_to_name_dict


