# importing neccessary map reduce classes from libraries
from mrjob.job import MRJob
from mrjob.step import MRStep


class RatingsBreakdown(MRJob):
    """
        Inherits from MRJob. (so it is a mapreduce job obv) with 1 step
        Mapper function = get_ratings
        Reducer function = count_ratings
    """
    def steps(self):
        return [
            MRStep(mapper=self.get_ratings,
                   reducer=self.count_ratings)
        ]

    def get_ratings(self, _, line):
        """
        splits a line up by a tab character from file ~/data/u.data
        inputs:
            userID, movieID, rating, timestamp
            0	  , 50     ,	  5,  881250949
            0	  , 172    ,	  5,  881250949
            etc...
        rating = a value from 1 - 5
        yields:
            rating = 5,5...(the key being used)
            value = 1
        output:
            value = 21203
                a generator object for each key value pair <generator object <genexpr> at 0x7f2ff881d780>
            rating = "5"
                a key to group the generator object by 
        """
        (userID, movieID, rating, timestamp) = line.split('\t') # \t is a tab
        value = 1
        yield rating, value

    def count_ratings(self, rating, value_generator):
        """ 
        inputs:
            output from mapper_get_ratings
            rating = number between 1-5
            value_generator = a generator object for each key value pair on going adds values
            value_generator != value from mapper_get_ratings BUT a place where the value is placed.
            value generator = [1,1,1,1,...etc] on going job until end
        yields:
             key = rating
             values = all the 1s added together
        """
        values = sum(value_generator)
        yield rating, values

if __name__ == '__main__':
    RatingsBreakdown.run()
