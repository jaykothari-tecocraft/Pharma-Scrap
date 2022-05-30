# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class PharmaPipeline:
    count = 1
    def __init__(self):
        self.connection()
        self.createtable()

    def process_item(self, item, spider):
        self.corsur.execute(f'''INSERT INTO MED VALUES({self.count},"{item['name']}","{item['img']}")''')
        self.conn.commit()
        self.count += 1
        return item

    def connection(self):
        self.conn = sqlite3.connect('./data.db')
        self.corsur = self.conn.cursor()

    def createtable(self):
        self.corsur.execute('DROP TABLE IF EXISTS MED;')
        self.corsur.execute('CREATE TABLE MED(id INT,name VARCHAR, img VARCHAR);')
