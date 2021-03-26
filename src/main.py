from settings import settings
from scanner import Scanner
import sys


settings.load_settings(str(sys.argv[1]))
scanner = Scanner()
scanner.scan()
