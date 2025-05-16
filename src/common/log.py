import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path

log_dirpath = "logs"
if not os.path.exists(log_dirpath):
    os.makedirs(log_dirpath)


class Log:
    # 运行日志
    # 创建一个RotatingFileHandler对象
    handler_file = RotatingFileHandler(
        filename=Path(log_dirpath) / "run.log",
        mode="a",
        maxBytes=1024 * 1024 * 1024,  # 1G日志
        backupCount=2,
        encoding="utf-8",
    )
    handler_console = logging.StreamHandler()

    # 设置日志级别
    handler_file.setLevel("INFO")
    handler_console.setLevel("DEBUG")
    # 创建一个格式化器
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler_file.setFormatter(formatter)
    handler_console.setFormatter(formatter)


def get_logger(logger_name: str) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.propagate = False
    logger.setLevel("DEBUG")
    logger.addHandler(Log.handler_file)
    logger.addHandler(Log.handler_console)
    return logger
