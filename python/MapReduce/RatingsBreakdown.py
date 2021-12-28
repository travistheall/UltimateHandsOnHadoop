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
        This creates a value list where len([1,1,1,...1]) => 21203 for rating 5
        output that feeds into reducer:
            value_generator = [1,1,1,...1] 21203
                a generator object for each key value pair <generator object <genexpr> at 0x7f2ff881d780>
                where [x for x in value_generator] => [1,1,1,...1]
            rating = "5"
                a key to group the generator object by 
        """
        (userID, movieID, rating, timestamp) = line.split("\t")
        value = 1
        yield rating, value

    def count_ratings(self, rating, value_generator):
        """ 
        inputs:
            output from get_ratings
            rating = string version of a number between 1-5
            value_generator = a generator object for each key value pair on going adds values
            value_generator != value from get_ratings BUT a place where the value is placed.
            value generator = [1,1,1,1,...etc] on going job until end
        yields:
             rating
             summed_values = all the 1s added together

        # value_list = [x for x in value_generator]
        # print(value_list) => len([1,1,1,...1]) => 21203 for rating 5
        # summed_values = sum(value_list)
        """
        summed_values = sum(value_generator)
        yield rating, summed_values

if __name__ == '__main__':
    RatingsBreakdown.run()
    """
    output:
    "4"     34174
    "5"     21203
    "1"     6111
    "2"     11370
    "3"     27145
    """
