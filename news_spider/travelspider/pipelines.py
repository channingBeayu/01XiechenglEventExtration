# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector
# import MySQLdb
# import pymysql

class TravelspiderPipeline(object):
    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost',
                                        user='root',
                                        passwd='root',
                                        db='xiecheng',
                                        charset='utf8')
        self.cursor = self.conn.cursor()

    '''处理采集资讯, 存储至Mongodb数据库'''
    def process_item(self, item, spider):
        print(dict(item))

        sql = "insert into travels(url, title, content) values (%s, %s, %s)"
        self.cursor.execute(sql, (item['url'], str(item['title']), str(item['content'])))
        self.conn.commit()

        # try:
        #     self.col.insert(dict(item))
        # except (pymongo.errors.WriteError, KeyError) as err:
        #     raise DropItem("Duplicated Item: {}".format(item['name']))
        return item

    def close_spider(self, spider):
        """在爬虫任务结束时被调用一次"""
        self.conn.close()
        self.cursor.close()