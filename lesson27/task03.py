class Stadium:
    def __init__(self, name=None, year=None, country=None, city=None, volume=None):
        self.__name = name
        self.__year = year
        self.__country = country
        self.__city = city
        self.__volume = volume

    def set_name(self, v):
        self.__name = v

    def set_year(self, v):
        self.__year = v

    def set_country(self, v):
        self.__country = v

    def set_city(self, v):
        self.__city = v

    def set_volume(self, v):
        self.__volume = v

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def get_country(self):
        return self.__country

    def get_city(self):
        return self.__city

    def get_volume(self):
        return self.__volume
