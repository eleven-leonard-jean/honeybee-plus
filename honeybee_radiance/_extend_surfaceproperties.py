from honeybee.surfaceproperties import SurfaceProperties
from .properties import RadianceProperties

#  add radiance properties to SurfaceProperties in honeybee-core


@property
def radiance_properties(self):
    """Get and set Radiance properties."""
    return self._rad_properties


@radiance_properties.setter
def radiance_properties(self, rad_properties):
    rad_properties = rad_properties or \
        RadianceProperties(self.surface_type.radiance_material)
    assert hasattr(rad_properties, 'isRadianceProperties'), \
        "%s is not a valid RadianceProperties" % str(rad_properties)
    if rad_properties.material is None:
        rad_properties.material = self.surface_type.radiance_material
    self._rad_properties = rad_properties


def rad_material_from_type(self):
    """Get default radiance material for the surface type."""
    return self.surface_type.radiance_material


if not hasattr('radiance_properties', SurfaceProperties):
    SurfaceProperties.radiance_properties = radiance_properties

if not hasattr('rad_material_from_type', SurfaceProperties):
    SurfaceProperties.rad_material_from_type = rad_material_from_type
