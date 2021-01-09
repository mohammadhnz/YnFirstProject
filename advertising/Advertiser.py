from advertising.BaseAdvertising import BaseAdvertising as BaseAdvertising


class Advertiser(BaseAdvertising):
    __all_advertisers = []

    def __init__(self, id, name):
        super(Advertiser, self).__init__(id)
        self.__name = name
        Advertiser.__all_advertisers.append(self)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @staticmethod
    def help():
        return "id: each advertiser has its own Id" \
               "\nname: name of advertiser\nclicks: count of clicks\nviews: count of views"

    def describe_me(self):
        return "this is advertiser class"

    @staticmethod
    def get_total_clicks():
        clicks = 0
        for advertiser in Advertiser.__all_advertisers:
            clicks += advertiser.get_clicks()
        return clicks