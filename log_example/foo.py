import logging
from time import sleep

logging.basicConfig(filename="example2.log", format="%(asctime)s:%(levelname)s:%(message)s")
i=0
while i < 100:
	logging.warning("new problem: {}".format(i))
	i += 1
	sleep(2)
logging.warning("finished!: {}".format(i))