import time
import datetime
import os
import pyautogui

# Main folder for all screenshots
main_folder = "Screenshots"

def take_screenshots_with_timestamp(interval):
    screenshot_count = 0  # Initialize the count of screenshots
    try:
        while True:
            # Current time for folder and file naming
            now = datetime.datetime.now()
            date_str = now.strftime("%Y-%m-%d")  # Folder name
            time_str = now.strftime("%H-%M-%S-%f")  # File name
            
            # Create a folder for today's date if it doesn't exist
            daily_folder = os.path.join(main_folder, date_str)
            if not os.path.exists(daily_folder):
                os.makedirs(daily_folder)
                
            # Define the filename with the current timestamp and a descriptive prefix
            filename = f'Screen_{time_str}.png'
            filepath = os.path.join(daily_folder, filename)
            
            # Take and save the screenshot with pyautogui
            screenshot = pyautogui.screenshot()
            screenshot.save(filepath)
            screenshot_count += 1  # Increment the screenshot count
            
            # Check if there are 100 screenshots and delete the 50 oldest if true
            if screenshot_count == 100:
                all_files = sorted(os.listdir(daily_folder))  # Get all files and sort them
                oldest_files = all_files[:50]  # Select the 50 oldest files
                for file in oldest_files:
                    os.remove(os.path.join(daily_folder, file))  # Delete the file
                screenshot_count -= 50  # Update the count after deleting

            time.sleep(interval)  # Wait for specified interval before taking next screenshot
    except KeyboardInterrupt:
        print("Stopped taking screenshots.")

# Ensure the main folder exists
if not os.path.exists(main_folder):
    os.makedirs(main_folder)

# Set the interval for 3 seconds
interval_seconds = 2

# Start taking screenshots every 3 seconds and saving them with current date and time in the filename
take_screenshots_with_timestamp(interval_seconds)
