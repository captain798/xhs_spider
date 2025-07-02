import scrapy

class RedbookItem(scrapy.Item):
    # 笔记基本信息
    note_id = scrapy.Field()      # 笔记唯一ID
    title = scrapy.Field()        # 笔记标题
    author = scrapy.Field()       # 作者名称
    author_link = scrapy.Field()  # 作者主页链接
    note_link = scrapy.Field()    # 笔记详情链接
    content = scrapy.Field()      # 笔记正文内容
    time = scrapy.Field()      # 发布时间
    type = scrapy.Field()  # 新增视频类型标识字段
    like_count = scrapy.Field()  # 点赞数
    comment_count = scrapy.Field()  # 评论数
    collect_count = scrapy.Field()  # 收藏数
    keywords = scrapy.Field() # 关键词
    description = scrapy.Field() # 描述
    media_url = scrapy.Field()


class CommentItem(scrapy.Item):
    # 评论关联信息
    note_id = scrapy.Field()      # 关联笔记ID
    comment_id = scrapy.Field()   # 评论唯一ID
    # 评论内容
    author = scrapy.Field()       # 评论作者
    author_link = scrapy.Field()  # 评论作者主页链接
    content = scrapy.Field()      # 评论内容
    time_ip = scrapy.Field()      # 评论时间和IP


    