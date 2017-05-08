from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class User(User):
    """
    Almost empty Users class
    """
    is_valid = models.BooleanField(default=False, blank=True)
