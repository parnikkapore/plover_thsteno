#! /usr/bin/env python3 -i
# call tt() with the stroke to test the dictionary

import thsteno_base as thbase
import thsteno_fingerspelling as thfing

def tt(stroke):
    try: print("thbase:", thbase.lookup([stroke]))
    except KeyError as e:
        print("thbase: Not valid -", e)
    
    try: print("thfing:", thfing.lookup([stroke]))
    except KeyError as e:
        print("thfing: Not valid -", e)
