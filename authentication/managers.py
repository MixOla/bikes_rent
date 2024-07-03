from django.contrib.auth.base_user import BaseUserManager

class UserRoles:
    USER = 'user'
    ADMIN = 'admin'
    choices = ((USER, 'Пользователь'), (ADMIN, 'Администратор'))

class UserManager(BaseUserManager):
    """
    Функция создания пользователя — в нее мы передаем обязательные поля
    """

    def create_user(self, email, username, password=None, role=UserRoles.USER):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            role=role
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, password, email, username, role=UserRoles.ADMIN):
        user = self.model(
            email=self.normalize_email(email),
            password=password,
            username=username,
            role=role
        )
        user.set_password(user.password)
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user