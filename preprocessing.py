import numpy as np
import scipy as sp

from math import *
import os,glob,sys

# from joblib import Parallel, delayed
# import multiprocessing

import cPickle as pickle
import pandas as pd

from IPython import embed

# sys.path.append('tools/')
from BehaviorAnalyzer import BehaviorAnalyzer


raw_data_folder = '/home/barendregt/Projects/PredictionError/Psychophysics/Data/k1f46/' #raw_data'
shared_data_folder = raw_data_folder #'raw_data'
figfolder = '/home/barendregt/Analysis/PredictionError/Figures'

sublist = ['AA','AB','AC','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO']#
sublist = ['AO']
#['s1','s2','s3','s4','s5','s6']#['s1','s2','s4']['s1','s2',[

# subname = 's1'#'tk2'#'s3'#'mb2'#'tk2'#'s3'#'tk2'

low_pass_pupil_f, high_pass_pupil_f = 6.0, 0.01

signal_sample_frequency = 1000
deconv_sample_frequency = 8
deconvolution_interval = np.array([-0.5, 4.5])

down_fs = 10
winlength = 4500#6500
minwinlength = 4000#6000
 
def run_analysis(subname):	

	print '[main] Running analysis for %s' % (subname)

	rawfolder = os.path.join(raw_data_folder,subname)
	sharedfolder = os.path.join(shared_data_folder,subname)

	csvfilename = glob.glob(rawfolder + '/*.csv')#[-1]

	h5filename = os.path.join(sharedfolder,subname+'.h5')

	pa = BehaviorAnalyzer(subname, csvfilename, h5filename, rawfolder, reference_phase = 3, signal_downsample_factor = down_fs, signal_sample_frequency = signal_sample_frequency, deconv_sample_frequency = deconv_sample_frequency, deconvolution_interval = deconvolution_interval)

	# pa.recombine_signal_blocks()
	# Pupil data
	# pa.load_data()

	pa.preprocessing_report()

	# pa.signal_per_trial()
	# pa.recombine_signal_blocks()
	# Pupil data

	# pa.event_related_average()
	# #pa.extract_signal_blocks()
	# # pa.run_FIR()


	# pa.store_pupil()



	# # Task data
	# pa.compute_performance()
	# # pa.compute_performance_pred_unpred()
	# # pa.compute_performance_attended_unattended()

	# #pa.fit_cum_gauss()
	# # pa.fit_sig_fun()
	# pa.fit_sig_fun('pred-v-unpred')
	# # pa.fit_sig_fun('col_pred-v-unpred')
	# # pa.fit_sig_fun('ori_pred-v-unpred')
	# # pa.fit_sig_fun('col_att-v-unatt')
	# # pa.fit_sig_fun('ori_att-v-unatt')

	# pa.store_behavior()
	




	pa.unload_data()

[run_analysis(sub) for sub in sublist]
# Run everything in parallel for speed 
# num_cores = multiprocessing.cpu_count()

# Parallel(n_jobs=num_cores)(delayed(run_analysis)(subname) for subname in sublist)