from datetime import timedelta



def timer(data_time):
    formats = {
        'seconds': 'seconds',
        'minutes': 'minutes',
        'hours': 'hours',
        'days': 'days'
    }

    values = {}

    for list_ in data_time.split():
        key, value = list_.split('=')
        if key in formats:
            values[formats[key]] = int(value)
        else:
            raise ValueError

    return timedelta(**values)
