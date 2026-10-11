import os
import datetime
from xml.sax.saxutils import escape

# Seamless Borderless Braille Art (60 lines)
BRAILLE_ART_RAW = [
    "",
    "",
    "",
    "                                 ⢟⣭⣴⣾  ⠟⠛⠉⠁⠂⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠉⠳⣌⠻ ⣾⣽",
    "                                   ⠿⠛⣩⠔⠈⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠘⠿⠿",
    "             ⣟                 ⠿⢛⣭⠖⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠒⢭⣙⠿",
    "              ⣾⣟⠻           ⡿⢛⣥⡾⢋⣡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣮⡙⢿",
    "                 ⣷⣦⣭⣉⣉⣙⣉⣉⣉⡥⢆⣴⣿⣫⣶⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠐⡐⢝⠣⡝⢿",
    "                         ⢋⣴⣿⣯⣿⢿⡭⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣄⠀⠌⠱⣝⢮⢻",
    "                      ⠟⠋⢡⣿⣿⡿⣿⣷⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡌⠠⠊⢮⣣⢻",
    "                   ⠟⣫⣴⢞⢁⡿⢁⠌⠾⣿⣿⣿⣿⡄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣆⡐⠀⠋⣧⢿",
    "                ⡿⣫⣴⣿⠟⡡⠂⠎⡔⢡⡞⣽⠟⠋⠉⠙⠉⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢟⣿⡌⠄⠈⢻",
    "              ⡿⣫⣾⣿⡿⢁⡞⠁⢀⠈⠀⢋⠞⠁⠀⠀⠀⡀⣰⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠘⣿⡆⢑⠀⠹",
    "             ⣟⣴  ⡟⣠⠏⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠐⣰⣏⣴⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡿⠀⠢⠀⢨⢿",
    "                ⡟⢰⠏⠀⠀⠀⠀⢀⠂⠀⠀⠀⠀⠠⢰⣿⣿⣿⡼⠑⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢃⢞⡀⠱⡀⢣⣻",
    "               ⡿⢰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠋⣿⠁⣼⡇⠀⢀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢊⡱⢀⠰⡈⣷⣻",
    "               ⡇⠊⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠛⠃⡸⠁⣴⣿⣧⣴⢊⡀⣷⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠄⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢌⠣⡀⢡⢸⣡⢿",
    "               ⡅⡘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⠁⢰⣿⣿⢿⢏⣾⠇⣿⣦⠄⠀⠀⠂⠀⠀⠀⠀⠀⠋⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢲⢡⠀⠋⣇⠚",
    "             ⡿⠋⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⢸⣿⡏⣼⠟⡠⣿⡇⠂⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⢎⡀⢸⢸⡤",
    "            ⠏⠀⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠃⣼⠃⢧⠀⣰⡆⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⡅⠠⠂⣇",
    "          ⡟⢁⣴ ⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠃⢀⡏⠁⠘⣿⣿⣷⢸⡇⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡀⠂⢸⢱⡘",
    "         ⠏⢠⣾  ⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⠀⣇⢿⣿⡆⠇⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡄⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠁⠌⢸⡇",
    "        ⡏⣴    ⠁⠀⠀⡄⠀⠀⠥⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣦⡿⠝⢆⠻⠿⠀⠀⠱⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣆⠀⠀⡀⠘⣧⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣼⡇",
    "        ⣴    ⡇⠀⠀⠘⡀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣆⣈⣮⡁⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠀⠀⠀⠀⠙⠋⠀⠀⠐⡀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢼⢣",
    "             ⠁⠀⢀⣼⣷⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢌⠈⠛⠿⢿⣿⡻⠿⠟⣁⠀⢤⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠠⣤⡀⠀⠀⣠⣤⣀⠄⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⢈⣾",
    "            ⠏⠀⣴ ⣟⢿⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡆⠸⠂⣉⣳⢷⠭⠒⠷⠮⣬⣯⢒⣠⡀⠀⢤⠀⠀⢳⡀⠄⠀⠀⠀⠀⠠⣀⠀⠀⠀⠀⣀⠈⠛⠉⠀⣀⠄⡀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾",
    "          ⠟⣁⣴⣦   ⡎⠃⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣣⠀⠨⠐⠂⠀⠈⠹⠛⠏⠀⠀⠓⠀⠉⠰⣜⠳⣄⠈⢻⣤⠀⠀⠀⠀⠀⠻⠍⣀⠤⠀⠈⠡⠀⣄⡙⢛⠻⠷⣦⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸",
    "         ⣣⣾       ⣆⠀⢼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡍⠀⠀⢀⣠⡄⣶⠆⠧⠀⠠⢀⣰⣓⣲⣀⣄⢂⣠⣿⣷⣤⡘⠧⣄⡀⠈⢂⣤⡈⠀⠀⣀⣀⠀⠀⠀⠀⠀⠈⠉⠐⠀⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⠃⢈",
    "                   ⠀⢺⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⣿⣦⣀⠴⢦⡔⢀⡶⠆⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢩⣾⣿⢻⣷⣮⣿⣿⣶⣯⣾⣷⣶⣶⣬⣤⣀⡀⠀⠀⠐⢀⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⣣ ⠀",
    "                   ⣆⠩⠀⢰⠀⠀⠀⠀⠀⡀⢸⡀⢹⣿⣟⡿⣶⣶⣿⣶⣶⣷⣿⣿⣿⣿⣿⣿⣿⢯⢾⣿⣿⣜⣧⢻⣿⣿⣿⣿⣿⣿⣿⣮⣛⣙⠿⢿⠽⠋⣡⣖⡦⠄⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢋⢁  ⢰",
    "                    ⣧⠀⣼⣷⠀⠀⠀⠀⠀⢦⣷⣼⡿⣿⣿⣾⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣿⣿⣿⣎⢇⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣷⣶⣶⣷⣶⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⢡  ⣏⣾",
    "                     ⣷⡟⠏⣼⣆⠃⠈⢀⣶⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢃⣴⠋⣠⠔⢁⠀⠀⠀⠀⠀⢤⡦⠃⣄",
    "                      ⣷⣀⡹⢿⡆⣇⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡫⢒⣡⣴⣋⠀⠀⠀⣠⡘⠈⣴⡀⢻",
    "                      ⣷⠛⢷⣌⣃⡈⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⠿⢟⣛⣛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢀⡆⡽⣹⠆⡿⢠",
    "                       ⣗⢦⡉⢿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⡀⠙⢿⡿⣿⠟⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣿⠛⠡⠍⣡⠞⢁",
    "                        ⣎⢿⣦⢻⡼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢷⣼⣿⣿⣿⣶⣾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⡟⡼⢶⠞⢉⢠",
    "                         ⣮⣛⣛⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⢣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢁⡟⣡⢺⢣",
    "                            ⣷⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣣⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣸⣾⠗⣡",
    "                             ⣆⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⡉⡡⢴⠪⣝⠳⠮⢭⣑⢉⣉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢰⣶⣶",
    "                              ⡌⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣉⠀⠀⣀⣀⢤⡤⣤⣤⣤⣤⣤⣤⢤⣄⣈⠀⠀⠨⠙⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢠",
    "                               ⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡻⢭⣿⣷⣿⣟⣿⣟⣯⣿⣾⣽⣿⣶⣶⣦⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢡",
    "                               ⡗⡆⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢠",
    "                               ⡇⢟⢧⣈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⡀",
    "                               ⣧⢸⣷⣭⢶⡌⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢃⣠⣾⢠",
    "                                ⢸⣿⣿⣯⢿⣦⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣡⣴⢟⣭⠇⣼",
    "                                ⠈⣿⣿⣿⣷⣻⣿⣦⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢉⣠⠞⣛⣵⣿⣿⢀",
    "                            ⠿⣟⣻⣟⡁⢿⣿⣿⣿⣇⢿⣿⣤⠓⢌⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣡⠔⠋⣤⣶⣿⣿⣿⡏⢸",
    "                          ⣶⣾⣿⣿⡿⣫⣇⢈⣿⣿⣿⣿⣎⢿⣿⢮⣠⠙⠦⣙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢛⡩⡴⢛⡡⢖⣽⣿⣿⠿⣟⣉⣡⣭⣽ ⣶⠹",
    "                    ⣯⡿⣻ ⣛⣻⢿⠿⢋⣤⡾⢷⣿⡘⣻⣿⣿⣿⣿⡸⣿⣯⢻⣦⠱⣌⠒⡤⠀⠀⠀⢈⠉⣉⢉⢡⣀⢤⣶⣯⣷⠶⠛⣠⣿⣿⣭⣶        ⡇⢻",
    "                  ⡟⠹⠖⣻    ⠿⣵⠋⡠⢴⣡⢻⡇⢷⣽⣿⣿⣿⣷⢻⣿⣷⣿⣧⢩⣓⠌⢳⡘⡭⢎⡳⡜⢎⡶⠹⢚⣙⣭⣷⣾⣿⣿⣿⣿⣿⣿⣶⣭⣛⡿    ⢡⠘",
    "                 ⠏⡐⣶⣿⡇⠻ ⡟⣭⡍⣀⣴⣶⣿⣿⠈⣧⠸⣿⣞⢿⣿⣿⡧⣿⣷⣿⣿⣧⠹⡞⣆⠱⡙⣬⢣⢙⠠⣐⠶⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣏⡻⣿⣿⣿⣾⣝⠿ ⢸⢰⢻",
    "                ⠇⡼⢸⣿⣿⣟⠀⢯⣵⣿⣧⡉⠻⢿⣿⣿⢰⡿⠀⣿⣿⣯⡻⣿⣿⢹⣿⡿⣿⡹⣧⡹⠼⣄⠓⠬⣃⢆⠀⣿⣿⣿⣶⣽⡻⣿⣿⣿⣿⣿⣿⣹⣿⡜⣿⣿⣿⣿⣿⣾⢸⢸⡄⢻",
    "               ⠏⡼⣰⢿⣵⢻⣾⠀⢸⣿⣿⣿⣿⣷⣶⣶⠍⠂⣐⡀⢙⢿⣿⣿⣮⢿⢸⣿⣷⡹⣷⡙⣷⣌⠳⢋⡁⠏⢎⢥⠘⠻⠟⠛⡉⠁⢠⠹⣿⣿⣿⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⢸⡚⣟⣆⢻",
    "              ⠋⣼⣵⣯⣟⣾⢳⣮⢆⠈⢿⣿⣿⡿⢟⠫⣀⣤⣅⢹⢠⢸⣮⢻⣿⣿⣿⣧⢻  ⣽⡇⢿⡟⣷⣾⣷⣌⡈⢆⢣⡉⠄⡑⠂⠈⠀⡴⠘⢿⣿⣿⣿⣿⣿⣇⣿⣿⣿⣿⣿⣮⣭⣝⢿⣦⠹",
    "             ⠃⢜⣽⣿⣦⣍⡋⠯⣾⡽⡄⠀⠉⠉⢀⢰⣾⡿⣛⡅⢸⠰⠘⣿⣷⡻⣿⣿⣿⣏⢿   ⠸⣷⠸⣿⣾⣻⣿⣦⡑⠌⢰⣶⣦⠀⣧⠨⡁⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣾⣿⣿⣟⣶⣝⣷⣍⠻",
    "            ⠇⢀⣼⣿⣿⣿⣿⣿⣷⣦⡹⠟⠂⠀⠄⠀⡀⢻⣾⣿⢸⡝⠀⢣⢹⣿⣷⡝⡻⣿⣿⣎  ⣟⢣⠹⣇⢻⣿⣿⣾⣽⡏⡖⣾⣿⢿⣧⠸⣧⠘⣦⠠⠻⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⠊⠿⢷⢹",
    "          ⡿⠃⣰⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠀⡐⠈⠐⡐⠀⠀⢿⢟⢸⣧⠀⢣⠄⢿⣿⣿⡕⡙⢿⣿⡌  ⣧⢹⡝⣦⣙⣻⣵⡟⢡⣼⢟⡽⢧⣿⠃⣽⢣⡀⢧⠱⠜⢿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠫⢖⡿⣿⣷⣛",
    "       ⠿⢛⡉⣀⣾⣿⣿⣿⣿⡿⠟⠋⠉⡀⠀⠄⠂⠤⢁⠃⠄⡁⠀⠘⣯⢸⡏⠐⡈⢖⠸⣿⣿⣧⢿⣎⢿⣿⢹  ⣧⢹⡾⢿⣿⠟⣰ ⣏⠞⣡⣿⢃⣶⣿⢸⢁⣌⠟⡸⢦⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⢳⢸ ⣮⢿",
    "   ⡿⠿⢋⡑⢎⡡⢦⣿⣿⡿⠟⠋⠁⡀⠄⢂⠡⢀⣥⡬⣌⠤⠁⣈⡀⠔⠀⠀⡼⣸⢣⠀⡅⠪⣅⢈⢿⣿⣎⢿⣎⢿⡆   ⣆⢿⣶⢹⣸  ⢪⣾⣿⢏⣾⣾⡿⢁⠾⠜⢠⠓⢚⠳⣬⠻⣿⣿⣿⣿⣿⡿⠃⢠⠂⡍⢸  ⢷⡻",
    "⠿⢛⡱⢈⠥⢣⠜⡢⢥⠿⠛⡉⠄⠂⢌⡐⢐⡈⠂⣀⣭⠬⠥⠒⣠⢾⣽⢻⡄⢁⠀⠠⢹⣮⠀⡜⠀⡐⠌⣧⡹ ⣎ ⠘ ⡸   ⡆⣷   ⣷  ⡏⢸⡿⠋⢠⣒⠒⣨⣴⣾ ⣶⣴⣷⣜⠿⠿⠟⢋⢀⡔⡡⢊⡄⠻ ⣻⣯ ⣜⢿",
]

def get_braille_tspans():
    tspans = []
    for i, line in enumerate(BRAILLE_ART_RAW):
        escaped_line = escape(line)
        tspans.append(f'<tspan x="0" y="{i * 10}">{escaped_line}</tspan>')
    return "\n".join(tspans)

def get_dots(text, length):
    text = str(text)
    just_len = max(0, length - len(text))
    if just_len <= 2:
        dot_map = {0: '', 1: ' ', 2: '. '}
        return dot_map.get(just_len, '')
    return ' ' + ('.' * just_len) + ' '

def build_svg(is_dark, stats=None):
    if stats is None:
        stats = {
            'age_data': '17 years, 7 months, 10 days',
            'repo_data': '21',
            'contrib_data': '21',
            'star_data': '25',
            'commit_data': '134',
            'follower_data': '5',
            'loc_data': '48,920',
            'loc_add': '52,140',
            'loc_del': '3,220'
        }

    # Color tokens matching Andrew Grant neofetch aesthetic
    if is_dark:
        bg_fill = "#161b22"
        text_fill = "#c9d1d9"
        title_color = "#58a6ff"
        key_color = "#ffa657"
        val_color = "#a5d6ff"
        add_color = "#3fb950"
        del_color = "#f85149"
        cc_color = "#616e7f"
        braille_fill = "#c9d1d9"
    else:
        bg_fill = "#f6f8fa"
        text_fill = "#24292f"
        title_color = "#0969da"
        key_color = "#953800"
        val_color = "#0a3069"
        add_color = "#1a7f37"
        del_color = "#cf222e"
        cc_color = "#8c959f"
        braille_fill = "#24292f"

    braille_tspans = get_braille_tspans()

    age_dots = get_dots(stats['age_data'], 50)
    repo_dots = get_dots(stats['repo_data'], 7)
    star_dots = get_dots(stats['star_data'], 15)
    commit_dots = get_dots(stats['commit_data'], 23)
    follower_dots = get_dots(stats['follower_data'], 10)
    loc_dots = get_dots(stats['loc_data'], 4)

    svg_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,monospace" width="985px" height="600px" font-size="14px" viewBox="0 0 985 600">
<style>
@font-face {{
  src: local('Consolas'), local('Consolas Bold');
  font-family: 'ConsolasFallback';
  font-display: swap;
  -webkit-size-adjust: 109%;
  size-adjust: 109%;
}}
.key {{fill: {key_color}; font-weight: 500;}}
.value {{fill: {val_color};}}
.addColor {{fill: {add_color};}}
.delColor {{fill: {del_color};}}
.cc {{fill: {cc_color};}}
.title {{fill: {title_color}; font-weight: bold;}}
text, tspan {{white-space: pre;}}
</style>
<rect width="985px" height="600px" fill="{bg_fill}" rx="15"/>

<!-- Seamless Borderless Braille Art -->
<g transform="translate(18, 15) scale(0.50, 0.96)" font-size="10px" font-family="monospace">
  <text x="0" y="0" fill="{braille_fill}">
{braille_tspans}
  </text>
</g>

<!-- Profile Specs & Live GitHub Stats -->
<text x="385" y="35" fill="{text_fill}">
<tspan x="385" y="35" class="title">securitygeek15@system</tspan> <tspan class="cc">-——————————————————————————————————————-—-</tspan>
<tspan x="385" y="60" class="cc">. </tspan><tspan class="key">OS</tspan>:<tspan class="cc"> ............................ </tspan><tspan class="value">Arch Linux, Windows 11</tspan>
<tspan x="385" y="80" class="cc">. </tspan><tspan class="key">Uptime</tspan>:<tspan class="cc" id="age_data_dots">{age_dots}</tspan><tspan class="value" id="age_data">{stats['age_data']}</tspan>
<tspan x="385" y="100" class="cc">. </tspan><tspan class="key">Host</tspan>:<tspan class="cc"> .......... </tspan><tspan class="value">AI Security Operations &amp; CTF</tspan>
<tspan x="385" y="120" class="cc">. </tspan><tspan class="key">Kernel</tspan>:<tspan class="cc"> ........ </tspan><tspan class="value">AI Red Teaming &amp; Pentesting</tspan>
<tspan x="385" y="140" class="cc">. </tspan><tspan class="key">IDE</tspan>:<tspan class="cc"> ................................... </tspan><tspan class="value">Neovim, VSCode</tspan>
<tspan x="385" y="160" class="cc">. </tspan>
<tspan x="385" y="180" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Programming</tspan>:<tspan class="cc"> ...... </tspan><tspan class="value">Python, Go, Bash, C/C++, Java</tspan>
<tspan x="385" y="200" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Computer</tspan>:<tspan class="cc"> ........... </tspan><tspan class="value">HTML, CSS, JavaScript, JSON</tspan>
<tspan x="385" y="220" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Real</tspan>:<tspan class="cc"> ................................... </tspan><tspan class="value">English</tspan>
<tspan x="385" y="240" class="cc">. </tspan>
<tspan x="385" y="260" class="cc">. </tspan><tspan class="key">Hobbies</tspan>:<tspan class="cc"> ........................... </tspan><tspan class="value">Breaking &amp; Fixing Things</tspan>
<tspan x="385" y="280" class="cc">. </tspan><tspan class="key">Research</tspan>:<tspan class="cc"> ......................... </tspan><tspan class="value">LLM Safety &amp; Jailbreaking</tspan>
<tspan x="385" y="300" class="cc">. </tspan>
<tspan x="385" y="325" class="title">- Contact</tspan> <tspan class="cc">-————————————————————————————————————————————-—-</tspan>
<tspan x="385" y="350" class="cc">. </tspan><tspan class="key">Email</tspan>.<tspan class="key">Personal</tspan>:<tspan class="cc"> ...................... </tspan><tspan class="value">goofyaapa@gmail.com</tspan>
<tspan x="385" y="370" class="cc">. </tspan><tspan class="key">GitHub</tspan>:<tspan class="cc"> .................................. </tspan><tspan class="value">securitygeek15</tspan>
<tspan x="385" y="390" class="cc">. </tspan><tspan class="key">Focus</tspan>:<tspan class="cc"> .................................... </tspan><tspan class="value">AI Security</tspan>
<tspan x="385" y="410" class="cc">. </tspan><tspan class="key">Role</tspan>:<tspan class="cc"> ............................. </tspan><tspan class="value">Security Researcher</tspan>
<tspan x="385" y="430" class="cc">. </tspan><tspan class="key">Target</tspan>:<tspan class="cc"> .......................... </tspan><tspan class="value">Adversarial AI &amp; Defenses</tspan>
<tspan x="385" y="450" class="cc">. </tspan>
<tspan x="385" y="475" class="title">- GitHub Stats</tspan> <tspan class="cc">-———————————————————————————————————————-—-</tspan>
<tspan x="385" y="500" class="cc">. </tspan><tspan class="key">Repos</tspan>:<tspan class="cc" id="repo_data_dots">{repo_dots}</tspan><tspan class="value" id="repo_data">{stats['repo_data']}</tspan> {{<tspan class="key">Contributed</tspan>: <tspan class="value" id="contrib_data">{stats['contrib_data']}</tspan>}} | <tspan class="key">Stars</tspan>:<tspan class="cc" id="star_data_dots">{star_dots}</tspan><tspan class="value" id="star_data">{stats['star_data']}</tspan>
<tspan x="385" y="520" class="cc">. </tspan><tspan class="key">Commits</tspan>:<tspan class="cc" id="commit_data_dots">{commit_dots}</tspan><tspan class="value" id="commit_data">{stats['commit_data']}</tspan> | <tspan class="key">Followers</tspan>:<tspan class="cc" id="follower_data_dots">{follower_dots}</tspan><tspan class="value" id="follower_data">{stats['follower_data']}</tspan>
<tspan x="385" y="540" class="cc">. </tspan><tspan class="key">Lines of Code on GitHub</tspan>:<tspan class="cc" id="loc_data_dots">{loc_dots}</tspan><tspan class="value" id="loc_data">{stats['loc_data']}</tspan> ( <tspan class="addColor" id="loc_add">{stats['loc_add']}</tspan><tspan class="addColor">++</tspan>, <tspan class="delColor" id="loc_del">{stats['loc_del']}</tspan><tspan class="delColor">--</tspan> )
</text>
</svg>
"""
    return svg_content

if __name__ == '__main__':
    with open('dark_mode.svg', 'w', encoding='utf-8') as f:
        f.write(build_svg(True))
    with open('light_mode.svg', 'w', encoding='utf-8') as f:
        f.write(build_svg(False))
    print("build_hud.py generated dark_mode.svg and light_mode.svg successfully!")
