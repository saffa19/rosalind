def rna2aa():
    '''A mapping of RNA codons to the amino acid they translate to.
    
    returns: dict of RNA codon : amino acid pairs
    
    example: {'AGU':'S'}
    '''
    codonsTable = '''UUU F      CUU L      AUU I      GUU V
        UUC F      CUC L      AUC I      GUC V
        UUA L      CUA L      AUA I      GUA V
        UUG L      CUG L      AUG M      GUG V
        UCU S      CCU P      ACU T      GCU A
        UCC S      CCC P      ACC T      GCC A
        UCA S      CCA P      ACA T      GCA A
        UCG S      CCG P      ACG T      GCG A
        UAU Y      CAU H      AAU N      GAU D
        UAC Y      CAC H      AAC N      GAC D
        UAA Stop   CAA Q      AAA K      GAA E
        UAG Stop   CAG Q      AAG K      GAG E
        UGU C      CGU R      AGU S      GGU G
        UGC C      CGC R      AGC S      GGC G
        UGA Stop   CGA R      AGA R      GGA G
        UGG W      CGG R      AGG R      GGG G'''
    codonsList = codonsTable.split()
    i = iter(codonsList)
    ret = dict(zip(i,i))
    return ret