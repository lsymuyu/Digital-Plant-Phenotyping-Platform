'''
This script provides functions to:
- create a PlantGL scene from a pandas.DataFrame of digitized data (see digits_to_scene),
- run Caribu on a PlantGL scene (see run_caribu).

TODO:  voir comment appliquer une forme (2D) a une courbure 3D (voir dataflow "animated leaf" + pgl_edition_node.curve2D)
#   -> exemples d alinea.adel.leaf utilisent en entree des courbures et formes 2D (xy et sr) ; alinea.adel.fitting.leaf_to_mesh_new(...) permet de construire un mesh avec un nombre defini de twists. leaf_to_mesh, leaf_to_mesh_new, partial_leaf semblent n ajouter qu 1 triangle a la fin de la feuille.
#   -> appeler Christian pour lui demander s'il existe des routines pour appliquer une forme 2D a une courbure 3D ; evoquer probleme des pointes.

This script was from Mariem at 22/04/2018
Some revisions were made by Shouyang
25/04/2018
'''

import math
from math import pi
import numpy as np
import pandas as pd
from scipy import optimize
from openalea.plantgl.all import *
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

#LEAF_COLORS = {(-2.0,-1.5): (0,255,0), (-1.5,-1): (29,255,0), (-1.0,-0.5): (57,255,0), # green
#               (-0.5,0.0): (86,255,0), (0.0,0.5): (114,255,0), (0.5,1.0): (143,255,0),
#               (1.0,1.5): (171,255,0), (1.5,2.0): (200,255,0),
#               (2.0,2.5): (235,255,0), (2.5,3.0): (255,240,0), (3.0,3.5): (255,205,0), (3.5,4.0): (255,170,0), # yellow
#               (4.0,4.5): (200,100,0), (4.5,5.0): (100,50,0)} # brown

LEAF_COLORS = {(-2.0,5.0): (0,255,0)} # brown

STEM_COLORS = {(0.0,13.0): (51,255,0)}

class TinoLeafShapeModel(object):

    def __init__(self, wmax, klig=0.7, swmax=0.9, f1=0.6, f2=0.9):
        self.wmax = wmax
        self.swmax = swmax
        self.c1 = self._compute_c1(f1)
        self.c2 = self._compute_c2(klig, f2)
        self.wlig = klig * self.wmax

    def _compute_c1(self, f1):
        return (1.0 - f1) / f1

    def _compute_c2(self, klig, f2):
        def f2_function(c2):
            return klig + (1 - klig) * (1 + 1.0 / c2) - 1.0 / math.log(1 + c2) - f2
        sol = optimize.root(f2_function, 0.0001)
        if not sol.success:
            raise Exception('Error computing c2 !!!')
        return sol.x[0]

    def compute_width(self, l, lmax):
        ''' l: length from the BASE of the leaf
        '''
        s = 1 - l / float(lmax)
        if s < self.swmax: # distal segment # Bug corrected by me
            w = self.wmax * (s / self.swmax) ** self.c1
        else: # basal segment
            w = self.wlig + (self.wmax - self.wlig) * math.log(1 + self.c2 * (1 - s) / (1 - self.swmax)) / math.log(1 + self.c2)
        return w

class OldLeafShapeModel(object):

    def __init__(self, alpha=-2.3):
        self.alpha = alpha
        self.beta = -2 * (alpha + math.sqrt(-alpha))
        self.gamma = 2 * math.sqrt(-alpha) + alpha

    def compute_width(self, l, lmax):
        s = l / float(lmax)
        return self.alpha * s**2 + self.beta * s + self.gamma

def leaf_extrusion(polyline, segment, shape_model):
    """ Extrude a Polyline to a QuadSet according to a shape model.
    Permits to construct the geometry of a leaf from midrib digitized points.
    segment is the normal of the Polyline at first digitized point. This normal passes
    through the origin of the affine frame.
    """
    n = len(polyline)
    midrib_points = np.array(list(polyline)*2)
    seg = segment

    len_max = polyline.getLength()
    current_len = 0
    current_base = [polyline[0][0],polyline[0][1],polyline[0][2]]

    for p in range (0,n-1):
        current_len += math.sqrt((polyline[p][0]-current_base[0])**2 + (polyline[p][1]-current_base[1])**2 + (polyline[p][2]-current_base[2])**2)
        width = shape_model.compute_width(current_len, len_max)
        midrib_points[p] -= seg * width/2.
        midrib_points[p+n] += seg * width/2.
        current_base = [polyline[p][0],polyline[p][1],polyline[p][2]]
    indices = [(i,i+n,i+n+1,i+1) for i in range(n-1)]
    geom = QuadSet(midrib_points, indices)
    return geom

def center_rotate(SC, Z_rotate, delta_Y):
#    bd = BoundingBox(SC)
#    
#    X_min = bd.getXMin()
#    Y_min = bd.getYMin()
#    
#    X_max = bd.getXMax()
#    Y_max = bd.getYMax()
#    
#    X = (X_max + X_min)/2.0
#    Y = (Y_max + Y_min)/2.0
    delta = delta_Y/2.0
    
    angles = math.radians(Z_rotate)
    
    SC = Scene([Shape(Translated(0, delta, 0, sh.geometry), sh.appearance,
                sh.id, sh.parentId) for sh in SC])
    
    SC = Scene([Shape(AxisRotated((0, 0, 1), angles, sh.geometry), sh.appearance,
                sh.id, sh.parentId) for sh in SC])
        
    SC = Scene([Shape(Translated(0, -delta, 0, sh.geometry), sh.appearance,
                sh.id, sh.parentId) for sh in SC])    
    
    return SC

def stem_extrusion(coordinates, radius):
    ''' Extrude a list of 3D coordinates.
    Permits to construct the geometry of a stem from digitized points and stem radius.
    '''
    coordinates_array = np.array(coordinates)
    coordinates_and_weights = np.column_stack((coordinates_array, np.ones(len(coordinates))))
    cir = Polyline2D.Circle(radius,50)
    prof = NurbsCurve(coordinates_and_weights)
    return Extrusion(prof, cir)

def digits_to_scene(digits_df, max_leaf_width=1.15, stem_diameter=0.25, digit_criteria={},   # !! here i used a mean maximum blade width that apllied for all treatements and all leaves and so on for stem_diamter... to be changed !!!
                    leaf_colors=LEAF_COLORS, stem_colors=STEM_COLORS,
                    display_leaf_age=False, display_haun_stage=False):
    '''
    Create a PlantGL scene from digitized data.

    Parameters
    ----------
    digits_df: pandas.DataFrame
        The dataframe of the digits.
    max_leaf_width: float, optional
        The maximum width of a leaf. Used by the leaf shape model. Default is 1.0.
    stem_diameter: float, optional
        The diameter of a stem. Used for stem extrusion. Default is 0.2.
    digit_criteria: dict, optional
        A dictionary whose keys are the columns of `digits_df` for which one want to apply
        a specific filter. These columns are: 'N_digit', 'Plant', 'axe', 'Leaf_number',
        'Variety_Interow', 'Organ', 'haun_stage' and 'Leaf_age'. The value associated to each key
        is a criteria that the rows of `digits_df` must satisfy to be included in
        the PlantGl scene. The values can be either one value or a list of values.
        For 'haun_stage' and 'Leaf_age', the value can be also an interval or a list
        of intervals. By default, all the digits are included.
    leaf_colors: dict, optional
        A dictionary whose keys are leaf_age intervals, and whose values are the RGB colors
        associated to these intervals. Permits to color the leaves depending on their age.
        Default is LEAF_COLORS.
    stem_colors: dict, optional
        A dictionary whose keys are haun_stage intervals, and whose values are the RGB colors
        associated to these intervals. Permits to color the stems depending on their haun stage.
        Default is STEM_COLORS.
    display_leaf_age: bool, optional
        Whether to create a PlantGL Text for each leaf age. If True, the Text is
        positioned at the tip of the leaf. Default is False.
    display_haun_stage: bool, optional
        Whether to create a PlantGL Text for each haun stage. If True, the Text is
        positioned at the middle of the stem. Default is False.

    Row direction is along Y axis.

    Returns
    -------
    out : PlantGL scene

    '''
    digit_criteria = digit_criteria.copy()
    for column, value in digit_criteria.items():
        if not isinstance(value, list):
            digit_criteria[column] = value = [value]
        if column in ('leaf_age', 'haun_stage') and \
        isinstance(value[0], tuple): # interval
            indexes_to_keep = []
            for interval in value:
                selection = (interval[0] <= digits_df[column]) & (digits_df[column] <= interval[1])
                indexes_to_keep.extend(selection[selection].index) # TODO: to check!
            indexes_to_keep.sort()
            digits_df = digits_df.ix[indexes_to_keep]
        else: # not an interval
            digits_df = digits_df.select(lambda idx: digits_df[column][idx] in value)

    digits_df.fillna(0, inplace=True)

    scene = Scene()

    leaf_age_intervals = sorted(leaf_colors.keys())

    haun_stage_intervals = sorted(stem_colors.keys())
    Bot_loc = [] # location of the plants bottom

   # stem_radius = stem_diameter / 2.0

    # Loop over each leaf3D_digit
    for (n_digit,variety_interow,  plant, axis,id_axis,id_cohort, organ,leaf_number, haun_stage, leaf_age), db_group in \
            digits_df.groupby(['N_digit', 'Variety_Interow','Plant', 'axis','id_axis','id_cohort', 'Organ','Leaf_number_ntop','haun_stage','Leaf_age']):
       
        coordinates = zip(db_group.X0, db_group.Y0, db_group.Z0)
        X0 = db_group['X0'].values.tolist()
        Y0 = db_group['Y0'].values.tolist()
        Z0 = db_group['Z0'].values.tolist()
        
        is_leaf = organ == 'Leaf'
        if is_leaf: # Leaf element
            if len(X0) < 4:
                midrib = Polyline(coordinates)
            else:
                tck, u = interpolate.splprep([X0, Y0, Z0], s=3)

                N = len(X0)
                u_fine = np.linspace(0,1,N)
                x_fine, y_fine, z_fine = interpolate.splev(u_fine, tck)
                coordinates = zip(x_fine, y_fine, z_fine)
                midrib = Polyline(coordinates)                
            
            if len(midrib) < 1:
                raise Exception('len(midrib) < 1 !!!')

            Wblade = db_group.Wblade
            n = midrib.getNormalAt(0).normed()
            geom = leaf_extrusion(midrib, n, TinoLeafShapeModel(wmax = Wblade.iloc[0]))
            #geom = leaf_extrusion(midrib, n, OldLeafShapeModel())
            # look for a color to apply to this leaf
            try:
                leaf_age_interval = next((leaf_age_interval for leaf_age_interval in leaf_age_intervals if (leaf_age_interval[0] <= leaf_age and leaf_age <= leaf_age_interval[1])))
            except StopIteration: # there is no color associated to the current leaf age
                color = Color3.BLACK
            else:
                color = leaf_colors[leaf_age_interval]
            if display_leaf_age:
                tip_coordinate = coordinates[-1]
                text = Text(str(leaf_age), tip_coordinate)
                text_shape = Shape(text, Material(Color3.BLACK))
                scene.add(text_shape)
        else: # Stem element
            Bot_loc.append(Y0[0])
            stem_radius = db_group.Dstem
            geom = stem_extrusion(coordinates, stem_radius.iloc[0]/2.0)
            # look for a color to apply to this stem
            try:
                haun_stage_interval = next( (haun_stage_interval for haun_stage_interval in haun_stage_intervals if (haun_stage_interval[0] <= haun_stage and haun_stage <= haun_stage_interval[1])))
            except StopIteration: # there is no color associated to the current haun stage
                color = Color3.BLACK
            else:
                color = stem_colors[haun_stage_interval]
            if display_haun_stage:
                middle_coordinate = coordinates[len(coordinates)/2]
                text = Text(str(haun_stage), middle_coordinate)
                text_shape = Shape(text, Material(Color3.BLACK))
                scene.add(text_shape)
        opt_sp = 1 # TODO : a tester sur leafscen
        id = int(opt_sp*10**7 + plant*10**5 + id_axis*10**3 + leaf_number*10**1 + int(is_leaf))
        shape = Shape(geom, Material(color), id)
        scene.add(shape)

    return scene, Bot_loc

def scene_big(SC, Bot_loc, sim_length, sim_width, Row_spacing):
    
    seg_n  = math.ceil(sim_length/40.0)
    N_duplicate = math.ceil(sim_width/Row_spacing/2.0)
    deta = Bot_loc[-1] - 100.0/(200.0/(100.0/Row_spacing))    
    
    New_sc = SC
    Z_rotate = 180
    # duplicate length
    for n in range(1,int(seg_n)):
#        SC_rotate = center_rotate(SC,Z_rotate*n, Bot_loc[-1])

        sc_plus = Scene([Shape(Translated(0,deta*n,0,sh.geometry), sh.appearance,
                         sh.id, sh.parentId) for sh in SC])
    
        New_sc = Scene([New_sc, sc_plus])
    
    L_sim = abs(deta*seg_n) # the true simulated length
    
    # duplicate width
    sc_final = New_sc
    angle = 180
    rangle = math.radians(angle)

    for n in range(1,int(N_duplicate)):
#        New_sc = center_rotate(New_sc,Z_rotate*n, L_sim)

        sc_plus = Scene([Shape(Translated(-Row_spacing*n,0,0,sh.geometry), sh.appearance,
                        sh.id, sh.parentId) for sh in New_sc])
            
#       sc_plus = Scene([Shape(EulerRotated(0,pi/2,pi/2,sh.geometry), sh.appearance,
#                     sh.id, sh.parentId) for sh in sc_plus])

        sc_minus = Scene([Shape(Translated(Row_spacing*n,0,0,sh.geometry), sh.appearance,
                        sh.id, sh.parentId) for sh in New_sc])

        sc_final = Scene([sc_final, sc_plus, sc_minus])
    
    W_sim = N_duplicate*Row_spacing*2

    return sc_final, L_sim, W_sim