from fedata.hub.generate_dataset import generate_dataset
import os

def main():
    data_config = {
    "dataset_name" : "mnist",
    "split_type" : "missing_classes_clustered",
    "shards": 15,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 15,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2, 3, 4],
            2: [5, 6, 7, 8, 9],
            3: [10, 11, 12, 13, 14]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7, 8, 9], # 0, 1, 2, 3 present only
            2: [0, 1, 2, 3, 7, 8, 9], # 4, 5, 6 present only
            3: [0, 1, 2, 3, 4, 5, 6] # 7, 8, 9 present only
        }
    }
    generate_dataset(config=data_config)


if __name__ == "__main__":
    main()