from GarbageGauge.logger import logging
from GarbageGauge.exception import AppException

try:
    a = 3 / "s"
    
except Exception as e:
    raise AppException(e, sys)
