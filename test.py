def find_upstream(dna_sequence):
    idx = dna_sequence.find("ATG")
    return dna_sequence[0:idx]

def find_gene(dna_sequence):
    idx = dna_sequence.find("ATG")
    return dna_sequence[idx:]

def second_codon(gene_sequence):
    idx = gene_sequence.find("ATG")
    return gene_sequence[idx + 3, idx + 6]

def third_codon(gene_sequence):
    idx = gene_sequence.find("ATG")
    return gene_sequence[idx + 6, idx + 9]

def complementary_nucleotide(nucleotide):
    match nucleotide:
        case 'A':
            return 'T'
        case 'T':
            return 'A'
        case 'G':
            return 'C'
        case 'C':
            return 'G'

def complemantary_sequence(dna_sequence):
    s = ""
    for i in dna_sequence:
        s += complementary_nucleotide(i)

if __name__ == "__main__":
    s = input("Please enter a DNA genetic sequence: ")
    print(f"\nOriginal sequence: {s}")

    print(f"\nATG codon at bp 10")
    print(f"\tfollowed by {second_codon}")