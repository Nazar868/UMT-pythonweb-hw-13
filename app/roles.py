from fastapi import HTTPException


def require_role(user, role="admin"):
    if user.get("role") != role:
        raise HTTPException(status_code=403, detail="Forbidden")
