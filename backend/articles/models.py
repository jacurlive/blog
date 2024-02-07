from django.db import models
from django.utils.text import slugify


class About(models.Model):
    full_name = models.CharField(max_length=300)
    specialization = models.CharField(max_length=255)
    image = models.ImageField(upload_to='about/', default=None, blank=True)
    instagram_link = models.URLField()
    github_link = models.URLField()
    linkedin_link = models.URLField()
    telegram_link = models.URLField()
    short_bio = models.TextField()
    bio = models.TextField()


class Blog(models.Model):
    title = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to='posts/', default=None, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        while Blog.objects.filter(slug=self.slug).exists():
            slug = Blog.objects.filter(slug=self.slug).first().slug
            if '-' in slug:
                try:
                    if slug.split('-')[-1] in self.title:
                        self.slug += '-1'
                    else:
                        self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                except Exception as e:
                    self.slug = slug + '-1'
            else:
                self.slug += '-1'

        super().save(*args, **kwargs)

