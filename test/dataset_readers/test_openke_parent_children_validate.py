from datasets.dataset_readers.openke_parent_children_validate import OpenKESingleRelationParentChildrenValidationDatasetReader
from allennlp.data.fields import ArrayField
from allennlp.common.params import Params
from allennlp.training import util
from pathlib import Path


def test_simple():
    test_data_path = Path(
        '/Users/dhruv/UnsyncedDocuments/IESL/kb_completion/datasets/.data/test'
    )
    reader = OpenKESingleRelationParentChildrenValidationDatasetReader(
        all_datadir=test_data_path)
    instances = reader.read("asd")

    for i, instance in enumerate(instances):
        print(i, instance)


def test_from_params():
    params = Params({
        "dataset_reader": {
            "type":
            'openke-single-relation-parent-childrem-validation-dataset',
            "dataset_name":
            'WNTC',
            "all_datadir":
            '/Users/dhruv/UnsyncedDocuments/IESL/kb_completion/datasets/.data/test',
            "validation_file":
            'entity2id.txt',
            "all_true_files": ['all_true.txt']
        },
        "train_data_path": None
    })
    dataset = util.datasets_from_params(params.duplicate())

    for i, instance in enumerate(dataset['train']):
        print(i, instance)

        for name, field in instance.items():
            if isinstance(field, ArrayField):
                print(name, field.array)


if __name__ == '__main__':
    test_from_params()
