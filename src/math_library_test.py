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
        # Positive float numbers
        self.assertAlmostEqual(MathLib.mul(1.23, 1.98), 2.4354, 4)
        self.assertAlmostEqual(MathLib.mul(123.2124, 456.9019), 56295.9796636, 4)
        self.assertAlmostEqual(MathLib.mul(537891.1234, 65219.4321), 35080953599.77902114, 4)
        self.assertAlmostEqual(MathLib.mul(111111111111111.111111111111111, 222222222222222.222222222222222), 24691358024691358024691358024.641975308641975, 4)

        # Negative float numbers
        self.assertAlmostEqual(MathLib.mul(-1.23, -1.98), 2.4354, 4)
        self.assertAlmostEqual(MathLib.mul(-123.2124, -456.9019), 56295.9796636, 4)
        self.assertAlmostEqual(MathLib.mul(-537891.1234, -65219.4321), 35080953599.77902114, 4)
        self.assertAlmostEqual(MathLib.mul(-111111111111111.111111111111111, -222222222222222.222222222222222), 24691358024691358024691358024.641975308641975, 4)

        # Mixed float numbers
        self.assertAlmostEqual(MathLib.mul(-1.23, 1.98), -2.4354, 4)
        self.assertAlmostEqual(MathLib.mul(-123.2124, 456.9019), -56295.9796636, 4)
        self.assertAlmostEqual(MathLib.mul(-537891.1234, 65219.4321), -35080953599.77902114, 4)
        self.assertAlmostEqual(MathLib.mul(-111111111111111.111111111111111, 222222222222222.222222222222222), -24691358024691358024691358024.641975308641975, 4)

    def test_div_int(self):
        # Division by zero
        with self.assertRaises(ZeroDivisionError):
            MathLib.div(1, 0)
            MathLib.div(125, 0)
            MathLib.div(-1, 0)

        # Positive integer numbers
        self.assertEqual(MathLib.div(1, 1), 1)
        self.assertEqual(MathLib.div(0, 456), 0)
        self.assertEqual(MathLib.div(521752, 65219), 8)
        self.assertEqual(MathLib.div(222222222222222, 111111111111111), 2)

        # Negative integer numbers
        self.assertEqual(MathLib.div(-1, -1), 1)
        self.assertEqual(MathLib.div(0, -456), 0)
        self.assertEqual(MathLib.div(-521752, -65219), 8)
        self.assertEqual(MathLib.div(-222222222222222, -111111111111111), 2)

        # Mixed integer numbers
        self.assertEqual(MathLib.div(-1, 1), -1)
        self.assertEqual(MathLib.div(0, 456), 0)
        self.assertEqual(MathLib.div(-521752, 65219), -8)
        self.assertEqual(MathLib.div(-222222222222222, 111111111111111), -2)

    def test_div_float(self):
        # Division by zero
        with self.assertRaises(ZeroDivisionError):
            MathLib.div(1, 0.0000)
            MathLib.div(125, 0.0000)
            MathLib.div(-1, 0.0000)

        # Positive float numbers
        self.assertAlmostEqual(MathLib.div(1.23, 1.98), 0.6212, 4)
        self.assertAlmostEqual(MathLib.div(123.2124, 456.9019), 0.26966926598, 4)
        self.assertAlmostEqual(MathLib.div(537891.1234, 65219.4321), 8.24740581266, 4)
        self.assertAlmostEqual(MathLib.div(111111111111111.111111111111111, 222222222222222.222222222222222), 0.5000, 4)

        # Negative float numbers
        self.assertAlmostEqual(MathLib.div(-1.23, -1.98), 0.6212, 4)
        self.assertAlmostEqual(MathLib.div(-123.2124, -456.9019), 0.26966926598, 4)
        self.assertAlmostEqual(MathLib.div(-537891.1234, -65219.4321), 8.24740581266, 4)
        self.assertAlmostEqual(MathLib.div(-111111111111111.111111111111111, -222222222222222.222222222222222), 0.5000, 4)

        # Mixed float numbers
        self.assertAlmostEqual(MathLib.div(-1.23, 1.98), -0.6212, 4)
        self.assertAlmostEqual(MathLib.div(-123.2124, 456.9019), -0.26966926598, 4)
        self.assertAlmostEqual(MathLib.div(-537891.1234, 65219.4321), -8.24740581266, 4)
        self.assertAlmostEqual(MathLib.div(-111111111111111.111111111111111, 222222222222222.222222222222222), -0.5000, 4)


    def test_mod_int(self):
        # Modulo by zero
        with self.assertRaises(ZeroDivisionError):
            MathLib.mod(1, 0)
            MathLib.mod(125, 0)
            MathLib.mod(-1, 0)

        # Positive integer numbers
        self.assertEqual(MathLib.mod(1, 1), 0)
        self.assertEqual(MathLib.mod(0, 456), 0)
        self.assertEqual(MathLib.mod(521755, 65219), 3)
        self.assertEqual(MathLib.mod(232222222222222, 111111111111111), 10000000000000)

        # Negative integer numbers
        self.assertEqual(MathLib.mod(-1, -1), 0)
        self.assertEqual(MathLib.mod(0, -456), 0)
        self.assertEqual(MathLib.mod(-521755, -65219), -3)
        self.assertEqual(MathLib.mod(-232222222222222, -111111111111111), -10000000000000)

        # Mixed integer numbers
        self.assertEqual(MathLib.mod(-1, 1), 0)
        self.assertEqual(MathLib.mod(0, 456), 0)
        self.assertEqual(MathLib.mod(-521755, 65219), 65216)
        self.assertEqual(MathLib.mod(-232222222222222, 111111111111111), 101111111111111)
        self.assertEqual(MathLib.mod(1, 1), 0)

    def test_div_float(self):
        # Modulo by zero
        with self.assertRaises(ZeroDivisionError):
            MathLib.mod(1, 0.0000)
            MathLib.mod(125, 0.0000)
            MathLib.mod(-1, 0.0000)

        # Positive float numbers
        self.assertAlmostEqual(MathLib.mod(1.23, 1.98), 1.23, 4)
        self.assertAlmostEqual(MathLib.mod(123.2124, 456.9019), 123.2124, 4)
        self.assertAlmostEqual(MathLib.mod(537891.1234, 65219.4321), 16135.6666, 4)
        self.assertAlmostEqual(MathLib.mod(111111111111111.111111111111111, 222222222222222.222222222222222), 111111111111111.111111111111111, 4)

        # Negative float numbers
        self.assertAlmostEqual(MathLib.mod(-1.23, -1.98), -1.23, 4)
        self.assertAlmostEqual(MathLib.mod(-123.2124, -456.9019), -123.2124, 4)
        self.assertAlmostEqual(MathLib.mod(-537891.1234, -65219.4321), -16135.6666, 4)
        self.assertAlmostEqual(MathLib.mod(-111111111111111.111111111111111, -222222222222222.222222222222222), -111111111111111.111111111111111, 4)

        # Mixed float numbers
        self.assertAlmostEqual(MathLib.mod(-1.23, 1.98), 0.75, 4)
        self.assertAlmostEqual(MathLib.mod(-123.2124, 456.9019), 333.6895, 4)
        self.assertAlmostEqual(MathLib.mod(-537891.1234, 65219.4321), 49083.76549999994, 4)
        self.assertAlmostEqual(MathLib.mod(-111111111111111.111111111111111, 222222222222222.222222222222222), 111111111111111.111111111111111, 4)

    def test_expo_int(self):
        # Negative exponent
        with self.assertRaises(ValueError):
            MathLib.expo(1, -1)
            MathLib.expo(125, -5)
            MathLib.expo(-1, -123232)

        self.assertEqual(MathLib.expo(1, 1), 1)
        self.assertEqual(MathLib.expo(0, 456), 0)
        self.assertEqual(MathLib.expo(3, 2), 9)
        self.assertEqual(MathLib.expo(10, 3), 1000)
        self.assertEqual(MathLib.expo(120, 5), 24883200000)
        self.assertEqual(MathLib.expo(30, 30), 205891132094649000000000000000000000000000000)

    def test_expo_float(self):
        # Negative exponent
        with self.assertRaises(ValueError):
            MathLib.expo(1, -1.2351)
            MathLib.expo(125, -5.091242)
            MathLib.expo(-1, -123232.12)

        self.assertEqual(MathLib.expo(1, 1.51), 1)
        self.assertEqual(MathLib.expo(0, 456), 0)
        self.assertAlmostEqual(MathLib.expo(3, 2.25), 11.844666116572432, 4)
        self.assertAlmostEqual(MathLib.expo(10, 3.9120), 8165.823713585923, 4)
        self.assertAlmostEqual(MathLib.expo(120.12, 5.1287), 46315153715.671974, 4)
        self.assertAlmostEqual(MathLib.expo(10.1, 10.1), 13920212824.5650399, 4)

    def test_sqrt_int(self):
        # Negative exponent
        with self.assertRaises(ValueError):
            MathLib.sqrt(1, -1)
            MathLib.sqrt(125, -5)
            MathLib.sqrt(-1, -123232)

        self.assertEqual(MathLib.sqrt(1, 1), 1)
        self.assertEqual(MathLib.sqrt(0, 456), 0)
        self.assertEqual(MathLib.sqrt(9, 2), 3)
        self.assertAlmostEqual(MathLib.sqrt(1000, 3), 10, 0)
        self.assertAlmostEqual(MathLib.sqrt(24883200000, 5), 120, 0)
        self.assertEqual(MathLib.sqrt(205891132094649000000000000000000000000000000, 30), 30)


    def test_sqrt_float(self):
        # Negative square root
        with self.assertRaises(ValueError):
            MathLib.sqrt(1, -1.2351)
            MathLib.sqrt(125, -5.091242)
            MathLib.sqrt(-1, -123232.12)

        self.assertEqual(MathLib.sqrt(1.51, 1), 1.51)
        self.assertAlmostEqual(MathLib.sqrt(11.844666116572432, 2.25), 3, 4)
        self.assertAlmostEqual(MathLib.sqrt(8165.823713585923, 3.9120), 10, 4)
        self.assertAlmostEqual(MathLib.sqrt(46315153715.671974, 5.1287), 120.12, 4)
        self.assertAlmostEqual(MathLib.sqrt(13920212824.5650399, 10.1), 10.1, 4)


    def test_factorial(self):
        # Negative factorial
        with self.assertRaises(ValueError):
            MathLib.fact(-1)
            MathLib.fact(-5)
            MathLib.fact(-123232)

        self.assertEqual(MathLib.fact(0), 1)
        self.assertEqual(MathLib.fact(1), 1)
        self.assertEqual(MathLib.fact(5), 120)
        self.assertEqual(MathLib.fact(10), 3628800)
        self.assertEqual(MathLib.fact(25), 15511210043330985984000000)
        self.assertEqual(MathLib.fact(50), 30414093201713378043612608166064768844377641568960512000000000000)

if __name__ == '__main__':
    unittest.main()