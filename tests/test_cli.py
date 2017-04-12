from testconfig import *
from r360_py.cli.__main__ import createParser, buildTravelOptions, getPolygons
from r360_py.util.enum.PolygonSerializationType import PolygonSerializationType
from r360_py.util.enum.TravelType import TravelType
# from r360_py.cli import create_parser
from unittest import TestCase
import json

class CommandLineTestCase(TestCase):
    """
    Base TestCase class, sets up a CLI parser
    """
    @classmethod
    def setUpClass(cls):
        parser = createParser()
        cls.parser = parser

class CliTestCase(CommandLineTestCase):
    def test_with_empty_args(self):
        """
        User passes no args, should fail with SystemExit
        """                              
        with self.assertRaises(SystemExit):
            self.parser.parse_args([

            ])

    def test_with_required_args(self):
        """
        User passes all required args, should pass
        """
        args = self.parser.parse_args([
            '--travelTimes', '300', '600', 
            '--travelType', 'walk', 
            '--source', '52.52;13.405', 
            '--outputDir', 'data/', 
            '--outputFilename', 'test.geojson',
            '--serviceKey', API_KEY,
            '--serviceUrl', 'http://service.route360.net/germany/'
        ])

        self.assertListEqual(args.travelTimes, [300, 600], 'Should properly assign travel times')
        self.assertEqual(args.travelType, 'walk', 'Should properly assign travel type')
        self.assertListEqual(args.source, [52.52, 13.405], 'Should properly assign source to list')
        self.assertEqual(args.outputDir, 'data/', 'Should properly assign output dir')
        self.assertEqual(args.outputFilename, 'test.geojson', 'Should properly assign output filename')
        self.assertIs(isinstance(args.serviceKey, str), True, 'Should properly assign service key')
        self.assertEqual(args.serviceUrl, 'http://service.route360.net/germany/', 'Should properly assign service url')

    def test_travel_options_required(self):
        """
        Travel Options created with required args
        """
        args = self.parser.parse_args([
            '--travelTimes', '300', '600', 
            '--travelType', 'walk', 
            '--source', '52.52;13.405', 
            '--outputDir', 'data/', 
            '--outputFilename', 'test.geojson',
            '--serviceKey', API_KEY,
            '--serviceUrl', 'http://service.route360.net/germany/'
        ])

        travelOptions = buildTravelOptions(args)
        self.assertIsNotNone(travelOptions, 'Should succeed in creating travelOptions')
        self.assertEqual(travelOptions.getTravelType().value, 'walk', 'Should properly assign travel type to travelOptions')

    def test_polygon_required_args(self):
        """
        Polygon creted with required args
        """
        args = self.parser.parse_args([
            '--travelTimes', '300', '600', 
            '--travelType', 'walk', 
            '--source', '52.52;13.405', 
            '--outputDir', 'data/', 
            '--outputFilename', 'test.geojson',
            '--serviceKey', API_KEY,
            '--serviceUrl', 'http://service.route360.net/germany/'
        ])

        travelOptions = buildTravelOptions(args)
        polygons = getPolygons(travelOptions)
        self.assertIsNotNone(polygons, 'Should succeed in creating polygons')