from .printrsrgb import printrsrgb
import sys

__all__ = ["printrsrgb"]
__version__ = "0.1.0"

if __name__ == "__main__":
    printrsrgb("".join(map(str, sys.argv[1:])), rainbow=1)
    printrsrgb(sys.stdin.read(), rainbow=1)