from python_framework import SchedulerType
from python_framework import Scheduler, SchedulerMethod, WeekDay, WeekDayConstant

from enumeration.UpdateMoment import UpdateMoment


@Scheduler()
class EmailScheduler :

    @SchedulerMethod(
        SchedulerType.CRON,
        week = WeekDayConstant.ALL_WEEK,
        weekDays = WeekDayConstant.WEEK_CHRON,
        hour = UpdateMoment.THE_NEWS.hour,
        minute = UpdateMoment.THE_NEWS.minute,
        toleranceTime = 10
    )
    # @SchedulerMethod(
    #     SchedulerType.INTERVAL,
    #     seconds = 10
    # )
    def updateTodaysNews(self):
        self.service.theNews.updateTodaysNews()