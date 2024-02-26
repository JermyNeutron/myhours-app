# time in ISO 8601 format

from datetime import datetime, timezone

current_time_utc = datetime.now(timezone.utc)
current_time_local = current_time_utc.astimezone()

current_time_iso8601 = current_time_local.isoformat()

print(current_time_iso8601)
