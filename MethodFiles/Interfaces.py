import abc

class GetDaysLeftInterface(abc.ABC):
    @abc.abstractmethod
    def getDaysLeft(self):
        pass