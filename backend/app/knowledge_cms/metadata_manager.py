class MetadataManager:
    @staticmethod
    def build_metadata(title: str, character_code: str, time_period: str, location: str, tags: str) -> dict:
        return {
            "title": title,
            "character_code": character_code,
            "time_period": time_period or "Unspecified",
            "location": location or "Unspecified",
            "tags": [t.strip() for t in tags.split(",") if t.strip()] if tags else []
        }