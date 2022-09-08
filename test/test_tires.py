import unittest


from tires.model.carrigan_tires import CarriganTires
from tires.model.octoprime_tires import OctoprimeTires

class TestCarrigan(unittest.TestCase):
    def test_should_be_serviced(self):
        sensors = [0.9, 0.3, 0.1, 0]
        tires = CarriganTires(sensors)
        self.assertTrue(tires.needs_service())

    def test_should_not_be_serviced(self):
        sensors = [0.89, 0.3, 0.1, 0]
        tires = CarriganTires(sensors)
        self.assertFalse(tires.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_should_be_serviced(self):
        sensors = [0.9, 0.9, 0.2, 1]
        tires = OctoprimeTires(sensors)
        self.assertTrue(tires.needs_service())

    def test_should_not_be_serviced(self):
        sensors = [0.89, 0.3, 0.1, 0]
        tires = OctoprimeTires(sensors)
        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()