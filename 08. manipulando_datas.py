from datetime import datetime, timedelta

# data

hoje = datetime.now()
print(hoje.date())

amanha = hoje + timedelta(days=1)
print(amanha.date())

data_evento = datetime(year=2023, month=9, day=1)
atraso = hoje - data_evento
print(atraso.days)

# extraindo datas em outros formatos

data_stringtodate = "01/09/2023"
data_stringtodate = datetime.strptime(data_stringtodate, "%d/%m/%Y")
print(data_stringtodate.date())

# extraindo horários em outros formatos

time_stringtotime = "1510"
object_stringtotime = datetime.strptime(time_stringtotime, "%H%M")
print(object_stringtotime.time())

# formato brasileiro

print(hoje.strftime("%d/%m/%y"))
print(hoje.strftime("%A"))

# fuso horário

hoje = hoje - timedelta(hours=1)
print(hoje)

import zoneinfo

## print(zoneinfo.available_timezones())
zona = zoneinfo.ZoneInfo("Europe/London")
agora_london = hoje.astimezone(zona)
print(agora_london)



