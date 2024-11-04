from fastapi import Path, Query, APIRouter
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from src.models.movie_model import Movie, MovieCreate,MovieUpdate

movies: list[Movie]=[]
movie_router=APIRouter()


@movie_router.get("/",tags=["Movies"],status_code=500, response_description="No hay datos guardados hasta el momento") 
def get_movies() -> list[Movie]:
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content,status_code=200)
@movie_router.get("/{id}",tags=["Home"])
def get_movie(id:int = Path(gt=0)) ->Movie | dict:
    for movie in movies:
        if movie.id==id:
            return JSONResponse(content=movie.model_dump(),status_code=400)
    return JSONResponse(content={},status_code=404)
@movie_router.get("/by_category",tags=["Movies"])
def get_movie_by_category(category:str=Query(min_length=5,max_length=20)) -> Movie:
    for movie in movies:
        if movie in movies:
            if movie["category"]==category:
                return JSONResponse(content=movie.model_dump)
    return JSONResponse(content={},status_code=404)
@movie_router.post("/",tags=["Home"])
def create_movie(movie: MovieCreate) -> list[Movie]: # indica el tipo de respuesta.
    movies.append(movie)
    return RedirectResponse("/", status_code=303)
@movie_router.put("/{id}",tags=["Movies"])
def update_movie(id:int, movie:MovieUpdate):
    for item in movies:
        if item.id == id:
            item.title = movie.title
            item.overview =movie.title
            item.year =movie.year
            item.rating=movie.rating
            item.category=movie.category
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content,status_code=200)
@movie_router.delete("/{id}",tags=["Movies"])
def delete_movie(id:int) -> list[Movie]:
    for movie in movies:
        if movie.id==id:
            print(movie)
            movies.remove(movie)
     
    return JSONResponse(content=[movie.model_dump() for movie in movies],status_code=200) 
@movie_router.get("/get_file")
def get_file():
    return FileResponse("LoremIpsum.txt")

