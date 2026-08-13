import unittest

from pxr import Gf


class TestQuaternionDotProduct(unittest.TestCase):
    def test_imaginary_dot_matches_manual_calculation(self):
        """Verify Gf.Dot on quaternion imaginary parts matches the old manual sum."""
        q1 = Gf.Quatd(1.0, Gf.Vec3d(0.1, 0.2, 0.3))
        q2 = Gf.Quatd(0.5, Gf.Vec3d(0.4, 0.5, 0.6))

        manual = (
            q1.GetImaginary()[0] * q2.GetImaginary()[0]
            + q1.GetImaginary()[1] * q2.GetImaginary()[1]
            + q1.GetImaginary()[2] * q2.GetImaginary()[2]
        )
        dot = Gf.Dot(q1.GetImaginary(), q2.GetImaginary())

        self.assertAlmostEqual(manual, dot)


if __name__ == "__main__":
