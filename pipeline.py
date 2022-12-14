from elt.transformation.transformer import RFMTransformer

class Pipeline(object):
    def __init__(self):
        self.transformer = RFMTransformer()

    def run(self):
        self.transformer.transform_data()