# Run after opening your Browser and logging into Metamask !!!

# If you are using Windows Power Toys + Multiple browsers just run the script
# Otherwise, run the following command in Windows Powershell (Without #):
# Start-Process -NoNewWindow python get_pos.py

from pynput import mouse


browsers = 1 #Enter the number of accounts/browsers here
browser = 1 #Just a counter. Keep the value 1!

name_list = [1,  2, 3]
lines = []
count = 0

print('Running...')

def on_click(x, y, button, pressed):
    global browsers
    global browser
    global count

    if button == mouse.Button.left and pressed:
        lines.append('{}'.format((x, y)))
        print('[Browser {}] {} at {}'.format(browser, name_list[count], (x, y)))
        count += 1
        
    if count == len(name_list):
        browser += 1
        count = 0

    if browser > browsers:
        with open('config.txt', 'w') as f:
            f.write('\n'.join(lines))

        print('Finished!')
        return False

listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()