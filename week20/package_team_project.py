from ca.moncton.zijun.project import MyProject as Zijun
from ca.moncton.jiaze.project import MyProject as Jiaze
from ca.moncton.andy.project import MyProject as Andy
from ca.moncton.jerry.project import MyProject as Jerry
from ca.moncton.ranran.project import MyProject as Ranran

team = [Ranran(), Jerry(), Andy(), Jiaze(), Zijun()]

if all(boy.doproject() for boy in team):
    print('Team project finished!')
