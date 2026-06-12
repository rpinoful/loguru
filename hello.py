from loguru import logger
import sys 


# # classic message - debug
# logger.debug('debug message')



# # log - for info message
# logger.info('info message')

# # log - for error
# logger.error('ERROR MESSAGE')



# # adding log level
# logger.remove()

# logger.add(sys.stderr, level="TRACE")


# logger.trace("Will this be visible?")

# logger.debug("A debug message")

# logger.info("An info message")



# customizing message
logger.remove()
logger.add(sys.stderr,format="{message}")
logger.info('simple message')