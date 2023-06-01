from endpoints.user import api_router as auth

list_of_routes = [
    auth,
]

__all__ = [
    "list_of_routes",
]
