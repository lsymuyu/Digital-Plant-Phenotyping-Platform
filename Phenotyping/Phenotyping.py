'''
The main function to conduct phenotyping experiments

11/09/2017
Shouyang Liu

'''

import os
from adel import AdelR
from adel.geometric_elements import Leaves
from adel.AdelR import R_xydb, R_srdb, genGeoLeaf
import pandas as pd
from adel.plantgen import plantgen_interface
import numpy as np
from adel.astk_interface import AdelWheat
from adel.stand.Generate_canopy import get_exposed_areas
from adel.postprocessing import axis_statistics_simple, plot_statistics_simple, plot_statistics_simple_filter, axis_statistics_simple_filter
from adel.povray.povray_ind import povray_Green
from pyDOE import *
from scipy.stats import uniform
from openalea.core.path import path
from adel.ADEL_OPT.Adel_OPT_Ind import Adel_Leaves, Adel_development
import prosail
from adel.ADEL_OPT.Adel_OPT_Ind import plot_LAI
from adel.macro.povray_pixels_several_colors import set_color_metamers_organs
from adel.povray.FAPAR import Sampling_diagnal, Hemispherical_IM, Sampling_GF, Hemispherical_IM_Sun
from adel.povray.GF_RGB import Green_Fract, Pov_Scene
from adel.povray.Canray import duplicate_scene, Optical_canopy, Optical_soil, povray_RF


def Phenotyping_Wheat(Param, Ind, thermals, Canopy, Adel_output,
                    LAI = False,save_scene = False,
                    GF = False, GF_camera = [],
                    FAPAR = False, Sunlit_TT = [], Sunlit_Ang = [],
                    Multi_spectral = False, Ray_camera = [], Ray_light = []):

    try:
        # Adel parameters
        development_parameters = Adel_development(N_phytomer_potential = float(Param['N_leaf']), a_cohort = float(Param['a_cohort']),
                                                  TT_hs_0 = float(Param['T_cohort']), TT_flag_ligulation = float(Param['TT_flag_ligulation']),
                                                  n0 = float(Param['n0']), n1 = float(Param['n1']), n2 = float(Param['n2']), 
                                                  number_tillers = float(Param['number_tillers']),
                                                  Lamina_L1 = float(Param['Lamina_L1']), N2 = float(Param['N2']), incl1 = float(Param['incl1']),
                                                  incl2 = float(Param['incl2']), N_elg = float(Param['N_elg']), density = float(Param['Density']))

        wheat_leaves = Adel_Leaves(incline = float(Param['incl_leaf']), dev_Az_Leaf = float(Param['dev_Az_Leaf']))

        # canopy configuration
        sim_width   = float(Canopy['width']) # m, generate three rows
        dup_length  = float(Canopy['length'])
        
        Row_spacing = float(Param['Row_spacing'])

        run_adel_pars = {'senescence_leaf_shrink': 0.01, 'leafDuration': 2, 'fracLeaf': 0.2, 'stemDuration': 2. / 1.2,
                         'dHS_col': 0.2, 'dHS_en': 0, 'epsillon': 1e-6, 'HSstart_inclination_tiller': 1,
                         'rate_inclination_tiller': float(Param['rate_Tiller']), 'drop_empty': True}

        # build the distribution pattern table to interpolate the density
        Wheat_Adel = AdelWheat(density = float(Param['Density']), duplicate = 40, devT = development_parameters,
                               leaves = wheat_leaves, pattern='regular', run_adel_pars = run_adel_pars,
                               incT = float(Param['Deta_Incl_Tiller']), ibmM = float(Param['incl_main']),
                               depMin = float(Param['min_Tiller']), dep = float(Param['max_Tiller']),
                               inter_row = Row_spacing, width = sim_width, length = dup_length)
        del development_parameters, wheat_leaves
        
        domain = Wheat_Adel.domain
        domain_area = Wheat_Adel.domain_area
        nplants = Wheat_Adel.nplants

        for TT in thermals:
            Canopy_Adel = Wheat_Adel.setup_canopy(age=TT)
            
            plantgl_scene = set_color_metamers_organs(Canopy_Adel)[0]
            
            # Summary LAI
            if LAI:
                new_plot_df = plot_LAI(Canopy_Adel, TT, domain_area, nplants, Adel_output, Ind)
                if 'plot_df' in locals():
                    plot_df = pd.concat([plot_df,new_plot_df])
                else:
                    plot_df = new_plot_df

            del Canopy_Adel
            # Save geometry file
            name_canopy = '%s%s%s%s.bgeom'%('Ind_',Ind,'_TT_',TT)
            if save_scene:
                plantgl_scene.save(Adel_output + '/' + name_canopy, 'BGEOM')
            
            # Green fraction
            if GF:
                sampling_times = GF_camera['Times_sampling']
                cameras = Sampling_GF(domain, sampling_times, 
                                           Azimuth = GF_camera['azimuth'], Zenith = GF_camera['zenith'],
                                           Row_spacing = Row_spacing, fov = GF_camera['fov'])[0]

                povfile_mesh, povfile_box, z_top = Pov_Scene(plantgl_scene, domain, 
                                                             output_directory = Adel_output, 
                                                             thermal = TT, Ind = Ind)                                                               
                povfile_scene, new_df = Green_Fract(povfile_mesh, povfile_box,
                                                    thermal = TT, Ind = Ind, cameras = cameras, 
                                                    image_height = GF_camera['image_height'], image_width = GF_camera['image_width'],
                                                    relative_height = GF_camera['distance'], z_top = 0,
                                                    output_directory = Adel_output)
                if 'result_df' in locals():
                    result_df = pd.concat([result_df,new_df])
                else:
                    result_df = new_df              

            # Fisheye for FAPAR
            if FAPAR:
                Azimuth_fisheye = [0]
                Zenith_fisheye = [0]
                sampling_times = 7
                dup_width = 8.0

                New_canopy, New_nplants, New_domain, New_area = duplicate_scene(plantgl_scene, nplants, canopy_width = dup_width,
                                                                                canopy_length = dup_length, sim_width = sim_width,
                                                                                Row_spacing = Row_spacing)
                domain = New_domain
                del plantgl_scene
                cameras_fisheye = Sampling_diagnal(New_domain, sampling_times,
                                                   Azimuth_fisheye, Zenith_fisheye,
                                                   Row_spacing, fov_fisheye)[0]
                povfile_mesh_new, povfile_box_new, z_top_new = Pov_Scene(New_canopy, New_domain,
                                                                         output_directory = Adel_output,
                                                                         thermal = TT, Ind = Ind)
                del New_canopy
                povray_image_fisheye = Hemispherical_IM(povfile_mesh = povfile_mesh_new, z_top = z_top_new,
                                                        cameras = cameras_fisheye,
                                                        image_height = 2000, image_width = 2000,
                                                        relative_height = relative_height,
                                                        output_directory = Adel_output)
                if TT in Sunlit_TT:
                    for A_sun in Sunlit_Ang:
                        povray_image_fisheye = Hemispherical_IM_Sun(povfile_mesh = povfile_mesh_new, z_top = z_top_new,
                                                                    cameras = cameras_fisheye, A_sun = A_sun,
                                                                    image_height = 2000, image_width = 2000,
                                                                    relative_height = relative_height,
                                                                    output_directory = Adel_output)
                                    
            # Simulate BRDF (need large scene)
            if Multi_spectral:
            # Setting of prosail
                RT = prosail.prospect_5b(n = Param['N'], cab = Param['Cab'], car = Param['Car'],
                                         cbrown = Param['Cbrown'], cw = Param['Cw'], cm = Param['Cm'])
                Full_wave = range(400, 2501)
                R = RT[:,0]
                T = RT[:,1]
                for wave in Ray_camera['Waves']:
                    Plant_optical = Optical_canopy(wave=wave, Full_wave=Full_wave, R=R, T=T)

                    soil_ref = Optical_soil(wave, brightness=Param['brightness'])

                    Output_file = povray_RF(Ray_light=Ray_light, Ray_camera=Ray_camera, Plant_optical=Plant_optical,
                                            soil_ref=soil_ref, domain=domain, povfile_scene=povfile_mesh,
                                            wave=wave, soil_type = Param['soil_type'],
                                            dict=Adel_output)

                    if not os.path.exists(Output_file):
                        Output_file = povray_RF(Ray_light=Ray_light, Ray_camera=Ray_camera, Plant_optical=Plant_optical,
                                                soil_ref=soil_ref, domain=domain, povfile_scene=povfile_mesh, 
                                                wave=wave,soil_type = Param['soil_type'], dict=Adel_output)
        
        if 'plot_df' in locals():
            result_plot_path = path(os.path.join(Adel_output, '%s%s%s'%('plot_LAI_',Ind,'.csv')))
            plot_df.to_csv(result_plot_path, index=False)
        
        if 'result_df' in locals():
            result_df_path = path(os.path.join(Adel_output, '%s%s%s'%('Fraction_',Ind,'.csv')))
            result_df.to_csv(result_df_path, index=False)

    except TypeError:
        print 'Pass it and move forward!!!***'
        result_df_path = []
        pass

    return Adel_output

def Phenotyping_Wheat_TT(Param, Ind, TT, Adel_output,
                         Ray_light = [], Ray_camera = [], Zenith_GF = [],
                         FAPAR = True, GF = True, Multi_spectral = False,
                         save_scene = False):

    try:
        # Adel parameters
        Row_spacing = float(Param['Row_spacing'])
        sim_width =  1.0
        dup_length = 12.0
        
        development_parameters = Adel_development(N_phytomer_potential = float(Param['N_leaf']), a_cohort = float(Param['a_cohort']),
                                                  TT_hs_0 = float(Param['T_cohort']), TT_flag_ligulation = float(Param['TT_flag_ligulation']),
                                                  n0 = float(Param['n0']), n1 = float(Param['n1']), n2 = float(Param['n2']), number_tillers = float(Param['number_tillers']),
                                                  Lamina_L1 = float(Param['Lamina_L1']), N2 = float(Param['N2']), incl1 = float(Param['incl1']),
                                                  incl2 = float(Param['incl2']), N_elg = float(Param['N_elg']), density = float(Param['Density']))

        wheat_leaves = Adel_Leaves(incline = float(Param['incl_leaf']), dev_Az_Leaf = float(Param['dev_Az_Leaf']))  

        run_adel_pars = {'senescence_leaf_shrink': 0.01, 'leafDuration': 2, 'fracLeaf': 0.2, 'stemDuration': 2. / 1.2,
                         'dHS_col': 0.2, 'dHS_en': 0, 'epsillon': 1e-6, 'HSstart_inclination_tiller': 1,
                         'rate_inclination_tiller': float(Param['rate_Tiller']), 'drop_empty': True}

        # build the distribution pattern table to interpolate the density
        Wheat_Adel = AdelWheat(density = float(Param['Density']), duplicate = 20, devT = development_parameters,
                               leaves = wheat_leaves, pattern='regular', run_adel_pars = run_adel_pars,
                               incT = float(Param['Deta_Incl_Tiller']), ibmM = float(Param['incl_main']),
                               depMin = float(Param['min_Tiller']), dep = float(Param['max_Tiller']),
                               inter_row = Row_spacing, width = sim_width, length = dup_length)
        del Param, development_parameters, wheat_leaves
        
        domain = Wheat_Adel.domain
        domain_area = Wheat_Adel.domain_area
        nplants = Wheat_Adel.nplants

        Canopy_Adel = Wheat_Adel.setup_canopy(age=TT)
        del Wheat_Adel
        plantgl_scene = set_color_metamers_organs(Canopy_Adel)[0]
        
        # Summary LAI
        plot_df = plot_LAI(Canopy_Adel, TT, domain_area, nplants, Adel_output, Ind)
        result_plot_path = path(os.path.join(Adel_output, '%s%s%s%s%s'%('plot_LAI_',Ind,'_TT_',TT,'.csv')))
        plot_df.to_csv(result_plot_path, index=False)
        del plot_df, Canopy_Adel
        
        # Save geometry file
        name_canopy = '%s%s%s%s.bgeom'%('Ind_',Ind,'_TT_',TT)
        if save_scene:
            plantgl_scene.save(Adel_output + '/' + name_canopy, 'BGEOM')
        
        # Common setting
        relative_height = 200 # camera above the canopy
        
        # Green fraction
        if GF:
            Azimuth = [0]
            fov = [10]
            sampling_times = 4
            cameras = Sampling_GF(domain, sampling_times, 
                                       Azimuth, Zenith_GF, 
                                       Row_spacing, fov)[0]
            povfile_mesh, povfile_box, z_top = Pov_Scene(plantgl_scene, domain, 
                                                         output_directory = Adel_output, 
                                                         thermal = TT, Ind = Ind)                                                        
            povfile_scene, result_df = Green_Fract(povfile_mesh, povfile_box,
                                                thermal = TT, Ind = Ind, cameras = cameras, 
                                                image_height = 1000, image_width = 1000, 
                                                relative_height = relative_height, z_top = z_top,
                                                output_directory = Adel_output)            
            result_df_path = path(os.path.join(Adel_output, '%s%s%s%s%s'%('Fraction_',Ind,'_TT_',TT,'.csv')))
            result_df.to_csv(result_df_path, index=False)

        # Fisheye for FAPAR
        if FAPAR:
            Azimuth_fisheye = [0]
            Zenith_fisheye = [0]
            fov_fisheye = [120]
            dup_width = 12.0
            sampling_times = 7

            New_canopy, New_nplants, New_domain, New_area = duplicate_scene(plantgl_scene, nplants, canopy_width = dup_width,
                                                                            canopy_length = dup_length, sim_width = sim_width,
                                                                            Row_spacing = Row_spacing)
                        
            del plantgl_scene
            cameras_fisheye = Sampling_diagnal(New_domain, sampling_times,
                                               Azimuth_fisheye, Zenith_fisheye,
                                               Row_spacing, fov_fisheye)[0]
            povfile_mesh_new, povfile_box_new, z_top_new = Pov_Scene(New_canopy, New_domain,
                                                                     output_directory = Adel_output,
                                                                     thermal = TT, Ind = Ind)
            del New_canopy
            povray_image_fisheye = Hemispherical_IM(povfile_mesh = povfile_mesh_new, z_top = z_top_new,
                                                    cameras = cameras_fisheye,
                                                    image_height = 2000, image_width = 2000,
                                                    relative_height = relative_height,
                                                    output_directory = Adel_output)
        # Simulate BRDF (need large scene)
        if Multi_spectral:
            # Setting of prosail
            RT = prosail.prospect_5b(n = Param['N'], cab = Param['Cab'], car = Param['Car'],
                                     cbrown = Param['Cbrown'], cw = Param['Cw'], cm = Param['Cm'])
            Full_wave = range(400, 2501)
            R = RT[:,0]
            T = RT[:,1]
            for wave in Waves_camera:
                Plant_optical = Optical_canopy(wave=wave, Full_wave=Full_wave, R=R, T=T)

                soil_ref = Optical_soil(wave, brightness=Param['brightness'])

                Output_file = povray_RF(Ray_light=Ray_light, Ray_camera=Ray_camera, Plant_optical=Plant_optical,
                                        soil_ref=soil_ref, domain=New_domain, povfile_scene=povfile_scene,
                                        wave=wave,
                                        dict=Adel_output)

                if not os.path.exists(Output_file):
                    Output_file = povray_RF(Ray_light=Ray_light, Ray_camera=Ray_camera, Plant_optical=Plant_optical,
                                            soil_ref=soil_ref, domain=New_domain, povfile_scene=povfile_scene,
                                            wave=wave,
                                            dict=Adel_output)
    except TypeError:
        print 'Pass it and move forward!!!***'
        result_df_path = []
        pass

    return Adel_output