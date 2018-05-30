import pickle

class dumpable(object):

    def dumpToFile(instace, target):
        pickle.dump(instance, target)

    def loadFromFile(instance, source):
        instance = pickle.load(source)

        