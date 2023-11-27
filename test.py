def find_upstream(dna_sequence):
    idx = dna_sequence.find("ATG")
    return dna_sequence[0:idx]

def find_gene(dna_sequence):
    idx = dna_sequence.find("ATG")
    return dna_sequence[idx:]

def second_codon(gene_sequence):
    idx = gene_sequence.find("ATG")
    return gene_sequence[idx + 3: idx + 6]

def third_codon(gene_sequence):
    idx = gene_sequence.find("ATG")
    return gene_sequence[idx + 6: idx + 9]

def complementary_nucleotide(nucleotide):
    # match nucleotide:
    #     case 'A':
    #         return 'T'
    #     case 'T':
    #         return 'A'
    #     case 'G':
    #         return 'C'
    #     case 'C':
    #         return 'G'
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'G':
        return 'C'
    elif nucleotide == 'C':
        return 'G'

def complemantary_sequence(dna_sequence):
    s = ""
    for i in dna_sequence:
        s += complementary_nucleotide(i)
    return s

if __name__ == "__main__":
    dna_sequence = input("Please enter a DNA genetic sequence: ")
    #dna_sequence = "CGCCATATAATGCTCGTCCGCGCCCTA"
    print(f"\n\nOriginal sequence: {dna_sequence}")

    gene_sequence = find_gene(dna_sequence)
    firstIdx = dna_sequence.find(gene_sequence) + 1
    print(f"\nATG codon at bp {firstIdx}")
    second = second_codon(gene_sequence)
    secondIdx = dna_sequence.find(second) + 1
    print(f"    followed by {second} at bp {secondIdx}")
    third = third_codon(gene_sequence)
    thirdIdx = dna_sequence.find(third) + 1
    print(f"    followed by {third} at bp {thirdIdx}")

    print()
    
    upstream = find_upstream(dna_sequence)
    print(f"Upstream sequence: {upstream}")
    print(f"Upstream length:   {len(upstream)} bp")

    print()

    print(f"Gene sequence: {gene_sequence}")
    print(f"Gene length:   {len(gene_sequence)} bp")
    
    print(f"[+ Strand]: {gene_sequence}")
    print(f"            {'|' * len(gene_sequence)}")
    print(f"[- Strand]: {complemantary_sequence(gene_sequence)}")