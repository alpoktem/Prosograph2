DATASET_ENG = "/Users/alp/Documents/phdCloud/playground/Prosograph2/data/eng"
DATASET_SPA = "/Users/alp/Documents/phdCloud/playground/Prosograph2/data/spa"
dataset_tags = {}

word_key = 'word'    #integer value which has the corresponding text in the vocabulary
punctuation_before_key = 'punctuation_before'
draw_punctuation = True
pause_before_key = 'pause_before'
draw_pause_boxes = True
word_duration_key = '' 
draw_word_duration = False
binary_feature_key = ''
label_feature_key = ''
draw_label_feature = False

draw_feature_line = True
point_feature_keys = ['i0_mean']
line_feature_keys = ['f0_mean']
curve_feature_keys = []
curve_axis_keys = []
evened_curve_feature_keys = []
percentage_feature_keys = [] 

minFeatureVal = -30
maxFeatureVal = 30

color_dict = {'f0_mean': [75, 150, 225, 255], 'i0_mean': [150, 100, 175, 255]}
