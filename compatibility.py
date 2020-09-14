from typing import Protocol, Union

class DjangoGEOSGeometry(Protocol):
    valid: bool

class ShapelyGeometry(Protocol):
    is_valid: bool

def check_validity(geometry: Union[DjangoGEOSGeometry, ShapelyGeometry]) -> bool:
    """
    Checks if the geometry is valid, in a way that is cross-compatible between
    shapely and django.
    """
    try:
        # geometry is a DjangoGEOSGeometry
        return geometry.valid
    except AttributeError:
        # geometry is a ShapelyGeometry
        return geometry.is_valid
