
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

topics = {
    "Environment": {
        "title": "SAVE OUR PLANET",
        "points": [
            "Reduce plastic waste",
            "Plant more trees",
            "Save water and electricity",
            "Keep our surroundings clean"
        ],
        "action": "SMALL ACTIONS, BIG CHANGE!"
    },
    "Cyber Safety": {
        "title": "STOP CYBERBULLYING",
        "points": [
            "Be kind online",
            "Never share passwords",
            "Report online harassment",
            "Think before you post"
        ],
        "action": "MAKE THE INTERNET SAFER!"
    },
    "Education": {
        "title": "EDUCATION FOR ALL",
        "points": [
            "Every child deserves education",
            "Support equal opportunities",
            "Encourage girls' education",
            "Never stop learning"
        ],
        "action": "LEARN TODAY, LEAD TOMORROW!"
    }
}

def create_infographic(topic):
    data = topics[topic]

    fig, ax = plt.subplots(figsize=(8, 10))
    fig.patch.set_facecolor("#F0F7FF")
    ax.set_facecolor("#F0F7FF")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis("off")

    header = FancyBboxPatch(
        (0.5, 8.8), 9, 2.3,
        boxstyle="round,pad=0.2",
        facecolor="#174A7E"
    )
    ax.add_patch(header)

    ax.text(5, 10.25, "SOCIAL AWARENESS",
            ha="center", color="white",
            fontsize=16, fontweight="bold")

    ax.text(5, 9.55, data["title"],
            ha="center", va="center",
            color="white", fontsize=20,
            fontweight="bold")

    ax.text(1, 8.1, "KEY POINTS",
            fontsize=16, fontweight="bold",
            color="#174A7E")

    for i, point in enumerate(data["points"]):
        y = 7.2 - i * 1.25

        card = FancyBboxPatch(
            (0.8, y - 0.3), 8.4, 0.8,
            boxstyle="round,pad=0.12",
            facecolor="white", edgecolor="#B7D5EF"
        )
        ax.add_patch(card)

        ax.text(1.2, y + 0.1, f"{i+1}.",
                fontsize=14, color="#E87520",
                fontweight="bold", va="center")

        ax.text(1.8, y + 0.1, point,
                fontsize=12, color="#222222",
                va="center")

    footer = FancyBboxPatch(
        (0.8, 1.1), 8.4, 1,
        boxstyle="round,pad=0.15",
        facecolor="#E87520"
    )
    ax.add_patch(footer)

    ax.text(5, 1.6, data["action"],
            ha="center", va="center",
            fontsize=13, color="white",
            fontweight="bold")

    filename = topic.lower().replace(" ", "_") + "_infographic.png"
    plt.savefig(filename, dpi=200, bbox_inches="tight")
    plt.close()
    print("Created:", filename)

for topic in topics:
    create_infographic(topic)
      
