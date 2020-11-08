from django.db import models
from myecho.db.models import BaseModel
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password, check_password


class User(BaseModel):
    """
        用户表
    """
    class Meta:
        db_table = 'sso_user'

    class PermissionType(models.IntegerChoices):
        ADMIN = 0, '管理员'
        NORMAL = 1, '普通用户'

    username_validator = [UnicodeUsernameValidator()]

    id = models.AutoField('id', primary_key=True, editable=False, help_text='主键')
    username = models.CharField(_('username'), max_length=150, unique=True, validators=username_validator)
    email = models.EmailField(_('email address'), blank=True)
    password = models.CharField(_('password'), max_length=128)
    permission_type = models.SmallIntegerField(_('permission_type'), choices=PermissionType.choices, default=1)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)

    def __str__(self) -> str:
        return self.username

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    def check_password(self, raw_password) -> bool:
        return check_password(raw_password, self.password)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
