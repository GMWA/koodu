from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from blog.routers.users import router as users_router
from blog.routers.posts import router as posts_router

app = FastAPI()
app.include_router(users_router)
app.include_router(posts_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # origins we allow
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)