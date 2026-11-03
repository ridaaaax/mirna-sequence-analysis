species=["hsa","mml","mmu"]

for name in species:
    input_file=f"analysis/{name}-pre.fas"
    output_file=f"analysis/{name}-pre-dna.fasta"

    sequences=""

    with open(input_file,"r") as infile:
        with open(output_file,"w")as outfile:

            for line in infile:
                sequence=line.strip().upper()

                if sequence and not line.startswith(">"):
                    sequences=sequences+sequence

                if line.startswith(">"):
                    outfile.write(line)

                else:
                    dna_sequence=line.upper().replace("U","T")
                    outfile.write(dna_sequence)

    print(f"{name} U nucleotides:",sequences.count("U"))
    print(f"{name} T nucleotides:", sequences.count("T"))
    print(f"Created: {output_file}")