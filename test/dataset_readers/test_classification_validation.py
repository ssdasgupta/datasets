from datasets.dataset_readers.classification_validate import ClassificationValidationDatasetReader
from allennlp.data.fields import ArrayField
from allennlp.common.params import Params
from allennlp.training import util
from pathlib import Path


def test_simple():
    test_data_path = Path(
        '/Users/dhruv/UnsyncedDocuments/IESL/kb_completion/datasets/.data/test'
    )
    reader = ClassificationValidationDatasetReader(
        dataset_name='WNTC', all_datadir=test_data_path)
    instances = reader.read()
    print(instances)

    for instance in instances:
        print(instance)

        for name, field in instance.items():
            if isinstance(field, ArrayField):
                print(name, field.array)


def test_from_params():
    params = Params({
        "dataset_reader": {
            "type":
            "classification-validation-dataset",
            "dataset_name":
            'WNTC',
            "all_datadir":
            '/Users/dhruv/UnsyncedDocuments/IESL/kb_completion/datasets/.data/test',
        },
        "train_data_path": None
    })
    dataset = util.datasets_from_params(params.duplicate())
    print(dataset)

    for instance in dataset['train']:
        print(instance)

        for name, field in instance.items():
            if isinstance(field, ArrayField):
                print(name, field.array)


if __name__ == "__main__":
    test_simple()
    test_from_params()
