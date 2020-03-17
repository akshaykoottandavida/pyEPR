# -*- coding: utf-8 -*-
"""
My First pyEPR Script
"""

import pyEPR as epr
from pathlib import Path
import logging
epr.logger.setLevel(logging.DEBUG)

if 1:
  path_to_project = r'Z:\akshay_koottandavida\3. Pair-Coherent States\HFSS\pcs_straddling_regime'
  pinfo = epr.ProjectInfo(project_path = path_to_project, 
                           project_name = 'straddling_regime_transmon',
                           design_name  = '2. stradling_tmon_prev_sample')
  
  pinfo.junctions['j1'] = {'Lj_variable' : 'LJ_wig', 
                           'rect'        : 'wigner_qubit', 
                           'line'        : 'Polyline1', 
                           'length'      : epr.parse_units('200um')}
  
  pinfo.validate_junction_info() 
  eprh = epr.DistributedAnalysis(pinfo)
  eprh.do_EPR_analysis();
  
  epra = epr.QuantumAnalysis(eprh.data_filename)
  
  # Analyze 
  epra.analyze_all_variations(cos_trunc = 6, fock_trunc = 7,return_ef=True)
  #epra.plot_hamiltonian_results();

#%%
  
import matplotlib.pyplot as plt
chi_ef = [epra.results[str(i)]['chi_ef'] for i in range(11)]
freq = [epra.results[str(i)]['f_ND'][2] for i in range(11)]

plt.plot(freq,chi_ef,'o')
plt.show()
  
  
  
  
  
  
  
  
  
  
  
  