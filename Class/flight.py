class Flight:

    def __init__(self):
        self.start = "New Delhi"
        self.destination = "Lucknow"
        self.date = "anytime"

    def location_name(self, data_start, location):
        if location == "Delhi":
            location = "New Delhi"

        for i in data_start['Places']:
            if location == i['PlaceName']:
                return i['PlaceId']

    def yes_no(self, entry):
        if entry:
            return "Yes"
        else:
            return "No"
