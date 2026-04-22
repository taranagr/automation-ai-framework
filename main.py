# This is a sample Python script.
import os

from common_library.healenium_setup import healenium_setup
from common_library.selenium_functions import open_browser


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')
    # Press Ctrl+F8 to toggle the breakpoint.
    os.environ["HEALENIUM_FLAG"] = "YES"
    healenium_setup()
    driver = open_browser()
    driver.get("https://www.google.com")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
