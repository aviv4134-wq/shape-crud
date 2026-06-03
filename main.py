import circle,rectangle,square,shape_manager
from logger_file import logger
from fastapi import FastAPI

app = FastAPI()

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
    """check input user menu SHAPE CRUD"""
    
    logger.debug(f'the user input is {user_input_menu}')
    try:
        logger.info('start checking user menu input')
        if not user_input_menu.isdigit() :
           raise ValueError('user enter a letter')
        elif not 1 <= int(user_input_menu) <= 5:
           raise ValueError('user enter number not allowed')
        logger.info('success user choose in menu SHAPE CRUS ')
        return True
    except ValueError as error:
        logger.error(f'user did not enter a number between 1 - 5 {error}')
        return False
def mange_user_input():
    """user input and validate the user input return None """
    run = True
    while run:
        logger.info('start user input loop and checking it in shape menu ')
        user_input = user_input_shape_menu()
        try:
            input_validation(user_input)
            logger.info('success user enter number between 1 - 3')
            return user_input
        except ValueError :
            logger.error('user input is letters not numbers')
            print('error letters not allowed')
        except TypeError:
            logger.error('user enter that not 1 - 3')
            print('error only numbers 1 - 3 allowed')
        
              

def user_input_shape_menu():
    """user input for shape menu
    return None"""
    user_input = input('enter type shape 1 - 3: ')
    return user_input
def input_validation(user_input):
    """check user input in shape menu only 1 2 3 allowed else error
    return None"""
    user_input = int(user_input)
    if not 1 <= user_input <=3:
        raise TypeError
    return None



def print_shape_menu():
    print("\n====================")
    print("    CHOOSE SHAPE    ")
    print("====================")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("--------------------")

 




def main():
    manager_shape = shape_manager.ShapeManager()    
    run = True
    while run:
        try:
            logger.info('start program')
            print_menu()
            user_input_menu = input('enter a number 1 - 5: ')
            if not check_user_menu_input(user_input_menu):
                print('error only number between 1 - 5 allowed')
                continue
            if user_input_menu == '1':
                print_shape_menu() 
                type_shape = mange_user_input()   #check user input if the input is in the menu(1,2,3) 
                if type_shape == '1':
                        type_shape = 'square'
                        id_shape = input('enter id to your shape:  ')
                        side_shape = input('enter side shape: ')
                        user_square:object = square.Square(id_shape,type_shape,side_shape)  #chck inputs side
                        manager_shape.create_shape(user_square)           
                elif type_shape == '2':
                        type_shape = 'rectangle'
                        id_shape = input('enter id to your shape:  ')
                        side_length = input('enter side shape: ')
                        side_width = input('enter side shape: ')
                        user_rectangle:object = rectangle.Rectangle(id_shape,type_shape,side_length,side_width)
                        manager_shape.create_shape(user_rectangle)          
                elif type_shape == '3':
                        type_shape = 'circle'
                        id_shape = input('enter id to your shape:  ')
                        radius_circle = input('enter a radius: ')
                        user_circle:object = circle.Circle(id_shape,type_shape,radius_circle)
                        manager_shape.create_shape(user_circle)
            elif user_input_menu == '2':      
                for shape in manager_shape.get_all_shapes():
                    print(shape)
            elif user_input_menu == '3':
                shape_id_user = input('enter id: ')
                new_update_shape = input('enter number update:  ') 
                manager_shape.update_shape(shape_id_user,new_update_shape)
            elif user_input_menu == '4':
                shape_id_user = int(input('enter id to delete shape: '))
                manager_shape.delete_shape(shape_id_user)
            elif user_input_menu == '5':
                print('good bay')
                run = False
                logger.info('the user exit from program')
            logger.info('user operation success  ')    
        except Exception as error :
            print(f'{error}')
            logger.error(f'{error}')
                 

   
main()

