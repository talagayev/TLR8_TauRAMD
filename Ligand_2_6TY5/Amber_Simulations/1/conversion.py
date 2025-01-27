import parmed as pmd

amber = pmd.load_file('6ty5_ref.prmtop', 'ref-equil-NPT.crd')

amber.save('6ty5_1.top')

amber.save('6ty5_1.gro')
