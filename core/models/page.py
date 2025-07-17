from django.db import models
from libs.models import TimeInfo, SEOBasicAbstract 
from django.utils.text import slugify 
from tinymce.models import HTMLField 


class GroupPage(TimeInfo):
    name = models.CharField(max_length=255, unique=True)
    display_in_footer = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = 'Group Page'
        db_table = 'group_pages'


    def __str__(self):
        return self.name 
    

class Topic(TimeInfo):
    name = models.CharField(max_length=255, unique=True)


    class Meta:
        verbose_name_plural = 'Topic'
        db_table = 'topics'


    def __str__(self):
        return self.name 
    


class StaticPage(TimeInfo, SEOBasicAbstract):
    PAGE_STATUS = (
        (0, 'Draft'),
        (1, 'Delete'),
        (2, 'Publish')
    )

    name = models.CharField(max_length=255, unique=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=300, null=True, blank=True)
    use_auto_slug = models.BooleanField(default=False)
    group = models.ForeignKey(GroupPage, on_delete=models.SET_NULL, null=True, blank=True)
    content = HTMLField(null=True, blank=True)
    display_status = models.SmallIntegerField(default=2, choices=PAGE_STATUS)


    class Meta:
        verbose_name_plural = 'Static Page'
        db_table = 'static_pages'


    def __str__(self):
        return self.name 
    

    def save(self, *args, **kwargs):
        if not self.slug: # and self.use_auto_slug
            self.slug = slugify(self.name)
        super(StaticPage, self).save(*args, **kwargs)

