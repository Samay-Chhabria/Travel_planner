def success_response(data=None, message: str = "Request completed successfully") -> dict:
    return {"success": True, "data": data, "message": message}
