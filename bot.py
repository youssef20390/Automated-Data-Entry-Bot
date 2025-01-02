
from pathlib import Path
from botcity.core import  BotMaestroSDK
from botcity.maestro import *
from botcity.plugins.http import BotHttpPlugin
import  pyautogui, time, os



# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

API_URL = "https://jsonplaceholder.typicode.com/posts"
SAVE_DIR = Path.home() /  "Desktop" / "tjm-project"




def open_notepad():
    try:
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('notepad')
        pyautogui.press('enter')
    except Exception as e:
        print(f"Error while openning notepad {e}")




def fetch_posts():
    try:
        url = API_URL
        http = BotHttpPlugin(url)
        return http.get().json()
    except Exception as e:
        print(f"Error fetching data from API: {e}")
        return []



def main():

    try:
      os.mkdir(SAVE_DIR)
      print("Directory created seccessfuly")
    except FileExistsError as e :
      print("Directory already exist")

    
    # Open noteopad
    open_notepad()
    time.sleep(0.5)

    # Fetch posts
    posts = fetch_posts()[:10]
    if not posts:
        print("No posts to process.")
        return

    # Write each post to Notepad
    for post in posts:
        print(f"Processing post {post['id']}...")
        try:

            # Title and body
            title = post['title'] + "\n\n"
            body = post['body']
            
            # Open new tab 
            pyautogui.hotkey('ctrl', 'n')
            time.sleep(0.5)
            
            # File name and path
            file_name = f"post {post['id']}.txt"
            file_path = os.path.join(SAVE_DIR, file_name)



            # Using pyautogui to write body and tiile in notepad
            pyautogui.write(title, 0.01)
            pyautogui.write(body, 0.01)
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 's')
            time.sleep(0.5)


            # Simulate copy and paste in Notepad (Another way to write into notepad) 
            # Text = title + body
            # bot.copy_to_clipboard(Text)
            # pyautogui.hotkey('ctrl', 'v')
            # pyautogui.hotkey('ctrl', 's')
            # time.sleep(1)
            


            # Type the full path of the file and save
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(0.5)

            # Close Tab
            pyautogui.hotkey('ctrl', 'f4')
            
        except Exception as e:
            print(f"Error automating Notepad: {e}")
        
    pyautogui.hotkey('alt', 'f4')



def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()