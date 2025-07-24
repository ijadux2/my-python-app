#!/usr/bin/env python3
import os
import shutil

def disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    print(f"Disk usage for {path}:")
    print(f"  Total: {total // (2**30)} GiB")
    print(f"  Used:  {used // (2**30)} GiB")
    print(f"  Free:  {free // (2**30)} GiB")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        disk_usage(sys.argv[1])
    else:
        disk_usage()
        
