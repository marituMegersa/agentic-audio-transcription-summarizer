from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.audio_transcription_summarizer.schemas import AgenticAudioTranscriptionSummarizerSessionCreate, AgenticAudioTranscriptionSummarizerSessionResponse
from app.domain.audio_transcription_summarizer.service import AgenticAudioTranscriptionSummarizerService

router = APIRouter(prefix="/api/v1/audio_transcription_summarizer", tags=["Agentic Audio Transcription Summarizer Domain"])

@router.post("/sessions", response_model=AgenticAudioTranscriptionSummarizerSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticAudioTranscriptionSummarizerSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Audio Transcription Summarizer.
    """
    return AgenticAudioTranscriptionSummarizerService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticAudioTranscriptionSummarizerSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticAudioTranscriptionSummarizerService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
