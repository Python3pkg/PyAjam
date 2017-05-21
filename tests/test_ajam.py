from nose import SkipTest
from nose.tools import assert_equal

from pyajam import Pyajam

class TestPyajam:
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ajam_unify_xml(self):
        input = '''<ajax-response>
                  <response type='object' id='unknown'><generic response='Success' message='Waiting for Event...' /></response>
                  <response type='object' id='unknown'><generic event='PeerStatus' privilege='system,all' peer='SIP/601' peerstatus='Registered' /></response>
                  <response type='object' id='unknown'><generic event='WaitEventComplete' /></response>
                </ajax-response> '''
        expected = [{'peer': 'SIP/601', 'peerstatus': 'Registered', 'event': 'PeerStatus', 'privilege': 'system,all'}, {'event': 'WaitEventComplete'}]

        ajam = Pyajam()

        #raise SkipTest
        assert_equal(expected, ajam._unify_xml(input))
