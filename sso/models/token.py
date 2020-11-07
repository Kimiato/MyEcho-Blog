import os
import binascii
from datetime import timedelta
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from sso.models import User


class Token(models.Model):
    """
        Token
    """
    class Meta:
        db_table = 'sso_token'

    id = models.AutoField('id', primary_key=True, editable=False, help_text='主键')
    key = models.CharField(_("Key"), max_length=50)
    user = models.ForeignKey(User, related_name='api_token', on_delete=models.CASCADE, verbose_name=_("User"))
    create_time = models.DateTimeField(_("create_time"), auto_now_add=True)
    expires_time = models.DateTimeField(_("expires_time"), blank=True, null=True)

    def __str__(self) -> str:
        return self.key

    def save(self, days=10, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        if not self.expires_time or self.is_expired:
            self.set_expires_time(days)
        return super().save(*args, **kwargs)

    def generate_key(self) -> str:
        key = binascii.hexlify(os.urandom(25)).decode()
        return key

    @property
    def is_expired(self):
        return timezone.now() > self.expires_time

    def set_expires_time(self, days=10):
        new_expires_time = timezone.now() + timedelta(days=days)
        if not self.expires_time or new_expires_time > self.expires_time:
            self.expires_time = new_expires_time
