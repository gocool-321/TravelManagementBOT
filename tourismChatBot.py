from bardapi import Bard
from colorama import Fore

import requests
import os
import time
import random

os.environ['_BARD_API_KEY'] = "<BARDAPI-KEY-HERE>"

def getDataFromBot():
    print("Hey wanna know about the tourism? Please ask me? ",end="",sep="")
    input_text = str(input())

    if input_text.lower() in ["exit","terminate","close"]:
        return [], True

    text = Bard().get_answer(input_text)['content']

    while "**" in text:
        text = text.replace("**","")

    lines = list(filter(lambda x: not x.startswith("[Image"),text.split("\n")))
    return lines,False

while True:
    result,terminate = getDataFromBot()
    if terminate:
        break
    for i in result:
        print(i,end="\n\n")