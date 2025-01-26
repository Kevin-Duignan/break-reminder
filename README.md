# Break Reminder: Installation and Usage Guide

This guide will help you set up and run the **Break Reminder** script on your system.

---

## Prerequisites

1. **Python**: Make sure Python 3.7 or later is installed on your system.
   - Check your Python version:
     ```bash
     python3 --version
     ```
   - If not installed, download it from [python.org](https://www.python.org/).

2. **pip**: Ensure you have `pip`, Python’s package manager, installed.
   - Check if `pip` is installed:
     ```bash
     python3 -m pip --version
     ```
   - Install it if needed:
     ```bash
     sudo apt install python3-pip  # Linux
     brew install pip              # macOS
     ```

---

## Installation Steps

1. **Clone or download the script**:
   - Clone the repository using Git:
     ```bash
     git clone https://github.com/Kevin-Duignan/break-reminder.git
     cd break_reminder
     ```
   - Or, download the script directly and navigate to its folder.

2. **Install dependencies**:
   The script uses the `notifypy` library for notifications and the `schedule` library for scheduling tasks. Install both using the following command:
   ```bash
   pip install notify-py schedule

3. **Place the audio file (optional)**:
   - Ensure the `water.wav` file is in the same directory as the script.
   - If the file is missing, the script will still work, but the notifications will not have sound.

---

## Running the Script

1. Open a terminal and navigate to the folder containing the script:
   ```bash
   cd /path/to/script

2. Run the script:
  ```bash
  nohup python3 break_reminder.py &
  
  This will log all outputs into the `nohup.out` file.

## Features
  - **Eye Break Reminder**: Notifies you every 20 minutes to look away from the screen for 20 seconds.
  - **Water Refill Reminder**: Reminds you at the top of every hour to refill your glass of water.
  - **Smart Scheduling**: The reminders only run:
    - On weekdays (Monday to Friday).
    - During working hours (7:00 AM to 6:00 PM).

## Customisation
  - **Change Work Hours**:
  Edit this line in the script:
  ```python3
  if datetime.now().weekday() <= 4 and 7 <= datetime.now().hour < 18:
  Adjust 7 and 18 to your desired start and end hours.
  - **Adjust Frequencies**:
  Modify the scheduling logic in the `schedule_reminders()` function:
  ```
  schedule.every(20).minutes.do(BreakReminder.remind_to_look_away)
  schedule.every().hour.at(":00").do(BreakReminder.remind_to_refill_water)
  ```
  - **Change Notification Audio**:
  Replace `./water.wav` and `blink.wav` with the path to your desired audio file:
  ```python3
  notification.audio = "/path/to/your_audio_file.wav"
