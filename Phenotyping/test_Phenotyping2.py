'''
Simulate RGB and fisheye imagery
Shouyang

08/09/2017
'''


import pandas as pd
from adel.Phenotyping.Phenotyping import Phenotyping_Wheat_TT

Ind = 2

for TT in [1050, 1100]:
    # Read properties
    design_path = r'D:\Papers\HTPPF_FIPAR\Data\FIPAR_Contrast.csv'
    Param_table = pd.read_csv(design_path)

    Param = Param_table[Param_table['Index'] == Ind]
    Output_dict = r'D:\Papers\HTPPF_FIPAR\Sim_fipar\IND_2'
    Zenith_camera = [0, 45]

    Phenotyping_Wheat_TT(Param, Ind=Ind, TT=TT,
                         Adel_output=Output_dict,
                         Zenith_GF=Zenith_camera,
                         FAPAR=False, GF=True, save_scene=False)
