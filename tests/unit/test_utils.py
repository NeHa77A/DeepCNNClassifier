import pytest
from DeepClassifier.utils import read_yaml
from pathlib import Path
from box import ConfigBox

class Test_read_yaml:
    yaml_file =[
        "D:/Template for Data Science/DeepCNNClassifier/tests/test_data/empty.yaml",
        "D:/Template for Data Science/DeepCNNClassifier/tests/test_data/demo.yaml"
    ]

    def test_read_yaml_empty(self):
        with pytest.raises(ValueError):
            read_yaml(Path(self.yaml_file[0]))

    def test_read_yaml_return_yaml(self):
        responese = read_yaml(Path(self.yaml_file[-1]))
        assert isinstance(responese,ConfigBox)

