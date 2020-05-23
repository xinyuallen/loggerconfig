# author: yang time:2020/5/23.
#拿到日志的产生者loggers
#第一个日志产生者kkk
#第二个日志产生者bbb

#但是需要先导入日志配置字典LOGGING_DIC
import settings
import settings
from logging import config,getLogger

config.dictConfig(settings.LOGGING_DIC)
# logger1=getLogger('kkk')
logger2=getLogger('bbb')

# logger1.info('这是一个info日志')
logger2.info('这是一个log2info日志')

#补充两个重要知识点
#1.日志的命名
#''默认的空key,当没有匹配的名字时就用这个，名字匹配传入的，记得在settings里留一个' '空key
#  日志名是区分日志的非常重要的标志
#2.日志轮转
# 日志记录着程序员