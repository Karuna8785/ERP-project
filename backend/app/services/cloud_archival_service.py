'''Cold Storage Cloud Document Archival Service.'''
class CloudArchivalService:
    @staticmethod
    def build_archive_key(org_id: str, doc_type: str, year: int, doc_id: str) -> str:
        return f"archives/{org_id}/{year}/{doc_type.lower()}/{doc_id}.pdf"
