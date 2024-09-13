from fastapi import FastAPI

from routers import auth, jobs, profile

app = FastAPI()

app.include_router(auth.router)
app.include_router(jobs.router)
app.include_router(profile.router)
