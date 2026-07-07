import uuid
from datetime import datetime, timezone


def generate_id(prefix: str) -> str:
    """
    Generate a unique ID with a given prefix.
    Example: INS_8f3d2a1b
    """
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


def current_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()
