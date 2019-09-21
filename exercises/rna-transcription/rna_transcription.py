from string import maketrans


def to_rna(dna_strand):
    table = maketrans("GCTA", "CGAU")
    return dna_strand.translate(table)
