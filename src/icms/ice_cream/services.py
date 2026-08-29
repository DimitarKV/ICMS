from .models import Person

class IceCreamService:
    def ensure_user_exists(self, token: str, role: str):
        person, created = Person.objects.get_or_create(token=token, role=role)

    def get_user_by_token(self, token: str):
        return Person.objects.get(token=token)
