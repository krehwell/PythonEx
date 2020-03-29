#this is a custom import ex from folder modulez

import sys
sys.path.append(".\\moduleZ")
from draw import draw_game

def play_game():
    print("the play game function is called")

def main():
    result = play_game()
    draw_game(result)

if __name__ == "__main__":
    main()
