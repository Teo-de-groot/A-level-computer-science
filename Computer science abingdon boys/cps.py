from pynput import mouse

log_file = "click_count.txt"

try:
    with open(log_file, "r") as f:
        content = f.read().strip()
        click_count = int(content)
except:
    click_count = 0

def on_click(x, y, button, pressed):
    global click_count

    if pressed:
        click_count += 1
        print(f"Clicks: {click_count}")

        with open(log_file, "w") as f:
            f.write(str(click_count))

with mouse.Listener(on_click=on_click) as listener:
    print(f"Starting click count: {click_count}")
    print("Click anywhere... press Ctrl+C to stop.")
    listener.join()