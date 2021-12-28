from mrjob.job import MRJob
from mrjob.step import MRStep


class MovieBreakdown(MRJob):
    """
    Challenge Exercise Stretch goal:
        - Sort the movies by the numbers of ratings

    Strategy:
        - Map to (movieID , 1) key/value
        - Reduce with output of (rating_count, movieID)
        - Send this to a second reducer so we end up with things sorted by rating count!
    
    Gotchas:
        - How do we set up more than one MapReduce set?
        - How do we ensure the rating counts are sorted properly?
    """

    def steps(self):
        return [
            MRStep(mapper=self.get_movieID_value, reducer=self.count_movieIDs),
            MRStep(reducer=self.sort_movieIDs),      
        ]

    def get_movieID_value(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        value = 1
        yield movieID, value

    def count_movieIDs(self, movieID, values):
        count = str(sum(values)).zfill(5)
        yield count, movieID

    def sort_movieIDs(self, count, movies):
        for movie in movies:
            yield movie, count


if __name__ == '__main__':
    MovieBreakdown.run()
