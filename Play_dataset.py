class Play_dataset:
    def __init__(self, path):
        self.__path = path
        self.__training_dataset = None
        self.__testing_dataset = None

    def __prepare_training_dataset(self):
        f = open(self.__path, "r")
        dataset_file = f.readlines()
        f.close()


        for i in range(len(dataset_file)):
            dataline = dataset_file[i].replace("\n", "").split(",")[1:]
            dataset_file[i] = dataline

        self.__training_dataset = [list(x) for x in zip(*dataset_file)]

    def get_training_dataset(self):
        if self.__training_dataset is None:
            try:
                self.__prepare_training_dataset()
            except:
                print("Error occured while trying to prepare Play training dataset.")
                exit()
        return self.__training_dataset

    def __prepare_testing_dataset(self):
        self.__testing_dataset = [list(x) for x in zip(*self.get_training_dataset())]

    def get_testing_dataset(self):
        if self.__testing_dataset is None:
            try:
                self.__prepare_testing_dataset()
            except:
                print("Error occured while trying to prepare Play testing dataset.")
                exit()
        return self.__testing_dataset









