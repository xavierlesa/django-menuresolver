# -*- encoding:utf-8 -*-

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Orderable(models.Model):
    sort_order = models.IntegerField(null=True, blank=True, editable=False)
    sort_order_field = 'sort_order'

    class Meta:
        abstract = True
        ordering = ['sort_order']

class Menu(models.Model):
    menu_text = models.CharField(max_length = 255)
    slug = models.SlugField(max_length = 255, blank=True, null=True)

    wrap_tag = models.CharField("Tag HTML", max_length = 255, default="ul")
    class_tag = models.CharField("Class", max_length = 255, default="", blank=True, null=True)
    attrs_tag = models.CharField("Atributos", max_length = 255, default="", blank=True, null=True)

    def __unicode__(self):
        return self.menu_text

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.menu_text)
        super(Menu, self).save(*args,**kwargs)


class Item(Orderable):
    LINK_TARGET_CHOICES = (
            (None, u"nada"),
            ("_blank", u"Nueva pestaña"),
            ("_new", u"Nueva ventana"),
            ("_top", u"Arriba"),
    )
    menu = models.ForeignKey("menuresolver.Menu", related_name="item_menu")
    item_text = models.CharField("Titulo del item", max_length = 255)
    slug = models.CharField(max_length = 255, blank=True, null=True)
    # URl Alternativa
    url = models.URLField("URL alternativa", blank=True, null=True)

    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="+")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    # Manipulacion HTML
    wrap_tag = models.CharField("Tag HTML", max_length = 255, default="li") #<li><a %(attrs)s>%(inside)s</%(tag)s>
    class_tag = models.CharField("Class", max_length = 255, default="", blank=True, null=True)
    attrs_tag = models.CharField("Atributos", max_length = 255, blank=True, null=True)
    
    link_to_email = models.CharField("Link a Mail", max_length=255, blank=True,
            null=True, help_text="Para tomar este link dejar campo URL y objetos relacionados vacios")
    
    is_link = models.BooleanField("Es link", default=True)
    link_target = models.CharField("Modo de apertura", max_length=40, blank=True, 
            null=True, choices=LINK_TARGET_CHOICES)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.item_text)
        super(Item, self).save(*args,**kwargs)

    def get_absolute_url(self):
        if self.url:
            return self.url 
        elif self.link_to_email:
            return "mailto:%s" % self.link_to_email
      
        try:
            url = self.content_object.get_absolute_url()
        except:
            try:
                url = self.content_object.url
            except:
                url = "/%s/" % self.slug

        return url
    
    def is_menu(self):
        """
        Bool - Anidamiento de menues
        """

        return self.content_type and isinstance(self.content_object, Menu)

    def __unicode__(self):
        return "%s -> %s" % (self.menu, self.item_text)
