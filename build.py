import json;
import os;

FILENAME = './src/games.json'
GS_PATH = './src/game-support'
SRC_PATH = './src'

FIRSTLINE_STARTING = '<!-- Aliases: ['
FIRSTLINE_ENDING = '] -->'
ALIAS_SPLIT = ', '

FIRSTLINE_STARTING_LEN = len(FIRSTLINE_STARTING)
FIRSTLINE_ENDING_LEN = len(FIRSTLINE_ENDING)

def build_json(dir):

    # open FILENAME
    f = open(FILENAME)
    current_json = json.load(f)
    
    # create a sorted list of the files in the path GS_PATH
    game_support_dir = dir
    
    # iterate through each game file in the directory that isnt the readme
    for i in game_support_dir:
        if i != "README.md" and i != "template.md":
            
            # open that file and read the first line
            f_curr = open(f"{GS_PATH}/{i}", "r")
            f_curr_line = f_curr.readline()
            
            # get a string of the aliases of the game,
            # starting from FIRSTLINE_STARTING_LEN and ending before
            # FIRSTLINE_ENDING_LEN + 1
            i_aliases = f_curr_line[FIRSTLINE_STARTING_LEN:len(f_curr_line) - (FIRSTLINE_ENDING_LEN + 1)]
            
            # split this string by ALIAS_SPLIT
            i_aliases = i_aliases.split(ALIAS_SPLIT)
            
            f_curr.readline()
            f_curr_line = f_curr.readline()
            
            i_name = f_curr_line[2:len(f_curr_line) - 1 ]
            
            # set the current value of the game to its aliases
            current_json[i] = {"aliases": i_aliases, "name": i_name}
    
    # writes these results
    outfile = open(FILENAME, "w")
    json.dump(current_json, outfile)
    
    f.close()
    outfile.close()

SUMMARY_FILENAME = './src/SUMMARY.md'
SUMMARY_STARTER = './build/SUMMARY_START.md'

def build_summary(game_dir):
    
    # open the summary file and read summary starter
    f = open(SUMMARY_FILENAME, "w")
    f_start = open(SUMMARY_STARTER, "r")
    
    # overwrite the summary file with the starter
    f_start_content = f_start.read()
    f.write(f_start_content)
    
    # get the json info of the games
    json_file = open(FILENAME, "r")
    json_contents = json.load(json_file)
    json_file.close()
    
    # iterate through the game directory and add it to the summary file,
    # get the name of the file from the json content and add that as well
    for i in game_dir:
        if i != "README.md" and i != "template.md":
            f.write(f"  - [{json_contents[i]["name"]}](./game-support/{i})\n")
    
    f.close()

if __name__ == '__main__':
    gs_dir = os.listdir(GS_PATH)
    gs_dir = sorted(gs_dir)
    
    build_json(gs_dir)
    build_summary(gs_dir)