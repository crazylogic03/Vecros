import uuid
from datetime import datetime, timezone


def generate_id(prefix):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


def current_timestamp():
    return datetime.now(timezone.utc).isoformat()