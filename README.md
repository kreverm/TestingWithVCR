# TestingWithVCR

Simple testing program using VCR.

Gets response from given URI (with JSON payload), generates VCR cassette,  and performs 3 tests using unittest:

1. Verify response code for the request is 200 (OK).
2. Verify number of candidates in JSON payload is correct.
3. The response body contains the expected candidates, identified by email address.

Run cmd: python -m unittest %your_local_folder%/tests.py

Python3.6
