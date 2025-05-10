from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Response, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi.templating import Jinja2Templates

from app import schemas
from app import crud
from app.schemas import TranslationRequest

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/index", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all origins
    allow_credentials=True,
    allow_methods=["*"], # Allow all methods
    allow_headers=["*"], # Allow all headers
)

@app.post("/translate", response_model=schemas.TranslationResponse)
def translate(request: schemas.TranslationRequest):
    # create new translation
    task = crud.create_translation_task(x,y,p)
    background_tasks.add_task(perform_translation, taskid, request.text, request.languages, db)
    return {"task_id": task.id}


