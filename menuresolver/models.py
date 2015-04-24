# -*- encoding:utf-8 -*-

from django.db import models
from wagtail.wagtailcore.models import Orderable
from modelcluster.fields import ParentalKey
from django.template.defaultfilters import slugify
from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel
from wagtail.wagtailsnippets.models import register_snippet
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


@register_snippet
class Menu(models.Model):
    menu_text = models.CharField(max_length = 255)
    slug = models.SlugField(max_length = 255)

    wrap_tag = models.CharField("Tag HTML", max_length = 255, default="ul")
    class_tag = models.CharField("Class", max_length = 255, default="", null=True)
    attrs_tag = models.CharField("Atributos", max_length = 255, default="", blank=True, null=True)

    # Representacion 
    def __unicode__(self):
        return self.menu_text

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.menu_text)
        super(Menu, self).save(*args,**kwargs)
    #Visualizacion de Paneles 
    panels = [
            FieldPanel('menu_text', classname="full title"),
            FieldPanel('slug'),
            FieldRowPanel([
                FieldPanel('wrap_tag', classname="col4"),
                FieldPanel('class_tag', classname="col4"),
                FieldPanel('attrs_tag', classname="col4"),
            ]),
        ]
#Fin Class Menu


@register_snippet
class Item(Orderable):
    LINK_TARGET_CHOICES = (
            (None, u"nada"),
            ("_blank", u"Nueva pestaña"),
            ("_new", u"Nueva ventana"),
            ("_top", u"Arriba"),
    )
    menu = models.ForeignKey("menuresolver.Menu", related_name="items")
    item_text = models.CharField("Titulo del item", max_length = 255)
    slug = models.CharField(max_length = 255)
    #URl Alternativa
    url = models.URLField("URL alternativa", blank=True, null=True)

    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    #Manipulacion HTML
    wrap_tag = models.CharField("Tag HTML", max_length = 255, default="li") #<li><a %(attrs)s>%(inside)s</%(tag)s>
    class_tag = models.CharField("Class", max_length = 255, null=True)
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
                url = self.slug

        return url
    
    #Bool - Anidamiento de menues
    def is_menu(self):
        return self.content_type and isinstance(self.content_object, Menu)

    #Representacion 
    def __unicode__(self):
        return "%s -> %s" % (self.menu, self.item_text)

    panels = [
            FieldPanel('menu'),
            FieldPanel('item_text', classname="full"),
            FieldPanel('slug'),
            FieldPanel('url'),
            FieldRowPanel([
                FieldPanel('wrap_tag', classname="col4"),
                FieldPanel('class_tag', classname="col4"),
                FieldPanel('attrs_tag', classname="col4"),
            ]),
            FieldRowPanel([
                FieldPanel('content_type',classname="col7"),
                FieldPanel('object_id', classname="col3"),
                ]),
            FieldPanel('link_to_email'),
            FieldRowPanel([
                FieldPanel('is_link', classname="col3"),
                FieldPanel('link_target', classname="col7"),
                ]),
            ]
# Fin Class Item
