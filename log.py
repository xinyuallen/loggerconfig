# author: yang time:2020/5/23.
import logging
#输出日志

logging.basicConfig(
    #1.日志输出位置：1.终端 2.文件
    filename='access.log',#不指定，默认打印到终端

    #2.日志格式
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s: %(message)s',
    #3.时间格式
    datefmt='%Y-%m-%d %H:%M:%S %p', #定制时间格式，替换asctime
    #4日志级别
    #critical=>50
    #error=>40
    #warning=>30
    #info=>20
    #debug=>10
    level=30,
)
logging.debug('调试debug')#10
logging.info('消息info')#20
logging.warning('警告warn')#30
logging.error('错误error')#40
logging.critical('严重critical')#50
