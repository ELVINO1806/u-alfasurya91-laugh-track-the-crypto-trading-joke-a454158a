import os

os.makedirs("/output", exist_ok=True)
# Joke: stop-loss yang gagal diejek jadi investasi jangka panjang.
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write("I set a stop-loss, a take-profit, and an alarm for 3 a.m. The alarm went off, the stop-loss didn't, and my portfolio now identifies as a long-term investment.")
