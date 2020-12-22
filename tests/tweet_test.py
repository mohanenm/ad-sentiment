# TODO: come back to this, going to be important with flask/aws and larger streams

import unittest
from unittest.case import skip

from mock import MagicMock, patch
import six

from .config import create_auth
from .test_utils import mock_tweet
from tweepy.api import API
from tweepy.auth import OAuthHandler
from tweepy.models import Status
from tweepy.streaming import ReadBuffer, Stream,


class MockStreamListener(StreamListener):
    def __init__(self, test_case):
        super(MockStreamListener, self).__init__()
            self.test_case = test_case
            self.status_count = 0
            self.status_stop_count = 0
            self.connect_cb = None

        def on_connect(self):
            if self.connect_cb:
                self.connect_cb()

        def on_timeout(self):
            self.test_case.fail('timeout')
            return False

        def on_error(self, code):
            print("response: %s" % code)
            return True

        def on_status(self, status):
            self.status_count += 1
            self.test_case.assertIsInstance(status, Status)
            if self.status_stop_count == self.status_count:
                return False


class TweepyStreamTests(unittest.TestCase):
    def setUp(self):
        self.auth = create_auth()
        self.listener = MockStreamListener(self)
        self.stream = Stream(self.auth, self.listener, timeout=3.0)

    def tearDown(self):
        self.stream.disconnect()

    def on_connect(self):
        API(self.auth).update_status(mock_tweet())

