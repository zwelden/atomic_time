from lxml import html
import requests


class AtomicTime:
    """ class for getting and manipulating Atomic Time sourced from
        https://www.timeanddate.com/time/international-atomic-time.html
        this class handles both UTC (Coordinated Universal Time)
        and TIA (International Atomic Time) time
        use subclasses UTC() and TIA() to directly work with those times types
    """

    def __init__(self):
        self.update_time()

    def __str__(self):
            return("TIA: {0:02d}:{1:02d}:{2:02d} -- UTC: {3:02d}:{4:02d}:{5:02d}".format(
                            self.tia_hours, self.tia_minutes, self.tia_seconds,
                            self.utc_hours, self.utc_minutes, self.utc_seconds))

    def update_time(self):
        self.time_and_date_atomic = requests.get("https://www.timeanddate.com/time/international-atomic-time.html")
        self.atomic_page_tree = html.fromstring(self.time_and_date_atomic.content)

        # set TIA time
        self.tia_hours_and_mins = self.atomic_page_tree.xpath('//span[@id="hourmin0"]/text()')[0]
        self.tia_hours = int(self.tia_hours_and_mins[:2])
        self.tia_minutes = int(self.tia_hours_and_mins[3:])
        self.tia_seconds = int(self.atomic_page_tree.xpath('//span[@id="sec0"]/text()')[0])

        # set UTC time
        self.utc_hours_and_mins = self.atomic_page_tree.xpath('//span[@id="hourmin1"]/text()')[0]
        self.utc_hours = int(self.utc_hours_and_mins[:2])
        self.utc_minutes = int(self.utc_hours_and_mins[3:])
        self.utc_seconds = int(self.atomic_page_tree.xpath('//span[@id="sec1"]/text()')[0])

    def get_tia_hours(self):
        return self.tia_hours

    def get_tia_minutes(self):
        return self.tia_minutes

    def get_tia_seconds(self):
        return self.tia_seconds

    def get_utc_hours(self):
        return self.utc_hours

    def get_utc_minutes(self):
        return self.utc_minutes

    def get_utc_seconds(self):
        return self.utc_seconds

class TIA(AtomicTime):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return("{0:02d}:{1:02d}:{2:02d}".format(self.tia_hours, self.tia_minutes, self.tia_seconds))

    def get_hours(self):
        return self.get_tia_hours()

    def get_minutes(self):
        return self.get_tia_minutes()

    def get_seconds(self):
        return self.get_tia_seconds()


class UTC(AtomicTime):

    def init(self):
        super().__init__()

    def __str__(self):
        return("{0:02d}:{1:02d}:{2:02d}".format(self.utc_hours, self.utc_minutes, self.utc_seconds))

    def get_hours(self):
        return self.get_utc_hours()

    def get_minutes(self):
        return self.get_utc_minutes()

    def get_seconds(self):
        return self.get_utc_seconds()
