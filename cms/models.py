from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.utils.translation import gettext_lazy as _



# Create your models here.
class Author(AbstractUser):
    email = models.EmailField(null=False)
    password = models.CharField(max_length=100 ,null=False)
    fullname =models.CharField(max_length=100,null=False)
    phone = PhoneNumberField(validators=[MinLengthValidator(10)])
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
    country = models.CharField(max_length=50,null=True)
    pincode = models.IntegerField(null=False)
    
    # change the related_name arguments for groups and user_permissions
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="author_set", # use a different name than user_set
        related_query_name="author",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="author_set", # use a different name than user_set
        related_query_name="author",
    )


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)  # Add other fields as needed

    def __str__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(max_length=30,null=False)
    body = models.CharField(max_length=300,null=False)
    summary = models.CharField(max_length=60,null=False)
    categories = models.ManyToManyField(Category)  # Many-to-many relationship
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ForeignKey relationship
    pdf = models.FileField(upload_to='pdfs',null=False)



    def __str__(self):
        return self.title