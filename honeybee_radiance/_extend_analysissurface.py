from honeybee._hbanalysissurface import HBAnalysisSurface

from .radfile import RadFile
from .material.glass import Glass
from .material.glow import Glow
from .material.plastic import Plastic
from .material.metal import Metal


@classmethod
def from_json(cls, srf_json):
    """Create a surface from json object.

    The minimum schema is:
        {"name": "",
        "vertices": [[(x, y, z), (x1, y1, z1), (x2, y2, z2)]],
        "surface_material": {},  // radiance material json file
            "surface_type": null  // 0: wall, 5: window
        }
    """
    name = srf_json["name"]
    vertices = srf_json["vertices"]
    type_id = srf_json["surface_type"]
    srf_type = surfacetype.SurfaceTypes.get_type_by_key(type_id)
    HBsrf = cls(name, vertices, srf_type)
    # Check material type and determine appropriate "from_json" classmethod
    if "surface_material" in srf_json.keys():
        material_json = srf_json["surface_material"]
        type = material_json["type"]
        if type == "plastic":
            radiance_material = Plastic.from_json(material_json)
        elif type == "metal":
            radiance_material = Metal.from_json(material_json)
        elif type == "glass":
            radiance_material = Glass.from_json(material_json)
        else:
            # raise ValueError "The material type {} in the surface json is either
            # not currently suported or incorrect"
            # .format(srf_json["surface_material"])
            radiance_material = None
        HBsrf.radiance_material = radiance_material
    return HBsrf


HBAnalysisSurface.from_json = from_json
