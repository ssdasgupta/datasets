import logging
import os
import sys

LEVEL = logging.DEBUG

sys.path.insert(
    0, os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s", level=LEVEL)

logger = logging.getLogger(__name__)
