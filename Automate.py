import pyautogui
import time

def connect_to_remote_desktop(remote_ip, username="", password=""):
    try:
        # Open Windows Remote Desktop
        pyautogui.hotkey('win', 'r')
        pyautogui.write('mstsc')
        pyautogui.press('enter')
        time.sleep(2)  # Wait for the Remote Desktop window to open

        # Enter the remote desktop connection details
        pyautogui.write(remote_ip)
        pyautogui.press('enter')
        time.sleep(2)

        # Fill in the username and password (assuming credentials are needed)
        if username:
            pyautogui.write(username)
            pyautogui.press('tab')
            if password:
                pyautogui.write(password)
                pyautogui.press('enter')

        # Save the connected IP address to the "welcome" file
        with open('welcome.txt', 'a') as welcome_file:
            welcome_file.write(remote_ip + '\n')

    except Exception as e:
        print(f"An error occurred while connecting to {remote_ip}: {str(e)}")

if __name__ == "__main__":
    file_path = "alive.txt"  # Path to the file containing IP addresses
    with open(file_path, "r") as file:
        ip_addresses = file.read().splitlines()

    for ip_address in ip_addresses:
        connect_to_remote_desktop(ip_address)
