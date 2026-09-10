from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.audio_transcription_summarizer.models import AgenticAudioTranscriptionSummarizerSession, AgenticAudioTranscriptionSummarizerItem
from app.domain.audio_transcription_summarizer.schemas import AgenticAudioTranscriptionSummarizerSessionCreate, AgenticAudioTranscriptionSummarizerItemCreate

class AgenticAudioTranscriptionSummarizerService:
    @staticmethod
    def create_session(db: Session, data: AgenticAudioTranscriptionSummarizerSessionCreate) -> AgenticAudioTranscriptionSummarizerSession:
        db_obj = AgenticAudioTranscriptionSummarizerSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticAudioTranscriptionSummarizerSession:
        return db.query(AgenticAudioTranscriptionSummarizerSession).filter(AgenticAudioTranscriptionSummarizerSession.id == session_id).first()
