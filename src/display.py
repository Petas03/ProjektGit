import time

class LCDDisplay:
    def __init__(self):
        # Initialize LCD display here
        pass

    def display_text(self, text):
        # Display the given text on the LCD
        pass

    def clear_display(self):
        # Clear the LCD display
        pass

    def show_time(self):
        while True:
            current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
            self.display_text(current_time)
            time.sleep(1)  # Update every second

# Example of using the LCDDisplay
if __name__ == '__main__':
    lcd = LCDDisplay()
    lcd.show_time()