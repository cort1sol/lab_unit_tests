import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    
    def test_area_positive(self):
        """Проверка площади квадрата с положительной стороной."""
        # Формула: a * a. Для a=5: 5 * 5 = 25
        self.assertEqual(area(5), 25)

    def test_area_zero(self):
        """Проверка площади квадрата при стороне 0."""
        self.assertEqual(area(0), 0)

    def test_perimeter_positive(self):
        """Проверка периметра квадрата с положительной стороной."""
        # Формула: 4 * a. Для a=5: 4 * 5 = 20
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_zero(self):
        """Проверка периметра квадрата при стороне 0."""
        self.assertEqual(perimeter(0), 0)

if __name__ == '__main__':
    unittest.main()