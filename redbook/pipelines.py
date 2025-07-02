from itemadapter import ItemAdapter
from redbook.items import RedbookItem, CommentItem  # 导入新定义的Item类
import pymongo 

class CommentPipeline:
    def process_item(self, item, spider):
        return item

class RedbookPipeline:
    def process_item(self, item, spider):
        return item

class MongoDBPipeline:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'redbook')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection_name = 'notes' if isinstance(item, RedbookItem) else 'comments'
        self.db[collection_name].insert_one(ItemAdapter(item).asdict())
        return item
