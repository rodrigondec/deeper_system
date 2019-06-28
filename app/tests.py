import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views.default import DefaultViews
        request = testing.DummyRequest()
        inst = DefaultViews(request)
        info = inst.home()
        self.assertEqual(info['videos'], [])

    def test_howdy(self):
        from .views.themes import ThemeViews
        request = testing.DummyRequest()
        inst = ThemeViews(request)
        info = inst.ranking()
        self.assertEqual(info['themes'], [])


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from app import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Pyramid' in res.body)

    def test_howdy(self):
        res = self.testapp.get('/howdy', status=200)
        self.assertTrue(b'Howdy!!' in res.body)
