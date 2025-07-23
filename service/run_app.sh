dir=$(dirname "$0")
cd "$dir"

uv run uvicorn main:app --reload