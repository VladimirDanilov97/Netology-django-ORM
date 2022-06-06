from datetime import datetime

class PubDateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        return datetime.date(datetime.strptime(value, '%Y-%m-%d'))

    def to_url(self, value):
        return datetime.strftime(value, '%Y-%m-%d')