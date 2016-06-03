import unittest
import identicon

class TestCase(unittest.TestCase):

    '''
        Initializes a test version of our Flask web application.
    '''
    def setUp(self):
        identicon.app.config["TESTING"] = True
        self.app = identicon.app.test_client()

    '''
        Test method that calls the URL / with the input “Moby Dock” for the name field.
        The test then checks that the method returns a 200 status code and the data con‐
        tains the strings “Hello” and “Moby Dock.”
    '''
    def test_get_mainpage(self):
        page = self.app.post("/", data=dict(name="Moby Dock"))
        assert page.status_code == 200
        assert 'Hello' in str(page.data)
        assert 'Moby Dock' in str(page.data)

    '''
        Tests that HTML entities are properly escaped in input.
    '''
    def test_html_escaping(self):
        page = self.app.post("/", data=dict(name='"><b>TEST</b><!--'))
        assert '<b>' not in str(page.data)

if __name__ == '__main__':
    unittest.main()
