import threading
from turtle import color
import Recources.key as core
from multiprocessing.pool import ThreadPool
from Recources.key import My
from Recources.styles import St as Stys

try:
    Stys.Consols("\n[STARTING]\n","Bold","Blue")
    Stys.Pointpans()
    Choice = Stys.InputWith_Choice(Stys.Texting("Choose from those ... ","Bold","Purple"),choicess=['1','2'])
    if Choice == '1':
        StartingPool = ThreadPool(processes=1)
        async_result = StartingPool.apply_async(core.Begin)
        Tobe = Stys.Input(Stys.Texting("Enter Text there ... ","Bold","Purple"))
        EncriptThread = threading.Thread(target=core.Encript,args=(Tobe,async_result.get(),Tobe[0]))
        EncriptThread.start()
    else:
        EndingPool2 = ThreadPool(processes=1)
        async_result23 = EndingPool2.apply_async(core.Begin)
        Frombee = Stys.Input(Stys.Texting("Enter Text there ... ","Bold","yellow"))
        Frombeee = Stys.Input(Stys.Texting("Enter Key there ... ","Bold","yellow"))
        core.Testing(Frombee,async_result23.get(),Frombeee)





except:
    if KeyboardInterrupt:
        Stys.Consols("[Code Exited!]",colours='Red',style='Bold')
        exit()