import logging

def setup_logger(log_file='output.log'):
    """Setup logging configuration"""
    logging.basicConfig(filename=log_file,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

def main():
    # Set up the logger
    setup_logger()

    # Example usage
    logging.info('This is an informational message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')

if __name__ == "__main__":
    main()