import logging

def setup_logging():
    # Configura o sistema de logging.
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
