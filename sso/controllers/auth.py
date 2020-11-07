from django.utils import timezone

from sso.models import User

def authenticate(username, password):
    user = User.objects.filter(username=username).first()
    if not user:
        return False
    if user.check_password(password):
        user.last_login = timezone.now()
        user.save()
        return user
    return False