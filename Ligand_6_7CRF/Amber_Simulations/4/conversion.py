import parmed as pmd

amber = pmd.load_file('7crf_ref.prmtop', 'ref-equil-NPT.crd')

amber.save('7crf.top')

amber.save('7crf.gro')
