import unittest
from math_library import MathLib

class TestCalculator(unittest.TestCase):

    def test_add_int(self):
        # Positive integer numbers
        self.assertEqual(MathLib.add(1, 1), 2)
        self.assertEqual(MathLib.add(123, 456), 579)
        self.assertEqual(MathLib.add(537891, 65219), 603110)
        self.assertEqual(MathLib.add(111111111111111, 222222222222222), 333333333333333)

        # Negative integer numbers
        self.assertEqual(MathLib.add(-1, -1), -2)
        self.assertEqual(MathLib.add(-123, -456), -579)
        self.assertEqual(MathLib.add(-537891, -65219), -603110)
        self.assertEqual(MathLib.add(-111111111111111, -222222222222222), -333333333333333)

        # Mixed integer numbers
        self.assertEqual(MathLib.add(-1, 1), 0)
        self.assertEqual(MathLib.add(-123, 456), 333)
        self.assertEqual(MathLib.add(-537891, 65219), -472672)
        self.assertEqual(MathLib.add(-111111111111111, 222222222222222), 111111111111111)

    def test_add_float(self):
        # Positive float numbers
        self.assertAlmostEqual(MathLib.add(1.23, 1.98), 3.21, 4)
        self.assertAlmostEqual(MathLib.add(123.2124, 456.9019), 580.1143, 4)
        self.assertAlmostEqual(MathLib.add(537891.1234, 65219.4321), 603110.5555, 4)
        self.assertAlmostEqual(MathLib.add(111111111111111.111111111111111, 222222222222222.222222222222222), 333333333333333.333333333333333, 4)

        # Negative float numbers
        self.assertAlmostEqual(MathLib.add(-1.23, -1.98), -3.21, 4)
        self.assertAlmostEqual(MathLib.add(-123.2124, -456.9019), -580.1143, 4)
        self.assertAlmostEqual(MathLib.add(-537891.1234, -65219.4321), -603110.5555, 4)
        self.assertAlmostEqual(MathLib.add(-111111111111111.111111111111111, -222222222222222.222222222222222), -333333333333333.333333333333333, 4)

        # Mixed float numbers
        self.assertAlmostEqual(MathLib.add(-1.23, 1.98), 0.75, 4)
        self.assertAlmostEqual(MathLib.add(-123.2124, 456.9019), 333.6895, 4)
        self.assertAlmostEqual(MathLib.add(-537891.1234, 65219.4321), -472671.6913, 4)
        self.assertAlmostEqual(MathLib.add(-111111111111111.111111111111111, 222222222222222.222222222222222), 111111111111111.111111111111111, 4)
 
    def test_sub_int(self):
               # Positive integer numbers
        self.assertEqual(MathLib.sub(1, 1), 0)
        self.assertEqual(MathLib.sub(123, 456), -333)
        self.assertEqual(MathLib.sub(537891, 65219), 472672)
        self.assertEqual(MathLib.sub(111111111111111, 222222222222222), -111111111111111)

        # Negative integer numbers
        self.assertEqual(MathLib.sub(-1, -1), 0)
        self.assertEqual(MathLib.sub(-123, -456), 333)
        self.assertEqual(MathLib.sub(-537891, -65219), -472672)
        self.assertEqual(MathLib.sub(-111111111111111, -222222222222222), 111111111111111)

        # Mixed integer numbers
        self.assertEqual(MathLib.sub(-1, 1), -2)
        self.assertEqual(MathLib.sub(-123, 456), -579)
        self.assertEqual(MathLib.sub(-537891, 65219), -603110)
        self.assertEqual(MathLib.sub(-111111111111111, 222222222222222), -333333333333333)

    def test_sub_float(self):
        # Positive float numbers
        self.assertAlmostEqual(MathLib.sub(1.23, 1.98), -0.75, 4)
        self.assertAlmostEqual(MathLib.sub(123.2124, 456.9019), -333.6895, 4)
        self.assertAlmostEqual(MathLib.sub(537891.1234, 65219.4321), 472671.6913, 4)
        self.assertAlmostEqual(MathLib.sub(111111111111111.111111111111111, 222222222222222.222222222222222), -111111111111111.111111111111111, 4)

        # Negative float numbers
        self.assertAlmostEqual(MathLib.sub(-1.23, -1.98), 0.75, 4)
        self.assertAlmostEqual(MathLib.sub(-123.2124, -456.9019), 333.6895, 4)
        self.assertAlmostEqual(MathLib.sub(-537891.1234, -65219.4321), -472671.6913, 4)
        self.assertAlmostEqual(MathLib.sub(-111111111111111.111111111111111, -222222222222222.222222222222222), 111111111111111.111111111111111, 4)

        # Mixed float numbers
        self.assertAlmostEqual(MathLib.sub(-1.23, 1.98), -3.21, 4)
        self.assertAlmostEqual(MathLib.sub(-123.2124, 456.9019), -580.1143, 4)
        self.assertAlmostEqual(MathLib.sub(-537891.1234, 65219.4321), -603110.5555, 4)
        self.assertAlmostEqual(MathLib.sub(-111111111111111.111111111111111, 222222222222222.222222222222222), -333333333333333.333333333333333, 4)

    def test_mul_int(self):
        # Positive integer numbers
        self.assertEqual(MathLib.mul(1, 1), 1)
        self.assertEqual(MathLib.mul(123, 456), 56088)
        self.assertEqual(MathLib.mul(537891, 65219), 35080713129)
        self.assertEqual(MathLib.mul(111111111111111, 222222222222222), 24691358024691308641975308642)

        # Negative integer numbers
        self.assertEqual(MathLib.mul(-1, -1), 1)
        self.assertEqual(MathLib.mul(-123, -456), 56088)
        self.assertEqual(MathLib.mul(-537891, -65219), 35080713129)
        self.assertEqual(MathLib.mul(-111111111111111, -222222222222222), 24691358024691308641975308642)

        # Mixed integer numbers
        self.assertEqual(MathLib.mul(-1, 1), -1)
        self.assertEqual(MathLib.mul(-123, 456), -56088)
        self.assertEqual(MathLib.mul(-537891, 65219), -35080713129)
        self.assertEqual(MathLib.mul(-111111111111111, 222222222222222), -24691358024691308641975308642)

    def test_mul_float(self):
        # Positive integer numbers
        self.assertEqual(MathLib.mul(1, 1), 1)
        self.assertEqual(MathLib.mul(123, 456), 56088)
        self.assertEqual(MathLib.mul(537891, 65219), 35080713129)
        self.assertEqual(MathLib.mul(111111111111111, 222222222222222), 24691358024691308641975308642)

        # Negative integer numbers
        self.assertEqual(MathLib.mul(-1, -1), 1)
        self.assertEqual(MathLib.mul(-123, -456), 56088)
        self.assertEqual(MathLib.mul(-537891, -65219), 35080713129)
        self.assertEqual(MathLib.mul(-111111111111111, -222222222222222), 24691358024691308641975308642)

        # Mixed integer numbers
        self.assertEqual(MathLib.mul(-1, 1), -1)
        self.assertEqual(MathLib.mul(-123, 456), -56088)
        self.assertEqual(MathLib.mul(-537891, 65219), -35080713129)
        self.assertEqual(MathLib.mul(-111111111111111, 222222222222222), -24691358024691308641975308642)

    def test_div(self):
        self.assertEqual(MathLib.div(1, 1), 1)

    def test_modulus(self):
        self.assertEqual(MathLib.mod(1, 1), 0)

    def test_exponentiation(self):
        self.assertEqual(MathLib.expo(1, 1), 1)

    def test_square_root(self):
        self.assertEqual(MathLib.sqrt(1, 1), 1)

    def test_factorial(self):
        self.assertEqual(MathLib.fact(1), 1)

if __name__ == '__main__':
    unittest.main()