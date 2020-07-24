class Titanic_dataset:
    def __init__(self, path):
        self.__path = path
        self.__dataset = None

    # This method doing preparation of dataset for the training process
    # firstly, it read dataset from file, after this it filters data
    def __prepare_dataset(self):
        f = open(self.__path, "r")
        dataset_file = f.readlines()
        f.close()
        
        new_dataset = []
        for i in range(len(dataset_file)):
            dataline = dataset_file[i]
            if dataline.count('"') != 0:
                x = dataline.index('"')
                y = len(dataline) - dataline[::-1].index('"')
                temp = list(dataline)
                temp = temp[:x] + temp[y:]
                dataline = "".join(temp)
                dataset_file[i] = dataline.replace("\n","").split(',')[1:]
                dataline = self.__filter_ages(dataset_file[i])
                if dataline is not None:
                    new_dataset.append(dataline)
            else:
                dataline = dataline.replace("\n","").split(',')[1:]
                new_dataset.append(dataline)

        self.__dataset = [list(x) for x in zip(*new_dataset)]
        self.__filter_columns()
        self.__convert_outcome()

    def get_dataset(self):
        if self.__dataset is None:
            #try:
                self.__prepare_dataset()
            #except:
             #   print('Error occured while trying to prepare Titanic training dataset.')
              #  exit()
        return self.__dataset

    # This method moves column with outcomes to the end of the list, and removes
    # columns which are unnecessury, by my opinion
    def __filter_columns(self):
        self.__dataset = self.__dataset[1:2] + self.__dataset[3:7] + self.__dataset[0:1]


    # In dataset we have outcome with zeros and ones, but our algorithm works
    # only with "Yes" and "No" values, so we need to convert them
    def __convert_outcome(self):
        for i in range(len(self.__dataset[-1])) :
            self.__dataset[-1][i] = "Yes" if self.__dataset[-1][i] == '1' else "No"

    # This method makes age classes, and change year with its group
    # if person has no name record, its column will be removed from dataset / try with 5th class for this, in testing phase
    # 0 - 24 -> 1
    # 25 - 49 -> 2
    # 50 - 74 -> 3
    # 75+ -> 4
    def __filter_ages(self, dataline):
        if dataline[4] == "":
            #dataline[4] = "5"
            #return dataline
            return None
        
        if float(dataline[4]) < 1:
            dataline[4] = str(float(dataline[4]) * 100)

        if float(dataline[4]) < 25:
            dataline[4] = "1"
        elif float(dataline[4]) < 50:
            dataline[4] = "2"
        elif float(dataline[4]) < 75:
            dataline[4] = "3"
        else:
            dataline[4] = "4"

        return dataline
