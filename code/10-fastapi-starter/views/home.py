
import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

router = fastapi.APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})
