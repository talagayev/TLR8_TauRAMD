import parmed as pmd

amber = pmd.load_file('3w3l_ref.prmtop', 'ref-equil-NPT.crd')

amber.save('3w3l_3.top')

amber.save('3w3l_3.gro')
