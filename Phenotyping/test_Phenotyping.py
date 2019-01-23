'''
Test phenotyping main function

08/09/2017
'''

import pandas as pd
from adel.Phenotyping.Phenotyping import Phenotyping_Wheat_TT
Ind = 43

# Read properties
design_path = r'D:\Papers\JY_3D_canopy\Test_canray_JY_5.csv'
Param_table = pd.read_csv(design_path)

Param = Param_table[Param_table['Index'] == Ind]
Output_dict = r'D:\Papers\FAPAR\Sim_Fapar2'
Zenith_camera = [0, 45]
TT = 350

Phenotyping_Wheat_TT(Param, Ind, TT = TT,
                  Adel_output = Output_dict,
                  Zenith_GF = Zenith_camera,
                  save_scene = False, FAPAR = True, GF = False)