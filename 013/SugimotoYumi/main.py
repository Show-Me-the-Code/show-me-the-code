from scrapy.cmdline import execute

import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scapy","crawl","jobbole"])
# execute(["scapy","crawl","zhihu"])
execute(["scrapy","crawl","Yumi"])