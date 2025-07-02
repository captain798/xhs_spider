# 小红书数据爬虫项目

## 项目简介
基于Scrapy框架的小红书数据采集系统，支持图文/视频笔记元数据抓取、用户信息采集、评论数据获取，并集成MongoDB存储。

## 主要功能
✅ 支持推荐页/搜索页笔记抓取  
✅ 自动识别图文/视频类型笔记  
✅ 元数据采集（标题、作者、发布时间等）  
✅ 多媒体链接抓取（封面图/视频直链）  
✅ MongoDB持久化存储  
✅ 随机请求延迟防封禁

## 环境要求
- Python 3.8+  
- Scrapy 2.8+  
- pymongo 4.3+  
- MongoDB 5.0+


## 配置说明
1. 在`settings.py`中配置MongoDB连接信息：
```python
MONGO_URI = 'mongodb://localhost:27017'
MONGO_DATABASE = 'redbook'
```

2. 视频存储路径默认在`database/videos`目录

## 快速开始

    直接运行run_spider.py

## 项目结构
```
redbook/
├── spiders/          # 爬虫目录
│   ├── __init__.py
│   └── xhs.py        # 主爬虫逻辑
├── items.py          # 数据模型定义
├── pipelines.py      # MongoDB存储管道
├── middlewares.py    # 中间件配置
└── videodownloader.py # 视频下载模块
```

## 数据示例
```json
{
  "title": "夏日穿搭指南",
  "author": "时尚达人",
  "like_count": 2458,
  "media_url": "https://sns-video.xhscdn.com/...mp4",
  "collect_count": 892,
  "publish_time": "2023-07-15"
}
```

## 注意事项
1. 请合理设置请求间隔（默认1-3秒随机延迟）
2. 视频下载功能需自行调用`videodownloader.py`模块
3. 遵守平台robots.txt规则，合理使用数据"
    