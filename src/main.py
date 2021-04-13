from settings import settings
from scanner import Scanner
import sys

import reconstructor


settings.load_settings(str(sys.argv[1]))
scanner = Scanner()
scanner.scan()
reconstructor.reconstruct()
