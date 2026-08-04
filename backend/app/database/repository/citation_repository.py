from sqlalchemy.orm import Session

from app.database.models.citation import Citation


class CitationRepository:

    def __init__(self, db: Session):
        self.db = db

    def get(self, citation_id: int):

        return (
            self.db.query(Citation)
            .filter(Citation.id == citation_id)
            .first()
        )

    def get_by_document_id(self, document_id: int):

        return (
            self.db.query(Citation)
            .filter(Citation.document_id == document_id)
            .all()
        )

    def create(
        self,
        document_id: int,
        content: str
    ):

        citation = Citation(
            document_id=document_id,
            content=content
        )

        self.db.add(citation)
        self.db.commit()
        self.db.refresh(citation)

        return citation

    def delete(self, citation_id: int):

        citation = self.get(citation_id)

        if citation is None:
            return False

        self.db.delete(citation)
        self.db.commit()

        return True