import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    
    def test_area_positive(self):
        """Проверка площади треугольника."""
        # Формула: (a * h) / 2. Для основания 10 и высоты 5: (10 * 5) / 2 = 25
        self.assertEqual(area(10, 5), 25)

    def test_area_zero_height(self):
        """Проверка площади, если высота равна 0."""
        self.assertEqual(area(10, 0), 0)

    def test_perimeter_positive(self):
        """Проверка периметра треугольника."""
        # Формула: a + b + c. Для сторон 3, 4, 5: 3 + 4 + 5 = 12
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_zero(self):
        """Проверка периметра, если все стороны равны 0."""
        self.assertEqual(perimeter(0, 0, 0), 0)

if __name__ == '__main__':
    unittest.main()