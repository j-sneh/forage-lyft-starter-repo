import unittest

from engine.model.capulet_engine import CapuletEngine
from engine.model.sternman_engine import SternmanEngine
from engine.model.willoughby_engine import WilloughbyEngine

class TestCapulet(unittest.TestCase):
    def test_should_be_serviced_30001(self):
        engine = CapuletEngine(30001, 0)
        self.assertTrue(engine.needs_service())

    def test_should_be_serviced_large(self):
        engine = CapuletEngine(80000, 10000)
        self.assertTrue(engine.needs_service())
    
    def test_should_not_be_serviced(self):
        engine = CapuletEngine(20000, 1)
        self.assertFalse(engine.needs_service())

class TestWilloughby(unittest.TestCase):
    def test_should_be_serviced_60001(self):
        engine = WilloughbyEngine(60001, 0)
        self.assertTrue(engine.needs_service())

    def test_should_be_serviced_large(self):
        engine = WilloughbyEngine(90000, 10000)
        self.assertTrue(engine.needs_service())
    
    def test_should_not_be_serviced(self):
        engine = WilloughbyEngine(30000, 1)
        self.assertFalse(engine.needs_service())

class TestSternman(unittest.TestCase):
    def test_should_be_serviced(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        engine = SternmanEngine(False)
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()