'''
Author : Bhagya Hendalage
Date : 30/12/2020
Understand the Python Object-oriented programming (OOP) techniques.
Python methods to analyze DNA sequences

Input: DNA/mRNA/amino acid sequences in FASTA format
Output: Sequence class,DNAseq subclass,mRNAseq subclass,Proteinseq subclass
'''
#create a Sequence class
class Sequence:
    gene_ID=''
    gene_name=''
    seq_type=''
    seq_length=0
    seq_count=0
    sp_name=''
    subsp_name=''
    sequence=''
#define attributes and methods
    def __init__(self,gene_name,gene_ID,sp_name,subsp_name,sequence):
        self.gene_ID=gene_ID
        self.gene_name=gene_name
        self.sp_name=sp_name
        self.subsp_name=subsp_name
        self.sequence=sequence
        self.seq_type=Sequence.get_Seq_Type(sequence)
        self.seq_length=len(sequence)
        Sequence.seq_count += 1

    @staticmethod
    def fasta_Split(file_name):
        """
        method to split fasta file to dectionary
        For proteins:{'Gene_name':(['>Gene_name_P' ,'RefSeq_gene_ID','species','subspecies','Uniprot_ID','reviewed_status'],'sequence')}
        For coding sequences:{'Gene_name:(['>Gene_name','CDS-RefSeq_gene_ID','species','subspecies'],'sequence')}

        Input: fasta file_name
        Output: dictionary with keys and values
        """
        #define an empty dictionary
        dict = {}
        with open(file_name, 'r') as sequence:
            Gene_name = ''
            seq = ''
            for line in sequence:
                if line != '\n':
                    line = line.strip()
                    if '>' in line:
                        #to split from '-'
                        Gene_name = line.split('-')
                        #to take the first index value as gene_name
                        Gene_name = Gene_name[0]
                        header_parts = line.split('-')
                        #to take all indeces to value
                        header_parts = header_parts[0:]
                        #without seq='', all keys contain first iterated sequence
                        seq=''
                    if '>' not in line:
                        seq = seq + line
                        dict[Gene_name] = header_parts, seq
        return(dict)

    @staticmethod
    def get_Seq_Type(sequence):
        """
        A method to check the sequence type from all 3 sequence types: DNA, mRNA, amino acid.

        Input: sequence
        Output: sequence type ('DNA' or 'mRNA' or 'amino acid')
        """
        if 'M' in sequence:
            return "Amino acid"
        elif 'U' in sequence and 'M' not in sequence:
            return "mRNA"
        else:
            return "DNA"

    @staticmethod
    def get_Character_Count(sequence):
        """
        method for return all characters in sequence and its count as a dictionary
        Input: sequence
        Output: dictionary of character counts
        """
        character_count = {}

        for i in sequence:
            if i in character_count:
                character_count[i] += 1
            else:
                character_count[i] = 1

        # printing result
        return(character_count)
#subclass for DNA
class DNAseq(Sequence):
    AT_content=0
    Transcribed_sequence=''


    def __init__(self, gene_name, gene_ID,sp_name, subsp_name,sequence):
        super().__init__(gene_name, gene_ID, sp_name, subsp_name, sequence)

        self.AT_content = self.get_AT_Contents(sequence)
        self.Transcribed_sequence=self.transcribe_Sequence(sequence)



    def transcribe_Sequence(self,sequence):
        '''
        method for transcribe DNA sequence
        Input : sequence
        Output : mRNA
        '''
        transcribed_sequence=sequence.replace('T','U')
        return transcribed_sequence


    def get_AT_Contents(self,sequence):
        '''
        method for get A,T bases content in sequence as a percentage
        Input : sequence
        Output : AT content as percentage
        '''
        #store the output as instance variable
        AT_content = ((sequence.count("A") + sequence.count("T")) / len(sequence)) * 100
        return AT_content

#subclass for mRNA
class mRNAseq(Sequence):
    AT_content=0
    Amino_acid_codons=''
    Translated_sequence=''


    def __init__(self, gene_name, gene_ID,sp_name, subsp_name,sequence):
        super().__init__(gene_name, gene_ID, sp_name, subsp_name, sequence)

        self.mRNA_id = gene_ID
        self.mRNA_name = gene_name
        self.seq_type = "mRNA"
        self.seq_len = len(sequence)
        self.AT_content = self.get_ATcontent(sequence)
        self.Translated_sequence = self.translate_Sequence(sequence)


    def get_ATcontent(self,sequence):
        '''
         methode for get AT content in mRNA sequnce
         input : sequence
         output : AU content as a percentage
        '''
        AT_content = ((sequence.count("A") + sequence.count("U")) / len(sequence)) * 100
        return AT_content

    def upload_Codons(mRNAseq,CodonfileName):
        Codon_dict = {}
        # open codon_table and store as a variable
        with open('codon_table.txt', 'r') as codon_table:
            for line in codon_table:
                # remove header and empty lines
                if '#' not in line and line != '\n':
                    (codon, AminoAcid, Letter, FullName) = line.strip().split('\t')
                    # fill the dictionary using codons and related amino acid name
                    Codon_dict[codon] = Letter
        return(Codon_dict)

    def translate_Sequence(self, sequence, CodonfileName="OSDREB_sequences.fasta"):
        protein = ''
        Codon_map = self.upload_Codons(CodonfileName)
        #start when meet 'AUG'
        start = sequence.find('AUG')
        if start != -1:
            while start + 2 < len(sequence):
                codon = sequence[start:start + 3]
                #stop when meet stop codons
                if codon == "UAG" or codon == "UAA" or codon == "UGA":
                    break;
                start += 3
                for i in Codon_map[codon]:
                    protein += i
            return(protein)

#subclass for proteins
class Proteinseq(Sequence):
    Uniprot_ID=''
    Reviewed_status=''
    Hydrophobicity=0
    def __init__(self, gene_name, gene_ID, sp_name, subsp_name, sequence,uniprot_ID,reviewed):
        super().__init__(gene_name, gene_ID, sp_name, subsp_name, sequence)
        self.prot_name=gene_name
        self.prot_ID=gene_ID
        self.uniprot_ID=uniprot_ID
        self.reveiwed=reviewed
        self.Hydrophobicity=self.get_Hydrophobicity(sequence)

    def get_Hydrophobicity(self,sequence):
        '''
        method for find hydrophobicity using content of hydrophobic amino acids
        input : sequence
        output : percentage of hydrophobicity
        '''
        Hydrophobicity = ((sequence.count("A") + sequence.count("I") + sequence.count("L") + sequence.count(
            "M") + sequence.count("F") + sequence.count("W") + sequence.count("Y") + sequence.count("V")) / len(
            sequence)) * 100
        return(Hydrophobicity)
