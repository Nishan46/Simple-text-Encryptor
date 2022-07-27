from ast import arg
import colorsys
from pydoc import text
from turtle import color
from rich.prompt import Prompt
from rich.console import Console
from rich.text import Text
from rich import print
from rich.panel import Panel
console = Console()



class St:
    def Consols(text,style="",colours="White",si=0,li=0):
        text = Text(text)
        if li == 0:
            text.stylize(f"{style} {colours}", si, len(text))
        else:
            text.stylize(f"{style} {colours}", si, li)
        console.print(text)

    def Texting(text,style,colours,si=0,li=0):
        text = Text(text)
        if li == 0:
            text.stylize(f"{style} {colours}", si, len(text))
        else:
            text.stylize(f"{style} {colours}", si, li)
        return text

    def InputWith_Choice(text,choicess=[],defa=""):
        name = Prompt.ask(text, choices=choicess, default=defa)
        return name 

    def Input(text):
        name = Prompt.ask(text)
        return name 

    def Pointpans():
        point = f'[+]'
        print(Panel.fit(f"[blue]{point} [cyan]Press 1 to Encrypt \n[blue]{point} [cyan]Press 2 to Test"))
    
    def pans(tcolor='',tt='',color='',text=''):
        print(Panel.fit(f"[{tcolor}] {tt}\n [{color}]{text}"))


    def pansError(tcolor='',tt=''):
        print(Panel.fit(f"[{tcolor}] {tt}"))
