import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The kitchen light is still on, low and amber, and the house has gone quiet in the way it does after everyone has gone to bed.",
        "Outside, the street is empty, and a cat moves along the fence in no hurry at all.",
        "The kettle ticks as it cools.",
        "Somewhere down the road a dog sighs in its sleep and settles again.",
        "The laundry on the line sways a little, smelling faintly of soap and night air.",
        "Nothing is asking anything of you now.",
        "The day has folded itself away like a letter put back in its envelope.",
        "The hours ahead are just soft dark and the slow turning of the ceiling fan, and the small warm weight of being exactly where you are.",
    ]
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Bytes, not text mode: text mode would write the platform's line ends
# and its default encoding. Two runs write the same bytes.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
