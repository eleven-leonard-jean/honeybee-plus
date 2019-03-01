from honeybee.surfaceproperties import SurfaceState
from .radfile import RadFile

#  ---------------------------------------------------------------------
#  add radiance properties to SurfaceState in honeybee.SurfaceState
#  ---------------------------------------------------------------------


@property
def radiance_properties(self):
    """Get Radiance material from SurfaceProperties."""
    if not self._surface_properties:
        return None
    else:
        return self._surface_properties.radiance_properties


@property
def radiance_material(self):
    """Get Radiance material from SurfaceProperties."""
    if not self.radiance_properties:
        return None
    else:
        return self.radiance_properties.material


@property
def radiance_black_material(self):
    """Get Radiance black material from SurfaceProperties."""
    if not self.radiance_properties:
        return None
    else:
        return self.radiance_properties.balck_material


# TODO(mostapha): Each surface should only have a single material. This method
# can be really confusing.
def radiance_materials(self, blacked=False, to_rad_string=False):
    """Get the full list of materials for surfaces."""
    mt_base = [srf.radiance_material for srf in self.surfaces]
    mt_child = [childSrf.radiance_material
                for srf in self.surfaces
                for childSrf in srf.children_surfaces
                if srf.has_child_surfaces]
    mt = set(mt_base + mt_child)
    return '\n'.join(m.to_rad_string() for m in mt) if to_rad_string else tuple(mt)


def to_rad_string(self, mode=1, include_materials=False,
                  flipped=False, blacked=False):
    """Get surfaces as a RadFile. Use str(to_rad_string) to get the full str.

    Args:
        mode: An integer 0-2 (Default: 1)
            0 - Do not include children surfaces.
            1 - Include children surfaces.
            2 - Only children surfaces.
        include_materials: Set to False if you only want the geometry definition
            (default:True).
        flipped: Flip the surface geometry.
        blacked: If True materials will all be set to plastic 0 0 0 0 0.
    """
    if not self.surfaces:
        return ''
    mode = 1 if mode is None else mode
    return RadFile(self.surfaces).to_rad_string(mode, include_materials,
                                                flipped, blacked)


if not hasattr('radiance_properties', SurfaceState):
    SurfaceState.rad_properties = radiance_properties

if not hasattr('radiance_material', SurfaceState):
    SurfaceState.radiance_material = radiance_material

if not hasattr('radiance_black_material', SurfaceState):
    SurfaceState.radiance_black_material = radiance_black_material

if not hasattr('radiance_materials', SurfaceState):
    SurfaceState.radiance_materials = radiance_materials

if not hasattr('to_rad_string', SurfaceState):
    SurfaceState.to_rad_string = to_rad_string
