from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend
from src.config import SECRET
cookie_transport = CookieTransport(cookie_name="news",
                                   cookie_max_age=3600,
                                   cookie_secure=False,
                                   cookie_httponly=False)

# SECRET = os.getenv("SECRET")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET,
                       lifetime_seconds=3600,
                       token_audience=["*"])


auth_backend = AuthenticationBackend(name="jwt",
                                     transport=cookie_transport,
                                     get_strategy=get_jwt_strategy
                                     )
