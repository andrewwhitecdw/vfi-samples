# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.
#

"""Regression tests for convert_orient_to_euler_simple."""

import os
import sys
import unittest
from unittest.mock import MagicMock

# The conversion logic only needs pxr; avoid a hard Kit runtime dependency.
sys.modules.setdefault("omni.usd", MagicMock())
sys.modules.setdefault("carb", MagicMock())

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pxr import Usd, UsdGeom, Gf

from scripts.animation.convert_orient_to_euler_simple import (
    convert_orient_to_rotateXYZ,
)


class TestStaticOrientDefault(unittest.TestCase):
    def test_zero_quaternion_default_is_converted(self):
        stage = Usd.Stage.CreateInMemory()
        xform = UsdGeom.Xform.Define(stage, "/Xform")
        xform.AddOrientOp().Set(Gf.Quatd(0.0, 0.0, 0.0, 0.0))

        self.assertTrue(convert_orient_to_rotateXYZ(xform.GetPrim(), stage))

        rotate_xyz_attr = xform.GetPrim().GetAttribute("xformOp:rotateXYZ")
        self.assertTrue(rotate_xyz_attr.IsValid())
        rotate_xyz = rotate_xyz_attr.Get()
        self.assertIsNotNone(rotate_xyz)
        for axis in range(3):
            self.assertAlmostEqual(rotate_xyz[axis], 0.0, places=5)

        orient_attr = xform.GetPrim().GetAttribute("xformOp:orient")
        self.assertIsNone(orient_attr.Get())

        op_types = [
            op.GetOpType()
            for op in UsdGeom.Xformable(xform.GetPrim()).GetOrderedXformOps()
        ]
        self.assertNotIn(UsdGeom.XformOp.TypeOrient, op_types)
        self.assertIn(UsdGeom.XformOp.TypeRotateXYZ, op_types)

    def test_unauthored_default_is_not_converted(self):
        stage = Usd.Stage.CreateInMemory()
        xform = UsdGeom.Xform.Define(stage, "/Xform")
        xform.AddOrientOp()

        self.assertFalse(convert_orient_to_rotateXYZ(xform.GetPrim(), stage))
        self.assertFalse(
            xform.GetPrim().GetAttribute("xformOp:rotateXYZ").IsValid()
        )

