from datetime import date, timedelta
from todolist.models import Day

def bulk_insert_dates(start_date, end_date):
    """
    start_date から end_date までの全日付を MyDate テーブルに一括登録する
    """
    bulk_list = []
    current_date = start_date
    while current_date <= end_date:
        bulk_list.append(Day(day=current_date))
        current_date += timedelta(days=1)

    Day.objects.bulk_create(bulk_list)

bulk_insert_dates(date(2026, 1, 1), date(2030, 12, 31))