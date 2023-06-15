# It will give you notification for drinking water in every 1 hr.

import time
from plyer import notification

repeat_interval = 3600
while True:
    notification.notify(title = '--- Drink Water Boiii! ---',
                        message = '''Drink water stay hydrated.
Lose your weight.
Improve your skin complexion.
And Think, Focus and Concentrate better.''',
                        timeout = 10)
        
    time.sleep(repeat_interval)