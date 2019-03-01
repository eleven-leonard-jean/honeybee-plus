"""Assign default Radiance materials to Honeybee Surface Types."""
from .material.plastic import Plastic
from .material.glass import Glass

from honeybee.surfacetype import SurfaceTypeBase, Wall, UndergroundWall, Roof, \
    UndergroundCeiling, Floor, UndergroundSlab, SlabOnGrade, ExposedFloor, Ceiling, \
    AirWall, Window, Context

SurfaceTypeBase.radiance_material = None

# TODO: move default materials to a separate file that can be edited by user.
Wall.radiance_material = Plastic.by_single_reflect_value("generic_wall", 0.50)
UndergroundWall.radiance_material = Plastic.by_single_reflect_value("generic_wall", 0.50)
Roof.radiance_material = Plastic.by_single_reflect_value("generic_roof", 0.80)
UndergroundCeiling.radiance_material = \
    Plastic.by_single_reflect_value("generic_wall", 0.5)
Floor.radiance_material = Plastic.by_single_reflect_value("generic_floor", 0.20)
UndergroundSlab.radiance_material = Plastic.by_single_reflect_value("generic_floor", 0.20)
SlabOnGrade.radiance_material = Plastic.by_single_reflect_value("generic_floor", 0.20)
ExposedFloor.radiance_material = Plastic.by_single_reflect_value("generic_floor", 0.20)
Ceiling.radiance_material = Plastic.by_single_reflect_value("generic_ceiling", 0.80)
AirWall.radiance_material = Glass.by_single_trans_value("generic_glass", 1.00)
Window.radiance_material = Glass.by_single_trans_value("generic_glass", 0.60)
Context.radiance_material = Plastic.by_single_reflect_value("generic_shading", 0.35)
