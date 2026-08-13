# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

"""
Tests for convert_orient_to_euler_simple.
"""

import pytest
from pxr import Usd, UsdGeom, Gf
from scripts.animation.convert_orient_to_euler_simple import (
    convert_orient_to_rotateXYZ,
)


def _ordered_op_types(prim):
    return [op.GetOpType() for op in UsdGeom.Xformable(prim).GetOrderedXformOps()]


def test_static_orient_creates_single_rotate_xyz():
    stage = Usd.Stage.CreateInMemory()
    prim = stage.DefinePrim("/Test")
    xformable = UsdGeom.Xformable(prim)

    orient_op = xformable.AddOrientOp()
    orient_op.Set(Gf.Quatd(0.70710678, 0.0, 0.70710678, 0.0))
    xformable.SetXformOpOrder([orient_op])

    assert convert_orient_to_rotateXYZ(prim, stage) is True

    op_types = _ordered_op_types(prim)
    assert UsdGeom.XformOp.TypeOrient not in op_types
    assert op_types.count(UsdGeom.XformOp.TypeRotateXYZ) == 1

    rotate_xyz = next(
        op for op in UsdGeom.Xformable(prim).GetOrderedXformOps()
        if op.GetOpType() == UsdGeom.XformOp.TypeRotateXYZ
    )
    assert rotate_xyz.Get() is not None


def test_static_orient_reuses_existing_rotate_xyz_no_duplicate():
    stage = Usd.Stage.CreateInMemory()
    prim = stage.DefinePrim("/Test")
    xformable = UsdGeom.Xformable(prim)

    rotate_xyz_op = xformable.AddRotateXYZOp()
    rotate_xyz_op.Set(Gf.Vec3d(10.0, 20.0, 30.0))

    orient_op = xformable.AddOrientOp()
    orient_op.Set(Gf.Quatd(0.5, 0.5, 0.5, 0.5).GetNormalized())

    assert convert_orient_to_rotateXYZ(prim, stage) is True

    op_types = _ordered_op_types(prim)
    assert UsdGeom.XformOp.TypeOrient not in op_types
    assert op_types.count(UsdGeom.XformOp.TypeRotateXYZ) == 1
