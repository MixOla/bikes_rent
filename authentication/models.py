from django.contrib.auth.base_user import AbstractBaseUser
from authentication.managers import UserManager, UserRoles
from django.db import models

class User(AbstractBaseUser):
    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'username'
    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['email']

    username = models.CharField(max_length=100, null=False, unique=True, blank=False)
    email = models.EmailField(verbose_name="email address", unique=True, null=False, blank=False)
    role = models.CharField(choices=UserRoles.choices, default=UserRoles.USER, max_length=5)

    # переопределим менеджер модели пользователя
    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN
    #
    # @property
    # def is_user(self):
    #     return self.role == UserRoles.USER
    #
    # @property
    # def is_superuser(self):
    #     return self.is_admin
    #
    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return f"{self.username}"
