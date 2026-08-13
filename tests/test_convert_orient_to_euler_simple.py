# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

import sys
import unittest
from unittest.mock import MagicMock

# The script imports omni.usd and carb, which are only present in an
# Omniverse Kit runtime. Provide lightweight mocks for unit testing.
sys.modules.setdefault('omni.usd', MagicMock())
sys.modules.setdefault('carb', MagicMock())

from pxr import Gf

from scripts.animation.convert_orient_to_euler_simple import ensure_euler_continuity


class TestEnsureEulerContinuity(unittest.TestCase):
    def test_small_diff_unchanged(self):
        seq = [(0, Gf.Vec3d(0, 10, 20)), (1, Gf.Vec3d(5, 15, 25))]
        out = ensure_euler_continuity(seq)
        self.assertEqual(len(out), 2)
        self.assertEqual(out[0][1], Gf.Vec3d(0, 10, 20))
        self.assertEqual(out[1][1], Gf.Vec3d(5, 15, 25))

    def test_wrap_positive(self):
        seq = [(0, Gf.Vec3d(0, 0, 0)), (1, Gf.Vec3d(0, 0, 200))]
        out = ensure_euler_continuity(seq)
        self.assertEqual(out[1][1], Gf.Vec3d(0, 0, -160))

    def test_wrap_negative(self):
        seq = [(0, Gf.Vec3d(0, 0, 0)), (1, Gf.Vec3d(0, 0, -200))]
        out = ensure_euler_continuity(seq)
        self.assertEqual(out[1][1], Gf.Vec3d(0, 0, 160))

    def test_multiple_wraps_stay_continuous(self):
        seq = [
            (0, Gf.Vec3d(0, 0, 0)),
            (1, Gf.Vec3d(0, 0, 200)),
            (2, Gf.Vec3d(0, 0, 400)),
            (3, Gf.Vec3d(0, 0, 600)),
        ]
        out = ensure_euler_continuity(seq)
        for i in range(1, len(out)):
            diff = out[i][1][2] - out[i - 1][1][2]
            self.assertLessEqual(abs(diff), 180, f'Frame {i} jump: {diff}')

    def test_short_sequence(self):
        self.assertEqual(ensure_euler_continuity([]), [])
        single = [(0, Gf.Vec3d(1, 2, 3))]
        self.assertEqual(ensure_euler_continuity(single), single)


if __name__ == '__main__':
    unittest.main()
