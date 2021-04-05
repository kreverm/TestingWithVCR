import os

# Consts
import vcr

URI = 'http://hs-recruiting-test-resume-data.s3.amazonaws.com/allcands-full.json'
CASSETTE_NAME = "cassette.yaml"
CASSETTE_FOLDER = "resource"
RECORD_MODE = "once"
SERIALIZER = "json"


# Util function to get cassette from local folder 'resource'
def local_cassette(filename):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_dir, CASSETTE_FOLDER, filename)
