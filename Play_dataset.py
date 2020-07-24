class Play_dataset:
    def __init__(self, path):
        self.__path = path
        self.__dataset = None

    def __prepare_dataset(self):
        f = open(self.__path, "r")
        dataset_file = f.readlines()
        f.close()


        for i in range(len(dataset_file)):
            dataline = dataset_file[i].replace("\n", "").split(",")[1:]
            dataset_file[i] = dataline

        self.__dataset = [list(x) for x in zip(*dataset_file)]

    def get_dataset(self):
        if self.__dataset is None:
            try:
                self.__prepare_dataset()
            except:
                print("Error occured while trying to prepare Play dataset.")
                exit()
        return self.__dataset