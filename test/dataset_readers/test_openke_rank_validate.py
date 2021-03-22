from test import setup
from datasets.dataset_readers.openke_rank_validate import OpenKERankValidationDatasetReader
from allennlp.data.fields import ArrayField
from allennlp.common.params import Params
from allennlp.training import util
from pathlib import Path
import datasets


def test_simple():
    test_data_path = Path(
        '/Users/dhruv/UnsyncedDocuments/IESL/kb_completion/datasets/.data/test'
    )
    reader = OpenKERankValidationDatasetReader(all_datadir=test_data_path)
    instances = reader.read("asd")

    for i, instance in enumerate(instances):
        print(i, instance)


def test_from_params():
    params = Params({
        "dataset_reader": {
            "type":
            "openke-rank-validation-dataset",
            "dataset_name":
            'FB15K237',
            "all_datadir":
            '/Users/dhruv/UnsyncedDocuments/IESL/kb_completion/datasets/.data/test',
            "file_reader": {
                "type": "rank-test-id-reader"
            }
        },
        "train_data_path": None
    })
    dataset = util.datasets_from_params(params.duplicate())

    for i, instance in enumerate(dataset['train']):
        print(i, instance)


def test_from_params2():
    params = Params({
        "dataset_reader": {
            "type":
            "openke-rank-validation-dataset",
            "dataset_name":
            'FB15K237',
            "all_datadir":
            '/Users/dhruv/UnsyncedDocuments/IESL/kb_completion/datasets/.data/test',
            "file_reader": {
                "type": "rank-val-id-reader"
            }
        },
        "train_data_path": None
    })
    dataset = util.datasets_from_params(params.duplicate())

    for i, instance in enumerate(dataset['train']):
        print(i, instance)


if __name__ == '__main__':
    test_from_params()
    test_from_params2()
