# -*- coding:utf-8 -*-


from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel
from menuresolver.models import Menu, Item

Menu.panels = [
            FieldPanel('menu_text', classname="full title"),
            FieldPanel('slug'),
            FieldRowPanel([
                FieldPanel('wrap_tag'),
                FieldPanel('class_tag'),
                FieldPanel('attrs_tag'),
            ]),
        ]

Item.panels = [
            FieldPanel('menu'),
            FieldPanel('item_text', classname="full"),
            FieldPanel('slug'),
            FieldPanel('url'),
            #FieldPanel('sort_order'),
            FieldPanel('wrap_tag'),
            FieldPanel('class_tag'),
            FieldPanel('attrs_tag'),
            FieldRowPanel([
                FieldPanel('content_type', classname="col6"),
                FieldPanel('object_id', classname="col6"),
            ]),
            FieldPanel('link_to_email'),
            FieldPanel('is_link'),
            FieldPanel('link_target'),
        ]


register_snippet(Menu)
register_snippet(Item)
