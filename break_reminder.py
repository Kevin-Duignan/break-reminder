from notifypy import Notify
import schedule
import time
from datetime import datetime


class BreakReminder:
    @staticmethod
    def remind_to_refill_water():
        """Send a reminder to refil water."""
        notification = Notify()
        notification.application_name = "Hydration Reminder"
        notification.title = "Give Yourself a Water Break!"
        notification.message = "Time to get up and grab some fresh water"
        notification.audio = "./water.wav"
        notification.send()

        print("Reminder: Time to refill  water!")

    @staticmethod
    def remind_to_look_away():
        """Send a reminder to look away from the screen."""
        notification = Notify()
        notification.application_name = "Eye Care Reminder"
        notification.title = "Give Your Eyes a Break!"
        notification.message = "Look away from the screen for 20 seconds to rest your eyes"
        notification.audio = "./blink.wav"
        notification.send()

        print("Reminder: Time to give your eyes a break!")

def schedule_reminders():
    """Schedule reminders every 20 minutes and hourly between 7:00 and 18:00."""
    # Schedule reminders every 20 minutes during working hours (7:00 to 18:00)
    schedule.every(20).minutes.do(BreakReminder.remind_to_look_away)

    # Schedule the hourly reminder to refill water at the top of each hour from 7:00 to 18:00
    schedule.every().hour.at(":00").do(BreakReminder.remind_to_refill_water)

    # Run the scheduler and check the time every second
    while True:
        # Check if it's a weekday (Mon-Fri) and during work hours (7:00 to 18:00)
        if datetime.now().weekday() <= 4 and 7 <= datetime.now().hour < 18: # 0 = Monday, 4 = Friday
            schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_reminders()
