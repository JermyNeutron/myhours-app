import datetime
import pytz


def main():
    current_time_utc = datetime.datetime.now(datetime.timezone.utc)
    pst = pytz.timezone('America/Los_Angeles')
    current_time_pst = current_time_utc.astimezone(pst)
    current_time_iso = current_time_pst.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'
    current_date = current_time_iso[:10]
    return current_date, current_time_iso

if __name__ == '__main__':
    main()