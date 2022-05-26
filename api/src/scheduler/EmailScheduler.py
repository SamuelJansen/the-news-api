from python_framework import SchedulerType
from python_framework import Scheduler, SchedulerMethod, WeekDay, WeekDayConstant

from enumeration.UpdateMoment import UpdateMoment


@Scheduler()
class EmailScheduler :

    @SchedulerMethod(
        SchedulerType.CRON,
        week = WeekDayConstant.ALL_WEEK,
        weekDays = WeekDayConstant.WEEK_CHRON,
        hour = UpdateMoment.TODAY_NEWS.hour,
        minute = UpdateMoment.TODAY_NEWS.minute,
        toleranceTime = 30
    )
    def startTodaysNewsUpdate(self):
        self.service.theNews.startTodaysNewsUpdate()
