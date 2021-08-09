import unittest
import main
import exceptions


class MainTest(unittest.TestCase):

    def test_when_fuel_is_low_for_start_failed(self):
        car = main.Car(fuel=-100, fuel_consumption=10, weight=100)
        eng = main.Engine(pistons=10, volume=20)
        car.set_engine(eng)
        self.assertRaises(exceptions.LowFuelError, car.start)

    def test_when_fuel_is_enough(self):
        car = main.Car(fuel=100, fuel_consumption=10, weight=100)
        eng = main.Engine(pistons=10, volume=20)
        car.set_engine(eng)
        self.assertTrue(car.start)

    def test_when_fuel_is_not_enough_for_distance(self):
        car = main.Car(fuel=100, fuel_consumption=10, weight=100)
        eng = main.Engine(pistons=10, volume=20)
        car.set_engine(eng)
        self.assertRaises(exceptions.NotEnoughFuel, car.move, 1000)

    def test_when_fuel_is_enough_for_distance(self):
        car = main.Car(fuel=100, fuel_consumption=10, weight=100)
        eng = main.Engine(pistons=10, volume=20)
        car.set_engine(eng)
        self.assertTrue(car.move, 5)

    def test_plane_cargo_overload(self):
        plane = main.Plane(fuel=100, fuel_consumption=10, weight=50, max_cargo=30)
        self.assertRaises(exceptions.CargoOverload, plane.load_cargo, 50)

    def test_plane_cargo_is_ok(self):
        plane = main.Plane(fuel=100, fuel_consumption=10, weight=50, max_cargo=30)
        self.assertTrue(plane.load_cargo, 20)

    def test_plane_remove_all_cargo(self):
        plane = main.Plane(fuel=100, fuel_consumption=10, weight=50, max_cargo=30)
        plane.load_cargo(new_cargo=25)
        self.assertEqual(plane.remove_all_cargo(), 25)
        self.assertEqual(plane.cargo, 0)