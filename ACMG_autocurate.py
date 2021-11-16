import sys
from cravat import BaseAnnotator
from cravat import InvalidData
import sqlite3
import os


class CravatAnnotator(BaseAnnotator):

    def setup(self):
        """
        Set up data sources.
        Cravat will automatically make a connection to
        data/example_annotator.sqlite using the sqlite3 python module. The
        sqlite3.Connection object is stored as self.dbconn, and the
        sqlite3.Cursor object is stored as self.cursor.
        """
        pass

    def annotate(self, input_data, secondary_data=None):
        chrom = input_data['chrom']
        pos = input_data['pos']
        ref_base = input_data['ref_base']
        alt_base = input_data['alt_base']
        so = input_data['so']
        is_clinvar = 1
        is_gnomad = 1
        is_spliceai = 1

        # getting appropriate values from input data sources
        gnomad_arr = secondary_data['gnomad']
        if len(gnomad_arr) == 0:
            is_gnomad = 0
        else:
            gnomad_arr = secondary_data['gnomad']
            gnomad_dict = gnomad_arr[0]
            global_af = gnomad_dict['af']

        clinvar_arr = secondary_data['clinvar']
        if len(clinvar_arr) == 0:
            is_clinvar = 0
        else:
            clinvar_arr = secondary_data['clinvar']
            clinvar_dict = clinvar_arr[0]
            clinvar_sig = clinvar_dict['sig']

        splice_arr = secondary_data['spliceai']
        if len(splice_arr) == 0:
            is_spliceai = 0
        else:
            splice_arr = secondary_data['spliceai']
            splice_dict = splice_arr[0]
            ds_ag = splice_dict['ds_ag']
            ds_al = splice_dict['ds_al']
            ds_dg = splice_dict['ds_dg']
            ds_dl = splice_dict['ds_dl']

        # default values for classification and reasoning
        classification = "VUS"
        reason = "Lack of Evidence"
        if is_clinvar ==  1:
            if clinvar_sig == "Benign" or clinvar_sig == "Likely benign":
                classification = "Benign"
                reason = "ClinVar Benign BS3"
            elif clinvar_sig == "Pathogenic" or clinvar_sig == "Likely pathogenic":
                classification = "Pathogenic"
                reason = "ClinVar Pathogenic PS1"
        elif is_gnomad == 1:
            if global_af > .05:
                classification = "Benign"
                reason = "gnomAD BA1/BS1"
        elif is_spliceai == 1:
            if so == 'SYN' and (ds_ag < .5 and ds_al < .5 and ds_dg < .5 and ds_dl < .5):
                classification = "Benign"
                reason = "Splice BP7"
        elif so == 'FSD' or so == 'FSI' or so == 'INI' or so == 'IND' or so == 'STR' or so == 'STL' or so == 'STG' or so == 'SPL':
            classification = "Pathogenic"
            reason = "LOF PVS1"
        return {
            'classification': classification,
            'reason': reason
        }


if __name__ == '__main__':
    annotator = CravatAnnotator(sys.argv)
    annotator.run()
