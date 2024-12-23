import parmed as pmd

amber = pmd.load_file('6kya_ref.prmtop', 'ref-equil-NPT.crd')

amber.save('6kya.top')

amber.save('6kya.gro')
