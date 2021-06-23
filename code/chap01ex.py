from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
'''
Exercise 1.2 In the repository you downloaded, you should find a file namedchap01ex.py; using this file as a starting place, write a function that reads the respondent file, 2002FemResp.dat.gz. The variable pregnum is  a  recode  that  indicates  how  many  times  each  re-spondent  has  been  pregnant.   
Print  the  value  counts  for  this  variable  and compare them to the published results in the NSFG codebook.You can also cross-validate the respondent and pregnancy files by comparing pregnum for each respondent with the number of records in the pregnancy file.
You can use nsfg.MakePregMap to make a dictionary that maps from each caseid to a list of indices into the pregnancy DataFrame. A solution to this exercise is inchap01soln.py
'''


def ReadFemPreg(dct_file='C:\Users\wschlin\Documents\GitHub\ThinkStats2\code\\2002FemResp.dct',dat_file='C:\Users\wschlin\Documents\GitHub\ThinkStats2\code\\2002FemResp.dat.gz'):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    CleanFemResp(df)
    return df

def CleanFemResp(df):
    # what goes here? birthweight isn't a field in resp
    # is this where pregnum goes??? 
    df.agepreg /= 100.0
    na_vals = [97, 98, 99]
    df.birthwgt_lb.replace(na_vals, np.nan, inplace=True)
    df.birthwgt_oz.replace(na_vals, np.nan, inplace=True)
    df['totalwgt_lb'] = df.birthwgt_lb + df.birthwgt_oz / 16.0

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    resp = nsfg.ReadFemResp()
    resp.head()

    print(resp.pregnum.valuecounts())
    respmap = nsfg.MakePregMap(resp)
    # or are we supposed to do our own MakePregMap since this is supposed to be the equivalent of nsfg?

    print('%s: All tests passed.' % script)
    # having the only output it comes with be 'All tests passed' is so frustrating. I could run the empty example problem and it would say "All tests passed".


if __name__ == '__main__':
    main(*sys.argv)
