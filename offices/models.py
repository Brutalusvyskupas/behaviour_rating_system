from django.db import models
from django.utils.text import slugify


class WorkOffice(models.Model):
    office_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=30, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.office_name)
        super(WorkOffice, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'offices'

    def __str__(self):
        return self.office_name

    # def get_absolute_url(self):
    #     return reverse('posts:list_of_posts_by_category', args=[self.slug])
