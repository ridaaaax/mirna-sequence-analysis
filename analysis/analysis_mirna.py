import matplotlib.pyplot as plt

# 1. Homo sapiens
# Read hsa-pre.fas
with open("analysis/hsa-pre.fas","r") as file:
    human_lengths=[]
    for line in file:
        sequence = line.strip()

        if sequence and not line.startswith(">"):
            length=len(sequence)
            human_lengths.append(length)

#Calculate lengths and average of homo sapien seq
human_average=sum(human_lengths)/len(human_lengths)
print("Total number of human pre-mirna sequences:",len(human_lengths))
print("Minimum length:",min(human_lengths))
print("Maximum length:",max(human_lengths))
print(f"Average pre-mirna length of human: {human_average:.2f}")
print("-"*40)

# 2.Macaca mulatta
# Read mml pre-fas
with open("analysis/mml-pre.fas","r") as file:
    macaque_lengths=[]
    for line in file:
        sequence=line.strip()
        if sequence and not line.startswith(">"):
            length=len(sequence)
            macaque_lengths.append(length)

# Calculate lengths and average of macaca mulatta seq
macaque_average=sum(macaque_lengths)/len(macaque_lengths)
print("Total number of macaque pre-mirna sequences:",len(macaque_lengths))
print("Minimum length:", min(macaque_lengths))
print("Maximum length:", max(macaque_lengths))
print(f"Average pre-mirna length of macaque:{macaque_average:.2f}")
print("-"*40)

# 3. Mus musculus
#Read mmu-pre.fas file
with open("analysis/mmu-pre.fas","r") as file:
    mouse_lengths=[]

    for line in file:
        sequences=line.strip()
        if sequences and not line.startswith(">"):
            length=len(sequences)
            mouse_lengths.append(length)

# Calculate lengths and average of mus musculus
mouse_average=sum(mouse_lengths)/len(mouse_lengths)
print("Total number of mouse pre-mirna sequences:",len(mouse_lengths))
print("Minimum length:",min(mouse_lengths))
print("Maximum length:", max(mouse_lengths))
print(f"Average pre-mirna length of mouse:{mouse_average:.2f}")


# 4. Boxplot comparing the three species

plt.boxplot([human_lengths, macaque_lengths, mouse_lengths])

plt.title("Pre-miRNA length distribution across three species")
plt.ylabel("Pre-miRNA length (nt)")
plt.xticks(
    [1, 2, 3],
    ["Homo sapiens", "Macaca mulatta", "Mus musculus"])


plt.tight_layout()
# save fig
plt.savefig("analysis/mirna_length_boxplot.png", dpi=300)
plt.show()
