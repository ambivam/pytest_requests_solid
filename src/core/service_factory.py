from src.api.user_service import UserService

class ServiceFactory:
    """Factory pattern for creating API service instances"""

    @staticmethod
    def get_service(service_name):
        services = {
            "user": UserService
        }
        return services.get(service_name, None)()
