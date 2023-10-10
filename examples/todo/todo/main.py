from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from todo.routers.users import router as users_router
from todo.routers.categories import router as categories_router
from todo.routers.todos import router as todos_router

app = FastAPI()
app.include_router(users_router)
app.include_router(categories_router)
app.include_router(todos_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # origins we allow
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)