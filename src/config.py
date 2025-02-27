# PYMUSE -------------------------- PROTOTYPE VERSION V2
# NOT FINAL PRODUCT

from PySide6.QtWidgets import *
from ui import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import *
# from csv_funcs import * # for csv shit

# metadata shit
from mutagen.mp3 import *
from mutagen.id3 import *
from mutagen.wave import *
from mutagen.ogg import *
from mutagen.flac import *
from mutagen.m4a import *
from mutagen.aac import *
from mutagen.oggvorbis import *

# from pop_ups import * #<------- Will implement when coded
# from cd_play_funcs import * #<------- Will implement when coded

import sys
import os
import time
import random
from random import shuffle
import json