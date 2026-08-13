import pytest
from pxr import Usd, UsdGeom, Gf

from scripts.animation.convert_orient_to_euler_simple import (
    convert_orient_to_rotateXYZ,
)


def test_static_orient_conversion_no_duplicate_rotateXYZ():
    stage = Usd.Stage.CreateInMemory()
    xform = UsdGeom.Xform.Define(stage, "/Xform")
    prim = xform.GetPrim()

    orient_op = xform.AddOrientOp()
    orient_op.Set(Gf.Quatd(1.0, Gf.Vec3d(0.0, 0.0, 0.0)))

    assert convert_orient_to_rotateXYZ(prim, stage)

    order_attr = xform.GetXformOpOrderAttr()
    order = order_attr.Get() if order_attr else None
    tokens = list(order) if order else []

    assert "xformOp:orient" not in tokens
    rotate_xyz_tokens = [t for t in tokens if t == "xformOp:rotateXYZ"]
    assert len(rotate_xyz_tokens) == 1

    rotate_xyz_op = xform.GetRotateXYZOp()
    assert rotate_xyz_op.IsDefined()
