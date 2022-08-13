import os, time, json, random, base64, threading, re, sys
try: import requests, colorama, cursor; from capmonster_python import HCaptchaTask
except: os.system('pip install -q capmonster-python websocket requests colorama cursor')
import requests, colorama, cursor; from capmonster_python import HCaptchaTask
from colorama import *
from pystyle import *
import hashlib
from os import system


lilith = """
                                      


                     ██╗     ██╗██╗     ██╗████████╗██╗  ██╗
                     ██║     ██║██║     ██║╚══██╔══╝██║  ██║
                     ██║     ██║██║     ██║   ██║   ███████║
                     ██║     ██║██║     ██║   ██║   ██╔══██║
                     ███████╗██║███████╗██║   ██║   ██║  ██║
                     ╚══════╝╚═╝╚══════╝╚═╝   ╚═╝   ╚═╝  ╚═╝

              ⌜――――――――――――――――――――――――――――――――――――――――――――――――――――⌝
              ┇      [Discord] https://discord.gg/rjAzwtA5Y9       ┇
              ┇      [Github]  https://github.com/isisv1           ┇
              ⌞――――――――――――――――――――――――――――――――――――――――――――――――――――⌟
"""
System.Size(200,40)
Anime.Fade(Center.Center(lilith), Colors.rainbow, Colorate.Vertical, interval=0.020, enter=True)


def fire(text):
    system(""); faded = ""
    green = 250
    for line in text.splitlines():
        faded += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
        if not green == 0:
            green -= 25
            if green < 0:
                green = 0
    return faded


print(fire("""
                     ██╗     ██╗██╗     ██╗████████╗██╗  ██╗
                     ██║     ██║██║     ██║╚══██╔══╝██║  ██║
                     ██║     ██║██║     ██║   ██║   ███████║
                     ██║     ██║██║     ██║   ██║   ██╔══██║
                     ███████╗██║███████╗██║   ██║   ██║  ██║
                     ╚══════╝╚═╝╚══════╝╚═╝   ╚═╝   ╚═╝  ╚═╝

              ⌜――――――――――――――――――――――――――――――――――――――――――――――――――――⌝
              ┇      [Discord] https://discord.gg/rjAzwtA5Y9       ┇
              ┇      [Github]  https://github.com/isisv1           ┇
              ⌞――――――――――――――――――――――――――――――――――――――――――――――――――――⌟
                                  ⌜CLICK ENTER⌝
             [1] Coming Soon    [3] Sniper           [5] D.I.D
             [2] Discord        [4] Mass DM          [6] Token Checker
             [7] Ronin Pinger   [8] Ronin Lookup     Creds To Axi
                                                  """)) 

choice = input("Option > ")

if choice == "2":
    os.startfile("login.exe")
if choice == "3":
    os.startfile("sniper.exe")
if choice == "4":
    os.startfile("massdm.exe")
if choice == "5":
    os.startfile("did.exe")
if choice == "6":
    os.startfile('token_checker.exe')
if choice == "7":
    os.startfile("RoninPinger.exe")
if choice == "8":
    os.startfile("RoninIP.exe")
