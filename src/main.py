from fastapi import FastAPI, Depends, Query
from fastapi.responses import PlainTextResponse,JSONResponse
from src.routers.movie_router import movie_router
from src.utils.http_error_handler import HTTPErrorHandler
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
import os
def dependency1():
    print("GlobalDependency 1")
def dependency2():
    print("GlobalDependency 2")
    
app=FastAPI(dependencies=[Depends(dependency1),Depends(dependency2)])

app.add_middleware(HTTPErrorHandler)
static_path=os.path.join(os.path.dirname(__file__),"static/")
templates_path= os.path.join(os.path.dirname(__file__),"templates/")

app.mount("/static",StaticFiles(directory=static_path),"static")
templates = Jinja2Templates(directory=templates_path)


@app.get("/",tags=["Home"])
def home(request: Request):
    # return PlainTextResponse(content="Home",status_code=200)
    return templates.TemplateResponse("index.html",{"request":request,"message":"Welcome!"})

app.include_router(prefix="/Movies",router=movie_router)
@app.middleware("http")
async def http_error_handler(request: Request, callnext)-> JSONResponse:
    print("Middleware runing")
    return await callnext(request)
# CommonDep=Annotated[str, Query(max_length=10)]
class CommonDep:
    def __init__(self,start_date:str,end_date:str) ->None:
        self.start_date=start_date
        self.end_date=end_date


def common_params(start_date:str, end_date:str):
	return f" 'start_date': {start_date}, 'end_date': {end_date}"
# @app.get("/users")
# def get_users(commons:CommonDep):
#     return f"Users created between {commons['start_date']} and  {commons['end_date']}"

@app.get("/users")
def get_users(commons:CommonDep= Depends(CommonDep)):
    return f"Users created between {commons.start_date} and  {commons.end_date}"
@app.get("/customers")
def get_costumers(commons:CommonDep= Depends(CommonDep)):
    return f"Users created between {commons.start_date} and  {commons.end_date}"


app.include_router(router=movie_router)