# Import all the models, so that Base has them before being
# imported by Alembic
from app.core.db.base_class import Base
from app.models.user import User
from app.models.chat import Chat
from app.models.member import Member
from app.models.message import Message
