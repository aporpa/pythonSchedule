day = float(raw_input("Enter current day: "))
month = float(raw_input("Enter current month: "))
daysRemain = 0
timeRemain = 0


def daysPercentage(day, month):
    if month == 8:
        daysRemain = 32 + (31 - day)
    elif month == 9:
        daysRemain = 32 - day
    elif month == 10:
        daysRemain = 2 - day
    else:
        return "Put current date"

    timeRemain = daysRemain / 63.0 * 100
    return timeRemain

time = daysPercentage(day, month)
print time

progress = float(raw_input("Your progress: "))
goalPercent = 100.0


def progressPercentage(progress):
    return goalPercent - progress

percent = progressPercentage(progress)
print percent


def schedule(time, percent):
    if time > percent:
        return "You're fine"
    else:
        return "You're out of time"

timeVsProgress = schedule(time, percent)
print timeVsProgress
