import logging

def create_logs():
    logging.info("I inform you that your rent is due to tomorrow")
    logging.warning("Don't be late again!")
    logging.debug("Let's go and find some more bugs")
    logging.error("Opps... Something broke")


def log_return(log_level):
    logger = logging.getLogger()
    logger.setLevel(log_level.upper())
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s')
    create_logs()

if __name__ == "__main__":
    log_return(input("Choose log level: "))