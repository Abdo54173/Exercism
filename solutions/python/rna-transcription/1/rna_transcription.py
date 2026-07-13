def to_rna(dna_strand):

    dna_to_rna ={
        "G":"C",
        "C":"G",
        "T":"A",
        "A":"U",
    }

    rna_sequence =""

    for i in dna_strand:
        if i in dna_to_rna:
            rna_sequence += dna_to_rna[i]
        else:
            print(f"Invalid nucleotide: {nucleotide}")
            
    return rna_sequence
