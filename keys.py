from pynput import keyboard

def on_press(key):
    try: k = key.char # single-char keys
    except: k = key.name # other keys
    if key == keyboard.Key.esc: return False # stop listener
    if k in ['space', 'left', 'right', 'up']: # keys interested
        # self.keys.append(k) # store it in global-like variable
        print('Key pressed: ' + k)

lis = keyboard.Listener(on_press=on_press)
lis.start() # start to listen on a separate thread
lis.join() # no this if main thread is polling self.keys
