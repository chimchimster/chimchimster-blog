from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy
from .managers import UserManager
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(gettext_lazy("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Comment(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    content = models.TextField(blank=False, verbose_name="Content")
    publishing_date = models.DateTimeField(auto_now_add=True, verbose_name="Published At")
    edited_date = models.DateTimeField(auto_now=True, verbose_name="Edited At")
    likes = models.IntegerField(default=0, verbose_name="Likes")
    dislikes = models.IntegerField(default=0, verbose_name="Dislikes")
    portfolio_id = models.ForeignKey("Portfolio", on_delete=models.PROTECT, verbose_name="Portfolio")
    user_id = models.ForeignKey("User", on_delete=models.PROTECT, verbose_name="User")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comment"
        ordering = ["-publishing_date"]


class Portfolio(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User's Email")
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name="Description")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True, verbose_name="Picture")
    is_published = models.BooleanField(default=True, verbose_name="Published?")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    edit_date = models.DateTimeField(auto_now=True, verbose_name="Edited At")
    date_of_work_beg = models.DateTimeField(verbose_name="Project Started At")
    date_of_work_end = models.DateTimeField(verbose_name="Project Ended At")
    repository_link = models.URLField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Link to Repository"
    )
    website_link = models.URLField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Link to Website"
    )
    likes = models.IntegerField(default=0, verbose_name="Likes")
    dislikes = models.IntegerField(default=0, verbose_name="Dislikes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio', kwargs={'portfolio_slug': self.slug})

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio"
        ordering = ['-creation_date']