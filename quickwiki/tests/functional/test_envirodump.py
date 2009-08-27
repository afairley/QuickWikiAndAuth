from quickwiki.tests import *

class TestEnvirodumpController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='envirodump', action='index'))
        # Test response...
