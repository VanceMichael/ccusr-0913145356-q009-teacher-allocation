from fastapi import FastAPI

app = FastAPI(title="教师结对支援匹配引擎")

@app.get("/healthz")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "q009-teacher-allocation"}
