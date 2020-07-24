from Tree import Tree
from Trainer import Trainer
from Play_dataset import Play_dataset
from Titanic_dataset import Titanic_dataset


if __name__ == "__main__":
    tree = Tree()

    pd = Play_dataset("play_dataset.txt")
    trainer = Trainer(tree, pd.get_dataset())
    trainer.begin_training()

    tree.print_tree()

    #td = Titanic_dataset("titanic_dataset_train.csv")
    
    #Trainer(tree, td.get_dataset()).begin_training()

    #tree.print_tree()