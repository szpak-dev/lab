from users.domain.ports.user_repository import UserRepository
from users.adapters.in_memory_user_repository import InMemoryUserRepository
from users.adapters.user_credentials_checker import UserCredentialsChecker
from users.domain.ports.credentials_checker import CredentialsChecker
from users.domain.ports.api_service import ApiService
from users.adapters.cli_user_creator import CliUserCreator
from users.adapters.http_api_service import HttpApiService
from users.domain.ports.user_creator import UserCreator
from users.domain.ports.user_transceiver import UserTransceiver
from users.adapters.mediator_user_transceiver import MediatorUserTransceiver
from mediator.event_bus import event_bus

user_repository: UserRepository = InMemoryUserRepository()
credentials_checker: CredentialsChecker = UserCredentialsChecker(user_repository)
api_service: ApiService = HttpApiService(user_repository)
user_creator: UserCreator = CliUserCreator(user_repository)

user_transceiver: UserTransceiver = MediatorUserTransceiver(event_bus, credentials_checker)
event_bus.user_transceiver = user_transceiver
