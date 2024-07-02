from django.contrib.auth.base_user import AbstractBaseUser
from authentication.managers import UserManager
from django.db import models

class User(AbstractBaseUser):
    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'
    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['username', 'email']

    username = models.CharField(max_length=100, null=False, unique=True, blank=False)
    email = models.EmailField(verbose_name="email address", unique=True, null=False, blank=False)

    # переопределим менеджер модели пользователя
    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.username}"
