from logging_config import setup_logging


logger = setup_logging()


def main():
    logger.info("Hello from uvtemplate!")


if __name__ == "__main__":
    main()
