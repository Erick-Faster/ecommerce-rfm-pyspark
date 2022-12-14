import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from config import config

class RFMTransformer(object):
    def __init__(self):

        self.path_elt_transformation = config.PATH_ELT_TRANSFORMATION

        self.rfm_script = None
        self.kernel = None
        
    def load_rfm_script(self):
        filename = f'{self.path_elt_transformation}/RFM.ipynb'
        with open(filename) as ff:
            self.rfm_script = nbformat.read(ff, nbformat.NO_CONVERT)
            
        self.kernel = ExecutePreprocessor(timeout=3000, kernel_name='python3')

    def transform_data(self):
        self.load_rfm_script()
        self.kernel.preprocess(self.rfm_script)
