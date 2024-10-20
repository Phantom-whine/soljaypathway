from django.contrib.auth.models import BaseUserManager

class CustomManager(BaseUserManager) :
    def create_user(self, email, password, **extra_fields) :
        if not email :
            raise ValueError('Email field cannot be empty')

        email = self.normalize_email(email)
        user = self.model(email=email, username=email.split('@')[0], **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields) :
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') == False :
            raise ValueError('is_staff for superuser must be true')
        if extra_fields.get('is_superuser') == False :
            raise ValueError('is_staff for superuser must be true')

        self.create_user(email, password, **extra_fields)