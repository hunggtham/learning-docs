import asyncio
import os
from fastapi import FastAPI, HTTPException
from pipeline import Pipeline

app = FastAPI(title="정보처리기사 Textbook Worker")
lock = asyncio.Lock()

@app.get("/health")
async def health():
    return {
        "ok": True,
        "draft_model": os.getenv("OPENAI_DRAFT_MODEL", "gpt-5.6-terra"),
        "qa_model": os.getenv("OPENAI_QA_MODEL", "gpt-5.6-sol"),
        "push_changes": os.getenv("PUSH_CHANGES", "false"),
    }

@app.post("/run")
async def run():
    if lock.locked():
        raise HTTPException(409, "A generation run is already active")
    async with lock:
        try:
            return await asyncio.to_thread(Pipeline().run)
        except Exception as exc:
            raise HTTPException(500, str(exc)) from exc
