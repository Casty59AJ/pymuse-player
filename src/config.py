# PYMUSE -------------------------- PROTOTYPE VERSION V2
# NOT FINAL PRODUCT

from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QFileDialog
from ui import Ui_Win
from PySide6.QtCore import QUrl, QTime
from PySide6.QtGui import QIcon
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
# from csv_funcs import * # for csv shit

# metadata shit
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from mutagen.wave import WAVE
from mutagen.ogg import OggFileType
from mutagen.flac import FLAC
from mutagen.m4a import M4A
from mutagen.aac import AAC
from mutagen.oggvorbis import OggVorbis

# from pop_ups import * #<------- Will implement when coded
# from cd_play_funcs import * #<------- Will implement when coded

import sys
import os
import time
import random
from random import shuffle
import json