import argparse
def to_packed_tile_id(level, x, y):
  highest_level = 15
  result = 1 << (highest_level - level + 1)
  level_mask = 1 << level
  result |= (~x & level_mask) >> level
  if level > 0:
    level -= 1
    level_mask >>= 1
    result <<= 1
    result |= (y & level_mask) >> level
    result <<= 1
    result |= (x & level_mask) >> level
    y = ~y
    while level > 0:
      level -= 1
      level_mask >>= 1;
      result <<= 1;
      result |= (y & level_mask) >> level;
      result <<= 1;
      result |= (x & level_mask) >> level;
  return result
parser = argparse.ArgumentParser(description='Converts tile id (level, x, y) to NDS packed tile id.')
parser.add_argument('--level', type=int, choices=range(0, 16), default=13)
parser.add_argument('--x', type=int, required=True)
parser.add_argument('--y', type=int, required=True)
args = parser.parse_args()
print(to_packed_tile_id(level=args.level, x=args.x, y=args.y))