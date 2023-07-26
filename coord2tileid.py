#!/usr/bin/env python

from __future__ import division
import argparse

def latlon_to_tile_id(latitude, longitude, lod):
    '''returns tile's x and y containing the given point'''
    sizeX = 2 ** (lod + 1)
    sizeY = 2 ** lod

    degreesPerTileUnitX = 360 / sizeX
    degreesPerTileUnitY = 180 / sizeY

    targetX = (180 + longitude) / degreesPerTileUnitY
    targetY = ( 90 - latitude)  / degreesPerTileUnitX

    tileX = 0 if targetX < 0 else min(int(targetX), sizeX - 1)
    tileY = 0 if targetY < 0 else min(int(targetY), sizeY - 1)

    return tileX, tileY

# Function not used currently...
# def tileIdsForBBox(latlon1, latlon2, lod):
#     '''returns a list of tile ids [(x, y, lod)] covering the given aabbox'''
#     tileX1, tileY1 = latlongToTileID(latlon1[0], latlon1[1], lod)
#     tileX2, tileY2 = latlongToTileID(latlon2[0], latlon2[1], lod)
#     result = []
#     for x in range(min(tileX1, tileX2), max(tileX1, tileX2) + 1):
#         for y in range(min(tileY1, tileY2), max(tileY1, tileY2) + 1):
#             result.append((x, y, lod))
#     return result;

def main():
    parser = argparse.ArgumentParser(
        description='Converts lat/lon coordinates (in degrees) to an x/y tile ID (at any lod)',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('latitude', type=float, help='latitude of a point')
    parser.add_argument('longitude', type=float, help='longitude of a point')
    parser.add_argument('lod', nargs='?', type=int, default=13, help='desired lod of the tile, optional, default=13')
    args = parser.parse_args()

    lod = args.lod
    print("(x, y)@lod{} = {}".format(lod, latlon_to_tile_id(args.latitude, args.longitude, lod)))

if __name__ == '__main__':
    main()
