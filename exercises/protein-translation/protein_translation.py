protein_dict = {
    'AUG': 'Methionine',
    "UUU": 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP'
}


def identify(codon):
    return protein_dict.get(codon, None)


def proteins(strand):
    proteins_list = []
    codon_queue = []
    for i in strand:
        codon_queue.append(i)
        if len(codon_queue) > 3:
            codon_queue.pop(0)
        if len(codon_queue) == 3:
            protein = identify(''.join(codon_queue))
            if protein and protein != 'STOP':
                proteins_list.append(protein)
                codon_queue.clear()
            else:
                break
    return proteins_list
