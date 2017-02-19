import unittest
import sympy
import Convergence
from sympy import *



class ConvergenceTest(unittest.TestCase):

    def test_is_convergent(self):
        n = Symbol("n")
        harmonic_n = "Sequence does not converge because harmonic comparison > 0"
        convergent_comp_y = "Sequence converges because comparison with convergent sequence >= 0"
        necessary_n = "Sequence does not converge by the necessary condition"
        cauchy_y = "Sequence converges because cauchy < 1"
        self.assertEqual(Convergence.is_convergent(1 / sympy.sqrt(10*n)), harmonic_n)
        self.assertEqual(Convergence.is_convergent(1 / (n+1)), harmonic_n)
        self.assertEqual(Convergence.is_convergent(1 / (n**2 + 1)), convergent_comp_y)
        self.assertEqual(Convergence.is_convergent(n / (n**2 + 1)), harmonic_n)
        self.assertEqual(Convergence.is_convergent(1 / cbrt(n + 6)), harmonic_n)
        self.assertEqual(Convergence.is_convergent((n+1)/n), necessary_n)
        self.assertEqual(Convergence.is_convergent(n / 2**n), cauchy_y)


if __name__ == '__main__':
    unittest.main()
