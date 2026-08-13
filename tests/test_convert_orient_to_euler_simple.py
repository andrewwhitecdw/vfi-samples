# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary

import sys
from pathlib import Path
from unittest import mock

import pytest

# Make the repo root importable so we can import scripts.animation.*.
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

# The module imports omni.usd and carb, which are only available inside an
# Omniverse Kit runtime. Mock them so the pure math helpers can be tested
# in a normal Python environment.
sys.modules["omni.usd"] = mock.MagicMock()
sys.modules["carb"] = mock.MagicMock()

from pxr import Gf

from scripts.animation.convert_orient_to_euler_simple import detect_gimbal_lock


def test_detect_gimbal_lock_near_90():
    assert detect_gimbal_lock(Gf.Vec3d(0.0, 89.0, 0.0), "XYZ", threshold=85.0) is True
    assert detect_gimbal_lock(Gf.Vec3d(0.0, -89.0, 0.0), "XYZ", threshold=85.0) is True


def test_detect_gimbal_lock_far_from_90():
    assert detect_gimbal_lock(Gf.Vec3d(0.0, 45.0, 0.0), "XYZ", threshold=85.0) is False


def test_detect_gimbal_lock_default_threshold():
    assert detect_gimbal_lock(Gf.Vec3d(0.0, 86.0, 0.0), "XYZ") is True
    assert detect_gimbal_lock(Gf.Vec3d(0.0, 84.0, 0.0), "XYZ") is False


def test_detect_gimbal_lock_threshold_clamped():
    # threshold > 90 must not produce a negative tolerance.
    assert detect_gimbal_lock(Gf.Vec3d(0.0, 89.0, 0.0), "XYZ", threshold=100.0) is False
    # threshold < 0 must not blow up the tolerance beyond 90.
    assert detect_gimbal_lock(Gf.Vec3d(0.0, 0.0, 0.0), "XYZ", threshold=-10.0) is False
    assert detect_gimbal_lock(Gf.Vec3d(0.0, 45.0, 0.0), "XYZ", threshold=-10.0) is True

