from fastapi import FastAPI,Body,HTTPException
import shape_manager,circle,rectangle,square
from logger_file import logger



app = FastAPI()
shape_manager = shape_manager.ShapeManager()


@app.get('/shapes')
def show_all_shapes():
    '''show all list of dicts shape each dict is a shape'''
    logger.info('server take the request')
    shapes = []
    for shape in shape_manager.get_all_shapes():
        shape = shape.to_dict()
        shapes.append(shape)
    logger.info('success to show all shape ')
    return shapes

@app.get('/shapes/total-area')
def show_total_area():
    '''show all shapes area combaine'''
    logger.info('server take the massage')
    count_area = 0 
    for shape in shape_manager.get_all_shapes():
        count_area += shape.get_area()
    logger.info('success to show the total area')
    return count_area

@app.post('/shapes')
def create_shape(shape:dict = Body(...)):
    '''take dict of shape and create object shape and save on json file return message success 
     if the creation fail it will be exception '''
    logger.info('server take the request')
    shape_dict = shape
    try:
        if shape_dict['type'] not in ['circle','rectangle','square']:
           raise HTTPException(status_code=400,detail='user enter wrong shape type')
        if shape_dict['type'] == 'circle':
             shape = circle.Circle(shape_dict['id'],shape_dict['type'],shape_dict['radius'])
        elif shape_dict['type'] == 'square' :
             shape = square.Square(shape_dict['id'],shape_dict['type'],shape_dict['side'])
        elif shape_dict['type'] == 'rectangle' :
             shape =  rectangle.Rectangle(shape_dict['id'],shape_dict['type'],shape_dict['side length'],shape_dict['side width'])    
        shape_manager.create_shape(shape)
        return 'success to create'
    except ValueError as error:
        logger.error(error)
        raise HTTPException(status_code=409,detail=f'{error}')
    except TypeError as error:
        logger.error(error)
        raise HTTPException(status_code=400,detail=f'{error}')
     
@app.get('/shapes/{shape_id}')    
def show_shape_by_id(shape_id:int):
    '''take shape id and show the dict of the shape return dict 
     if id not exists raise exception error '''
    logger.info('server take the request')
    for shape in shape_manager.shapes:
        if shape_id == shape.shape_id:
            return shape.to_dict()
    logger.error('id not exists')
    raise HTTPException(status_code=404,detail='id not found in the system')
    

@app.delete('/shapes/{shape_id}')
def delete_shape(shape_id):
    '''take int shape id and delete the shape from the list of shapes return success massage
    if id not exists raise exception'''
    logger.info('server take the request')
    if not shape_manager.is_id_exists(shape_id):
        logger.error('the id not exists in the system')
        raise HTTPException(status_code=404,detail='error the id not exists')
    shape_manager.delete_shape(shape_id)
    logger.info('success to delete shape')
    return 'success to delete shape' 


@app.put('/shapes/{shape_id}')
def update_shape(shape_id:int,new_data:dict = Body(...)):
    '''take shape id and new shape dict and update the shape object return success massage
    and check if shape id exists and validation if fails it will be raise exception
      '''
    logger.info('server take the request')
    if 0 > shape_id  or 50 < shape_id:
        logger.error('id not allowed only 1 - 50 allowed ')
        raise HTTPException(status_code=400,detail='error only id from 1 - 50 allowed')
    if not shape_manager.is_id_exists(shape_id):
        logger.error('the id not exists in the system')
        raise HTTPException(status_code=404,detail='error the id not exists')
    try:
        logger.info('start updating')
        list_of_shapes = shape_manager.shapes
        for shape in list_of_shapes:
            if shape.shape_id == shape_id:
                if isinstance(shape,rectangle.Rectangle):
                    shape.side_length = new_data.get('side length')
                    shape.side_width = new_data.get('side width')
                elif isinstance(shape,circle.Circle):
                    shape.radius = new_data.get('radius')
                elif isinstance(shape,square.Square):
                    shape.side = new_data.get('side')
                shape.shape_id = new_data.get('id')
                shape.shape_type = new_data.get('type') 
                shape_manager.save_to_json()
    except TypeError as error:
        logger.error(error)
        raise HTTPException(status_code = 400,detail = error)    
    logger.info('success to update shape')
    return f'success to update {show_all_shapes()}'

if __name__ == '__main__':
  #d=  {'id':3,'type':'circle','radius':10 }
  #print(update_shape(3,d)

  #print(show_all_shapes())
  pass