from mrjob.job import MRJob
from mrjob.step import MRStep


class MovieBreakdownEasy(MRJob):
    """
    Easy challenge exercise:
        - All you need is to change one thing in the mapper,
        we don't actually care about ratings now, we care about
        movieID's
        - Start with this and make sure you can do it
        - You can use nano to just edit the existing RatingsBreakdown.py script
    """

    def steps(self):
        return [
            MRStep(mapper=self.get_movie_id,
                   reducer=self.count_movie_id)
        ]

    def get_movie_id(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield movieID, 1

    def count_movie_id(self, movieID, values):
        yield movieID, sum(values)

if __name__ == '__main__':
    MovieBreakdownEasy.run()
