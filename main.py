
from fastapi import FastAPI 
import importlib 
import os 


def get_routers(folder_name): 
    path = os.path.join(os.getcwd(), '', folder_name) 
    for folder in os.listdir(path): 
        if not folder.startswith('__'): 
            if os.path.isdir(os.path.join(path, folder)): # 若是文件夹 
                for file in os.listdir(os.path.join(path, folder)): 
                    if not file.startswith('__'): 
                        lib = importlib.import_module(f'{folder_name}.{folder}.{file.split(".")[0]}') 
                        sub_router = getattr(lib, 'router') 
                        app.include_router(sub_router) 
            else: # 若是文件 
                lib = importlib.import_module(f'{folder_name}.{folder.split(".")[0]}') 
                sub_router = getattr(lib, 'router') 
                app.include_router(sub_router) 


app = FastAPI() 

get_routers('routers')


@app.get("/")
async def root():
    return {"message": "Hello World"}