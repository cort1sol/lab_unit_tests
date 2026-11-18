import unittest
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    
    def test_area_positive(self):
        """Проверка площади круга для положительного радиуса."""
        # Формула: pi * r^2. Для r=10: 3.14159... * 100 = 314.159...
        self.assertAlmostEqual(area(10), 314.1592653589793)

    def test_area_zero(self):
        """Проверка площади круга при радиусе 0 (граничный случай)."""
        self.assertEqual(area(0), 0)

    def test_perimeter_positive(self):
        """Проверка длины окружности для положительного радиуса."""
        # Формула: 2 * pi * r. Для r=10: 2 * 3.14159... * 10 = 62.8318...
        self.assertAlmostEqual(perimeter(10), 62.83185307179586)

    def test_perimeter_zero(self):
        """Проверка длины окружности при радиусе 0."""
        self.assertEqual(perimeter(0), 0)

if __name__ == '__main__':
    unittest.main()