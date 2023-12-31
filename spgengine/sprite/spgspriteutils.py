from pygame import Surface, Rect
from pygame.transform import *
from pygame.math import Vector2
from math import degrees, atan2, sqrt

def point_at(point: Vector2, target_point: Vector2, angle_offset: float = 0):
    '''
    Returns the angle from the origin point to the target point.

    Argument List:
     - point:        (origin point)
     - target_point: (To be pointed at)
     - angle_offset: (Optional, added on the resulting angle)
    '''

    x_distance = target_point.x - point.x
    y_distance = target_point.y - point.y
    angle = degrees(atan2(y_distance, x_distance))
    return angle + angle_offset

def rotate_around_center(surface: Surface, angle: float, center_point: tuple[int, int]) -> [Surface, Rect]:
    '''
    Rotates image by given angle. Returns new surface and rect.
    
    "center_point" is based on world coordinates.

    Notes:
    Since pygame's Y coordinate is inverted, the angle is inverted aswell. This was solved by
    making the angle negative in this function.
    '''
    
    surf = rotate(
        surface,
        -angle
    )
    rect = surf.get_rect(center = center_point)

    return [surf, rect]

def get_position_from_origin(origin: Vector2, angle: float, distance_from_center: int) -> Vector2:
    '''
    Returns a coordinate n distance away from an origin point at a given angle.
    '''
    offset = Vector2()
    offset.from_polar((distance_from_center, angle))
    
    return origin + offset 

# physics / movement

def lerp(origin: Vector2, target: Vector2, speed: int = 20) -> Vector2:
    return Vector2(
        (target.x - origin.x) / speed,
        (target.y - origin.y) / speed
    )