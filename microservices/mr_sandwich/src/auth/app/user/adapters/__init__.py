from app.user.domain.ports.user_repository import UserRepository
from app.user.adapters.in_memory_user_repository import InMemoryUserRepository
from app.user.adapters.user_credentials_checker import UserCredentialsChecker
from app.user.domain.ports.credentials_checker import CredentialsChecker
from app.user.domain.ports.api_service import ApiService
from app.user.adapters.cli_user_creator import CliUserCreator
from app.user.adapters.http_api_service import HttpApiService
from app.user.domain.ports.user_creator import UserCreator
from app.user.domain.ports.user_transceiver import UserTransceiver
from app.user.adapters.mediator_user_transceiver import MediatorUserTransceiver
from app.mediator.event_bus import event_bus

user_repository: UserRepository = InMemoryUserRepository()
credentials_checker: CredentialsChecker = UserCredentialsChecker(user_repository)
api_service: ApiService = HttpApiService(user_repository)
user_creator: UserCreator = CliUserCreator(user_repository)

user_transceiver: UserTransceiver = MediatorUserTransceiver(event_bus, credentials_checker)
event_bus.user_transceiver = user_transceiver
