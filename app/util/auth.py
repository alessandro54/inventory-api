from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "e8645c4bcb2b6bb9019bdc4b5c29b105a3c99369c0de5cf456c993421c451bc1"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")