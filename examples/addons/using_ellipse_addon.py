# Purpose: examples for using ellipse() add-on
# Copyright (c) 2018, Manfred Moitzi
# License: MIT License
from __future__ import unicode_literals
from math import radians
import ezdxf
from ezdxf.addons import ellipse
from ezdxf.algebra import Matrix44

NAME = 'ellipse.dxf'
dwg = ezdxf.new('R12')
msp = dwg.modelspace()


def render(points):
    msp.add_polyline2d(list(points))


def tmatrix(x, y, angle):
    return Matrix44.chain(
        Matrix44.z_rotate(radians(angle)),
        Matrix44.translate(x, y, 0),
    )


for axis in [0.5, 0.75, 1., 1.5,  2., 3.]:
    render(ellipse(200, rx=5., ry=axis))

attribs = {
    'color': 1,
    'linetype': 'DASHDOT',
}

msp.add_line((-7, 0), (+7, 0), dxfattribs=attribs)
msp.add_line((0, -5), (0, +5), dxfattribs=attribs)

for rotation in [0, 30, 45, 60, 90]:
    m = tmatrix(20, 0, rotation)
    render(m.transform_vectors(ellipse(100, rx=5., ry=2.)))

for startangle in [0, 30, 45, 60, 90]:
    m = tmatrix(40, 0, startangle)
    render(m.transform_vectors(
        ellipse(90, rx=5., ry=2., start_param=radians(startangle), end_param= radians(startangle+90)))
    )
    render(m.transform_vectors(
        ellipse(90, rx=5., ry=2., start_param=radians(startangle+180), end_param= radians(startangle+270)))
    )

dwg.saveas(NAME)
print("drawing '%s' created.\n" % NAME)
