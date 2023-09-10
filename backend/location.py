class Location:

    def __init__(self, rating, description):
        self.rating = rating
        self.description = description
    
    @property
    def GetRating(self):
        return self.rating
    
    @property
    def GetDescription(self):
        return self.description