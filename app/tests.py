import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from .views.default import DefaultViews
        request = testing.DummyRequest()
        inst = DefaultViews(request)
        info = inst.home()
        # self.assertEqual(info['project'], 'deeper_system')

    def test_howdy(self):
        from .views.themes import howdy_view
        request = testing.DummyRequest()
        response = howdy_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Howdy!!', response.body)


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
