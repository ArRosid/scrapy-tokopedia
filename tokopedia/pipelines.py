# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from tokopedia.models import Discount, db_connect, create_table

class TokopediaPipeline(object):
    def process_item(self, item, spider):
        return item

class SaveDiscountsPipeline(object):
    
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
    
    def process_item(self, item, spider):
        """Save discounts in the database
        This method is called for every item pipeline component
        """
        session = self.Session()
        discount = Discount()

        discount.description = item["description"]
        discount.periode = item["periode"]
        discount.minimum_transaction = item["minimum_transaction"]
        discount.promo_code = item["promo_code"]

        try:
            session.add(discount)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item