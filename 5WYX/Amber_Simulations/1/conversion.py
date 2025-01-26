import parmed as pmd

amber = pmd.load_file('5wyx_ref.prmtop', 'ref-equil-NPT.crd')

amber.save('5wyx.top')

amber.save('5wyx.gro')
