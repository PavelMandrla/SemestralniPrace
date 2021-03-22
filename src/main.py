#from settings import ScannerSettings
from settings import settings
from motor import Motor
from camera import Camera
from scanner import Scanner

settings.load_settings("../settings.js")
scanner = Scanner()
scanner.scan()
