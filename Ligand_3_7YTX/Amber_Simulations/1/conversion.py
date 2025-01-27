import parmed as pmd

amber = pmd.load_file('7tyx_ref.prmtop', 'ref-equil-NPT.crd')

amber.save('7tyx_1.top')

amber.save('7tyx_1.gro')
