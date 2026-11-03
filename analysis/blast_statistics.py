total_hits = 0
alignment_lengths = []

with open("analysis/human_vs_mouse.tsv", "r") as file:
    for line in file:
        columns = line.strip().split("\t")

        total_hits += 1
        alignment_lengths.append(int(columns[3]))

print("Total alignment hits:", total_hits)
print("Average hits per human miRNA:", total_hits / 514)
print("Average alignment length:", sum(alignment_lengths) / len(alignment_lengths))

short_hits = 0
long_hits = 0

for length in alignment_lengths:
    if length < 20:
        short_hits += 1
    else:
        long_hits += 1

print("Alignments shorter than 20 nt:", short_hits)
print("Alignments 20 nt or longer:", long_hits)

filtered_lengths = []

for length in alignment_lengths:
    if length >= 20:
        filtered_lengths.append(length)

print("Filtered alignment count:", len(filtered_lengths))
print("Filtered average alignment length:",
      sum(filtered_lengths) / len(filtered_lengths))



import matplotlib.pyplot as plt

plt.hist(alignment_lengths, bins=30)

plt.xlabel("Alignment length (nt)")
plt.ylabel("Number of alignments")
plt.title("Human vs Mouse pre-miRNA BLASTn alignment lengths")

plt.tight_layout()
plt.savefig("analysis/human_vs_mouse_alignment_lengths.png")
plt.show()


mouse_hits = 0
mouse_alignment_lengths = []

with open("analysis/mouse_vs_human.tsv", "r") as file:
    for line in file:
        columns = line.strip().split("\t")

        mouse_hits += 1
        mouse_alignment_lengths.append(int(columns[3]))

print("\nMouse → Human results")
print("Total alignment hits:", mouse_hits)
print("Average hits per mouse miRNA:", mouse_hits / 404)
print("Average alignment length:",
      sum(mouse_alignment_lengths) / len(mouse_alignment_lengths))

mouse_short_hits = 0
mouse_long_hits = 0

for length in mouse_alignment_lengths:
    if length < 20:
        mouse_short_hits += 1
    else:
        mouse_long_hits += 1

print("Mouse → Human alignments shorter than 20 nt:", mouse_short_hits)
print("Mouse → Human alignments 20 nt or longer:", mouse_long_hits)