#! /usr/bin/env python

# author: Thomas Fillon <thomas@parisson.com>

from __future__ import division

from numpy import arange, sin
from unit_timeside import *
from timeside.decoder.utils import get_uri, get_media_uri_info, path2uri
import os.path


class TestGetUri(TestCase):
    "Test get_uri function"
    def testFileName(self):
        "Retrieve the uri from a filename"
        self.source = os.path.join(os.path.dirname(__file__),
                                   "samples/sweep.wav")

        self.uri = path2uri(os.path.abspath(self.source))

    def testUri(self):
        "Retrieve the uri from an uri"
        self.uri = 'file://already/an/uri/file.wav'
        self.source = self.uri

    def tearDown(self):
        self.assertEqual(self.uri, get_uri(self.source))


class TestGetUriWrongUri(TestCase):
    def testMissingFile(self):
        "Missing file raise IOerror"
        self.source = os.path.join(os.path.dirname(__file__),
                                   "a_missing_file_blahblah.wav")
    def testNotValidUri(self):
        "Not valid uri raise IOerror"
        self.source = os.path.join("://not/a/valid/uri/parisson.com")

    def testNotSupportedUriProtocol(self):
        "Not supported uri protocol raise IOerror"
        self.source = os.path.join("mailto://john.doe@parisson.com")

    def tearDown(self):
        self.assertRaises(IOError, get_uri, self.source)


class TestGetMediaInfo(TestCase):
    "Test get_media_uri_info function on an uri"

    def setUp(self):
        self.test_exact_duration = True
        self.source_duration = 8
        self.expected_channels = 2
        self.expected_samplerate = 44100
        self.expected_depth = 16

    def testWav(self):
        "Test wav decoding"
        self.source = os.path.join(os.path.dirname(__file__),
                                   "samples/sweep.wav")


    def testWavMono(self):
        "Test mono wav decoding"
        self.source = os.path.join(os.path.dirname(__file__),
                                   "samples/sweep_mono.wav")

        self.expected_channels = 1

    def testWav32k(self):
        "Test 32kHz wav decoding"
        self.source = os.path.join(os.path.dirname(__file__),
                                   "samples/sweep_32000.wav")
        self.expected_samplerate = 32000

    def testFlac(self):
        "Test flac decoding"
        self.source = os.path.join(os.path.dirname(__file__),
                                   "samples/sweep.flac")

    def testOgg(self):
        "Test ogg decoding"
        self.source = os.path.join(os.path.dirname(__file__),
                                   "samples/sweep.ogg")
        self.expected_depth = 0  # ?

    def testMp3(self):
        "Test mp3 decoding"
        self.source = os.path.join(os.path.dirname(__file__),
                                   "samples/sweep.mp3")
        self.expected_depth = 32

    def tearDown(self):
        uri = get_uri(self.source)
        uri_info = get_media_uri_info(uri)
        self.assertEqual(self.source_duration, uri_info['duration'])
        self.assertEqual(self.expected_channels, uri_info['streams'][0]['channels'])
        self.assertEqual(self.expected_samplerate, uri_info['streams'][0]['samplerate'])
        self.assertEqual(self.expected_depth, uri_info['streams'][0]['depth'])

if __name__ == '__main__':
    unittest.main(testRunner=TestRunner())