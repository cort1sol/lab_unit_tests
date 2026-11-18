import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    
    def test_area_positive(self):
        """Проверка площади прямоугольника."""
        # Формула: a * b. Для сторон 10 и 5: 10 * 5 = 50
        self.assertEqual(area(10, 5), 50)

    def test_area_zero(self):
        """Проверка площади прямоугольника, если одна из сторон равна 0."""
        self.assertEqual(area(10, 0), 0)

    def test_perimeter_positive(self):
        """Проверка периметра прямоугольника."""
        # Формула: (a + b) * 2. Для сторон 10 и 5: (10 + 5) * 2 = 30
        self.assertEqual(perimeter(10, 5), 30)

    def test_perimeter_zero(self):
        """Проверка периметра прямоугольника, если стороны равны 0."""
        self.assertEqual(perimeter(0, 0), 0)

if __name__ == '__main__':
    unittest.main()