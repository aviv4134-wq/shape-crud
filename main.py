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

def check_user_menu_input(user_input_menu:str) -> bool:
    logger.debug(f'the user input is {user_input_menu}')
    try:
        logger.info('start checking user menu input')
        if not user_input_menu.isdigit() :
           raise ValueError('user enter a letter')
        elif not 1 <= int(user_input_menu) <= 5:
           raise ValueError('user enter number not allowed')
        logger.info('input main allowed check completed')
        return True
    except ValueError as error:
        logger.error(f'user did not enter a number between 1 - 5 {error}')
        return False

 
def main():
    run = True
    while run:
        print_menu()
        user_input_menu = input('enter a number 1 - 5: ')
        if not check_user_menu_input(user_input_menu):
            print('error only number between 1 - 5 allowed')
            continue
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

#main()