import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - [%(filename)s] - %(message)s")
file_handler = logging.FileHandler('logs.txt',encoding='utf-8')
file_streamer = logging.StreamHandler()

file_handler.setFormatter(formatter)
file_streamer.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(file_streamer)

def print_menu() ->None:
    """print menu to user"""
    print('===WELCOME to SHAPE CRUD===')
    print("""add shape 1
Show all shapes .2
Update shape .3
Delete shape .4
Exit .5
 """)



def main():
    run = True
    while run:
        print_menu()
        user_input_menu = input('enter a number 1 - 5: ')
        if user_input_menu == '1':
            pass
        elif user_input_menu == '2':
            pass
        elif user_input_menu == '3':
            pass
        elif user_input_menu == '4':
            pass
        elif user_input_menu == '5':
            print('good bay')
            break 

main()