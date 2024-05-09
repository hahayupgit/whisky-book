import json;
import os;

FILENAME = './src/games.json'
GS_PATH = './src/game-support'

FIRSTLINE_STARTING = '<!-- Aliases: ['
FIRSTLINE_ENDING = '] -->'
ALIAS_SPLIT = ', '

FIRSTLINE_STARTING_LEN = len(FIRSTLINE_STARTING)
FIRSTLINE_ENDING_LEN = len(FIRSTLINE_ENDING)

if __name__ == '__main__':
    
    # open FILENAME
    f = open(FILENAME)
    current_json = json.load(f)
    
    # create a sorted list of the files in the path GS_PATH
    game_support_dir = os.listdir(GS_PATH)
    game_support_dir = sorted(game_support_dir)
    
    # iterate through each game file in the directory that isnt the readme
    for i in game_support_dir:
        if i != "README.md" and i != "template.md":
            
            # open that file and read the first line
            f_curr = open(f"{GS_PATH}/{i}")
            f_curr_firstline = f_curr.readline()
            
            # get a string of the aliases of the game,
            # starting from FIRSTLINE_STARTING_LEN and ending before
            # FIRSTLINE_ENDING_LEN + 1
            i_aliases = f_curr_firstline[FIRSTLINE_STARTING_LEN:len(f_curr_firstline) - (FIRSTLINE_ENDING_LEN + 1)]
            
            # split this string by ALIAS_SPLIT
            i_aliases = i_aliases.split(ALIAS_SPLIT)
            print(i_aliases)
            print(i)
            # set the current value of the game to its aliases
            current_json[i] = {"aliases": i_aliases}
    
    # writes these results
    outfile = open(FILENAME, "w")
    json.dump(current_json, outfile)