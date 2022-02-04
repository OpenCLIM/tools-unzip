import subprocess
from pathlib import Path
import os
from os.path import join
import logging

# setup paths to data
data = Path(os.getenv('DATA_PATH', '/data'))

data.mkdir(exist_ok=True)

inputs = data / 'inputs'

outputs = data / 'outputs'

outputs.mkdir(exist_ok=True)

logger = logging.getLogger('tools-unzip')
logger.setLevel(logging.INFO)
fh = logging.FileHandler(outputs / 'tools-unzip.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

archive_to_unzip = os.getenv('ARCHIVE_PATH')

logger.info('Running unzip process')

subprocess.call(['unzip',
                 join('/data/inputs', archive_to_unzip),    # source
                 '-d', outputs,         # destination directory
                 ])

logger.info('Zip completed')
