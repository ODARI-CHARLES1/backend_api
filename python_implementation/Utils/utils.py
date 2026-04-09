import hashlib
import secrets
from datetime import datetime, timedelta

def hash_string(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

def generate_token(length: int = 32) -> str:
    return secrets.token_urlsafe(length)

def format_datetime(dt: datetime) -> str:
    return dt.isoformat()

def parse_datetime(date_str: str) -> datetime:
    return datetime.fromisoformat(date_str)

def add_days(dt: datetime, days: int) -> datetime:
    return dt + timedelta(days=days)

class ResponseHelper:
    @staticmethod
    def success(data: any = None, message: str = "Success"):
        return {"success": True, "message": message, "data": data}
    
    @staticmethod
    def error(message: str, code: int = 400):
        return {"success": False, "message": message, "code": code}
    
    @staticmethod
    def paginated(items: list, total: int, page: int, limit: int):
        return {
            "items": items,
            "total": total,
            "page": page,
            "limit": limit,
            "pages": (total + limit - 1) // limit
        }