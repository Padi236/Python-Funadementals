#Importing only the specific required module allows to write the module name while accesing it 
#And not the package full path like in main.py in current dir
#Same result with lesser code

from Game.Characters import player

#Importing specific definitions allows further code reduction
from Game.Characters.Boss import get_Boss_info

player.get_player_info()
get_Boss_info()