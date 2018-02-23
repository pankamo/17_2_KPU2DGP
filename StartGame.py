import platform
import os
import game_framework

if platform.architecture()[0] == "32bit" :
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else :
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

import LogoStateFirst
import LogoStateSecond
import MainTitleState
import LaunchState
import FlyingState
import GoalState



game_framework.run(LogoStateFirst)
#game_framework.run(LogoStateSecond)
#game_framework.run(MainTitleState)
#game_framework.run(LaunchState)
#game_framework.run(FlyingState)
#game_framework.run(GoalState)

