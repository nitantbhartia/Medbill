"""Customer documents (denial letters, bills, EOBs) kept on the private volume, never under static/."""

import os
import secrets

import config

ALLOWED_TYPES = {
    "application/pdf": ".pdf",
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/heic": ".heic",
    "image/webp": ".webp",
}


def validate_upload(content_type: str | None, data: bytes) -> str | None:
    """Return an error message for an unacceptable upload, or None if it is fine."""
    if not data:
        return "The file is empty."
    if content_type not in ALLOWED_TYPES:
        return "Upload a PDF or a photo (JPG, PNG, HEIC or WEBP)."
    if len(data) > config.MAX_UPLOAD_SIZE_MB * 1024 * 1024:
        return f"Files must be under {config.MAX_UPLOAD_SIZE_MB} MB."
    return None


def save_private_upload(folder: str, content_type: str, data: bytes) -> str:
    """Write the file under PRIVATE_UPLOAD_DIR/<folder>/ with a random name and return its path."""
    directory = os.path.join(config.PRIVATE_UPLOAD_DIR, folder)
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, secrets.token_hex(16) + ALLOWED_TYPES[content_type])
    with open(path, "wb") as f:
        f.write(data)
    return path
