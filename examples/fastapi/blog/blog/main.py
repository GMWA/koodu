from dotenv import load_dotenv

load_dotenv()
from blog.routers.posts import router as posts_router
from blog.routers.users import router as users_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
