import uuid
from pathlib import Path

from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

from app.game_service import GameSession, get_session
from app.models import GameMode, GameState

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Soc Ops - Social Bingo")
app.add_middleware(SessionMiddleware, secret_key="soc-ops-secret-key")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR / "templates")


def _get_game_session(request: Request) -> GameSession:
    """Get or create a game session using cookie-based sessions."""
    if "session_id" not in request.session:
        request.session["session_id"] = uuid.uuid4().hex
    return get_session(request.session["session_id"])


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> Response:
    session = _get_game_session(request)
    return templates.TemplateResponse(
        request,
        "home.html",
        {"session": session, "GameState": GameState, "GameMode": GameMode},
    )


@app.post("/start", response_class=HTMLResponse)
async def start_game(request: Request) -> Response:
    session = _get_game_session(request)

    # Default to classic bingo
    game_mode_str = GameMode.CLASSIC_BINGO.value

    # Try to get game_mode from various sources
    # 1. Check query params first
    if "game_mode" in request.query_params:
        game_mode_str = request.query_params["game_mode"]
    else:
        # 2. Try form data if content-type indicates form data
        content_type = request.headers.get("content-type", "")
        if "urlencoded" in content_type:
            try:
                form_data = await request.form()
                if form_data and "game_mode" in form_data:
                    game_mode_str = form_data["game_mode"]
            except Exception as e:
                # Log but don't fail - just use default
                print(f"Form parsing error: {e}")

    # Validate and convert to GameMode enum
    try:
        game_mode = GameMode(game_mode_str)
    except ValueError:
        game_mode = GameMode.CLASSIC_BINGO

    session.start_game(game_mode)
    return templates.TemplateResponse(
        request, "components/game_screen.html", {"session": session}
    )


@app.post("/toggle/{square_id}", response_class=HTMLResponse)
async def toggle_square(request: Request, square_id: int) -> Response:
    session = _get_game_session(request)
    session.handle_square_click(square_id)
    return templates.TemplateResponse(
        request, "components/game_screen.html", {"session": session}
    )


@app.post("/reset", response_class=HTMLResponse)
async def reset_game(request: Request) -> Response:
    session = _get_game_session(request)
    session.reset_game()
    return templates.TemplateResponse(
        request,
        "components/start_screen.html",
        {"session": session, "GameState": GameState},
    )


@app.post("/dismiss-modal", response_class=HTMLResponse)
async def dismiss_modal(request: Request) -> Response:
    session = _get_game_session(request)
    session.dismiss_modal()
    return templates.TemplateResponse(
        request, "components/game_screen.html", {"session": session}
    )


def run() -> None:
    """Entry point for the application."""
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
