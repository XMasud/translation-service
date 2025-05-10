from sqlalchemy.orm import Session
import models

def create_translation_task(db:Session, text: str, languages: list):
    task = models.TranslationTask(text=text, Languages=languages)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task