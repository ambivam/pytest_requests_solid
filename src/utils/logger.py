import logging
import os

class Logger:
    """Logger Utility to handle logging"""
    
    _logger = None  # Singleton Logger instance

    @staticmethod
    def get_logger():
        """Returns a singleton logger instance"""
        if Logger._logger is None:
            log_file = "logs/test_log.log"
            os.makedirs(os.path.dirname(log_file), exist_ok=True)

            Logger._logger = logging.getLogger("API_Framework")
            Logger._logger.setLevel(logging.INFO)

            # Formatter
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )

            # File Handler
            file_handler = logging.FileHandler(log_file, mode="a")
            file_handler.setFormatter(formatter)

            # Console Handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            # Add Handlers
            Logger._logger.addHandler(file_handler)
            Logger._logger.addHandler(console_handler)

        return Logger._logger
