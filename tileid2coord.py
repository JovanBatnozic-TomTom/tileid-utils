#!/usr/bin/env python

from __future__ import division
import argparse

def tile_id_to_latlon(x, y, lod):
    sizeX = 2 ** (lod + 1)
    sizeY = 2 ** lod

    degreesPerTileUnitX = 360 / sizeX
    degreesPerTileUnitY = 180 / sizeY

    lat = (y * degreesPerTileUnitY - 90) * -1
    lon = (x * degreesPerTileUnitX - 180)
    
    return lat, lon

def main():
    parser = argparse.ArgumentParser(
        description='Converts an x/y tile ID (at lod 13) to lat/lon coordinates (in degrees)',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('x', type=float, help='tile_id.x')
    parser.add_argument('y', type=float, help='tile_id.y')
    # parser.add_argument('lod', nargs='?', type=int, default=13, help='desired lod of the tile, optional, default=13')
    args = parser.parse_args()

    lod = 13
    print("(lat, lon)@lod13 = {}".format(tile_id_to_latlon(args.x, args.y, lod)))

if __name__ == '__main__':
    main()
