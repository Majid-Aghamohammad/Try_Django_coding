from django.db import models
from django.utils import timezone
# Create your models here.

class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)
class BlogPostManager(models.Manager):
    def get_queryset(self):
        return self.filter(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()
class BlogPost(models.Model):
    title        = models.CharField(max_length=255)
    slug         = models.SlugField(unique=True)
    content      = models.TextField()
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False , null=True, blank=True)
    timestamp    = models.DateTimeField(auto_now_add=True)
    updated      = models.DateTimeField(auto_now=True)



    objects      = BlogPostManager()



    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_edit_url(self):
        return f"/blog/{self.slug}/edit"

    def get_delete_url(self):
        return f"/blog/{self.slug}/delete"