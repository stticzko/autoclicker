AutoClicker README

Overview:
This AutoClicker script is designed to automate mouse clicks on your system. It allows you to set the click rate, toggle between different clicking modes, bind a key to start/stop clicking, and target specific windows for clicking. 

Instructions:

1. Installation:
   - Ensure you have Python installed on your system.
   - Install the required dependencies by running: 
     ```
     pip install pygetwindow keyboard mouse
     ```

2. Usage:
   - Run the script using Python: 
     ```
     python autoclicker.py
     ```
   - Once the script is running, it will start listening for the specified bind key (default is "r"). Pressing this key will toggle the autoclicker on/off.
   - While the script is running, you can adjust the settings by following the on-screen instructions.
   - To exit the script, choose option "5" from the menu.

3. Settings:
   - CPS (Clicks Per Second): Adjust the speed of clicking.
   - Mode: Choose between "toggle" (clicks on/off with each press) and "press" (clicks as long as the bind key is held).
   - Bind Key: Set the key that activates/deactivates the autoclicker.
   - Target Window: Specify a window title to restrict clicking to that particular window.


