from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="src/pages/templates")

@router.get("/", response_class=HTMLResponse)
def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/email-confirmation", response_class=HTMLResponse)
def get_email_conf(request: Request):
    return templates.TemplateResponse("email-confirmation.html", {"request": request})