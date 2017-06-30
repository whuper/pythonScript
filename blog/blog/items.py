# -*- coding: utf-8 -*-

from scrapy.item import Item, Field


class Website(Item):

    title = Field()
    description = Field()
    url = Field()
