from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().\
            filter(published_date__lte=timezone.now()).order_by('published_date')


class BlogDb(models.Model):
    """
    This is model class which is used for database creation.
    """
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, default=None, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    published = PublishedManager()

    def publish(self):
        """
        This method can be used to commit entries from django shell into the database.
        Django shell can be invoked using python3 manage.py shell.
        :return:
        """
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
