from Tree import Tree
from Trainer import Trainer

if __name__ == "__main__":
    tree = Tree()

    f = open("play_dataset.txt", "r")
    dataset_file = f.readlines()
    f.close()
    for i in range(len(dataset_file)):
        dataline = dataset_file[i].replace("\n", "").split(",")[1:]
        dataset_file[i] = dataline

    dataset = [list(x) for x in zip(*dataset_file)]
        
    trainer = Trainer(tree, dataset)
    trainer.begin_training()

    tree.print_tree()