# game.py module
import draw

def play_game():
    ...

def returnMultiply(n):
    return n*n

def main():
    result = play_game
    draw.draw_game(result)

if __name__ == '__main__':
    main()


clear = returnMultiply(4)
draw.clear_screen(clear)