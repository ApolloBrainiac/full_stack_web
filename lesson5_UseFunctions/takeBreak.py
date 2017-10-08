import time
import webbrowser

total_breaks = 3
i = 0

print("This program started on "+time.ctime())
while i < total_breaks:
    i += 1
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=rCAIY5n1hPA")
