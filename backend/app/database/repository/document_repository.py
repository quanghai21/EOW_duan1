from sqlalchemy.orm import Session

from app.database.models.document import Document


class DocumentRepository:

    def __init__(self, db: Session):
        self.db = db

    def get(self, document_id: int):

        return (
            self.db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

    def get_all(self):

        return (
            self.db.query(Document)
            .order_by(Document.id.desc())
            .all()
        )

    def create(
        self,
        title: str,
        content: str
    ):

        document = Document(
            title=title,
            content=content
        )

        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)

        return document

    def delete(self, document_id: int):

        document = self.get(document_id)

        if document is None:
            return False

        self.db.delete(document)
        self.db.commit()

        return True