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


