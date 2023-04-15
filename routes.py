from microblog import blog
from fastapi import APIRouter

routes = APIRouter

routes.include_router(blog.router)
