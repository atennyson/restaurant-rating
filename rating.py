import csv


class RestaurantRating:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def __repr__(self):
        return f"<RestaurantRating name={repr(self.name)} rating ={repr(self.rating)}>"

    def __lt__(self, other):
        return self.rating < other.rating

    def update_rating(self, rating):
        self.rating = rating


class RestaurantRatings:
    def __init__(self, ratings=None):
        self.ratings = ratings or []

    def __repr__(self):
        return f"<{repr(self.ratings)}>"

    def add_rating(self, name, rating):
        """create and add a new RestaurantRating."""

        # Create a new RestaurantRating instance
        r = RestaurantRating(name, rating)

        # Add it to the list of ratings
        self.ratings.append(r)

    def remove_rating_by_index(self, index):
        """Remove a rating by index."""

        self.ratings.pop(index)

    def remove_rating_by_name(self, name):
        """Remove a rating by name."""

        for index, rating in enumerate(self.ratings):
            if rating.name == name:
                self.remove_rating_by_index(index)

    def get_rating_by_name(self, name):
        for rating in self.ratings:
            if rating.name == name:
                return rating

    def to_file(self, filename):
        """Write ratings to filename."""

        # Open filename in write mode
        with open(filename, "w") as f:
            # Create a CSV writer
            writer = csv.writer(f)

            # Loop over ratings and write data to CSV
            for r in self.ratings:
                writer.writerow([r.name, r.rating])

    @classmethod
    def from_file(cls, filename):
        """Read ratings from filename"""

        r = RestaurantRatings()
        with open(filename) as f:
            reader = csv.reader(f)
            for row in reader:
                r.ratings.append(row)

            return r
