# Credits:
# - https://medium.com/@shivama205/audio-signals-comparison-23e431ed2207
# - http://www.randombytes.org/audio_comparison.html
# - https://oxygene.sk/2011/01/how-does-chromaprint-work/
# - https://yohanes.gultom.id/2018/03/24/simple-music-fingerprinting-using-chromaprint-in-python/
# - https://stackoverflow.com/a/55957642

import argparse
from correlation import correlate

def initialize():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i ", "--source-file", help="source file")
    parser.add_argument("-o ", "--target-file", help="target file")
    args = parser.parse_args()
  
    SOURCE_FILE = args.source_file if args.source_file else None
    TARGET_FILE = args.target_file if args.target_file else None
    if not SOURCE_FILE or not TARGET_FILE:
      raise Exception("Source or Target files not specified.")
    return SOURCE_FILE, TARGET_FILE
  
if __name__ == "__main__":
    SOURCE_FILE, TARGET_FILE = initialize()
    correlate(SOURCE_FILE, TARGET_FILE)
