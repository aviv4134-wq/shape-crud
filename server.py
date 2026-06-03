from fastapi import FastAPI,Body,HTTPException
import shape_manager,circle,rectangle,square
from pydantic import BaseModel

app = FastAPI()
shape_manager = shape_manager.ShapeManager()


@app.get('/shapes')
def show_all_shapes():
    '''show all list of dicts shape each dict is a shape'''
    shapes = []
    for shape in shape_manager.get_all_shapes():
        shape = shape.to_dict()
        shapes.append(shape)
    return shapes
@app.get('/shapes/total-area')
def show_total_area():
    '''show all shapes area combaine'''
    count_area = 0 
    for shape in shape_manager.get_all_shapes():
        count_area += shape.get_area()
    return count_area

@app.post('/shapes')
def create_shape(shape:dict = Body(...)):
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
        raise HTTPException(status_code=409,detail=f'{error}'  )
    except TypeError as error:
        raise HTTPException(status_code=400,detail=f'{error}')
@app.get('/shapes/{shape_id}')
def show_shape_by_id(shape_id:int):
    try:
        for shape in shape_manager.get_all_shapes():
           if shape_id == shape['id']:
              return shape
        raise ValueError('id not found in the system')
    except ValueError:
        return 'id not found in the system'

@app.delete('/shapes/{shape_id}')
def delete_shape(shape_id):
    shape_manager.delete_shape(shape_id)
    return 'success' 
#print(delete_shape(1))

@app.put('/shapes/{shape_id}')
def update_shape(shape_id:int,new_data:dict = Body(...)):
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
        
    return f'success to update {show_all_shapes()}'

if __name__ == '__main__':
  #d=  {'id':3,'type':'circle','radius':10 }
  #print(update_shape(3,d))
  print(show_all_shapes())