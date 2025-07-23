dir=$(dirname "$0")
cd "$dir"

uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000 --workers 1 --log-level info