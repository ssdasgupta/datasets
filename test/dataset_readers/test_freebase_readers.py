from datasets.dataset_readers.freebase_readers import (
    OpenKEDatasetReaderWithNegativeSampling,
    OpenKEClassificationDatasetReaderWithNegativeSampling, OpenKEDatasetReader)
from allennlp.data.fields import ArrayField, LabelField
from allennlp.common.params import Params
from allennlp.training import util
from pathlib import Path


def test_simple1():
    test_data_path = Path(
        '/Users/dhruv/UnsyncedDocuments/IESL/kb_completion/datasets/.data/test'
    )
    reader = OpenKEDatasetReaderWithNegativeSampling(
        all_datadir=test_data_path)
    instances = reader.read()
    print(instances)

    for instance in instances:
        print(instance)

        for name, field in instance.items():
            if isinstance(field, ArrayField):
                print(name, field.array)


def test_from_params1():
    params = Params({
        "dataset_reader": {
            "type":
            "openke-dataset-negative-sampling",
            "dataset_name":
            'FB15K237',
            "all_datadir":
            '/Users/dhruv/UnsyncedDocuments/IESL/kb_completion/datasets/.data/test',
            "mode":
            "train",
            "number_negative_samples":
            2
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


def test_simple2():
    test_data_path = Path(
        '/Users/dhruv/UnsyncedDocuments/IESL/kb_completion/datasets/.data/test'
    )
    reader = OpenKEClassificationDatasetReaderWithNegativeSampling(
        all_datadir=test_data_path)
    instances = reader.read()
    print(instances)

    for instance in instances:
        print(instance)

        for name, field in instance.items():
            if isinstance(field, ArrayField):
                print(name, field.array)


def test_from_params2():
    params = Params({
        "dataset_reader": {
            "type":
            "openke-classification-dataset-negative-sampling",
            "dataset_name":
            'FB15K237',
            "all_datadir":
            '/Users/dhruv/UnsyncedDocuments/IESL/kb_completion/datasets/.data/test',
            "mode":
            "train",
            "number_negative_samples":
            2
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

            if isinstance(field, LabelField):
                print(name, field.label)


def test_simple3():
    test_data_path = Path(
        '/Users/dhruv/UnsyncedDocuments/IESL/kb_completion/datasets/.data/test'
    )
    reader = OpenKEDatasetReader(all_datadir=test_data_path)
    instances = reader.read()
    print(instances)

    for instance in instances:
        print(instance)

        for name, field in instance.items():
            if isinstance(field, ArrayField):
                print(name, field.array)


def test_from_params3():
    params = Params({
        "dataset_reader": {
            "type":
            "openke-dataset",
            "dataset_name":
            'FB15K237',
            "all_datadir":
            '/Users/dhruv/UnsyncedDocuments/IESL/kb_completion/datasets/.data/test',
            "mode":
            "train",
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

            if isinstance(field, LabelField):
                print(name, field.label)


if __name__ == "__main__":
    test_simple1()
    test_from_params1()
    test_simple2()
    test_from_params2()
    test_simple3()
    test_from_params3()
