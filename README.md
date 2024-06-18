# TemplateMatch
A repository for scripts to do frequency domain cross-correlation template matching with DAS data. 

1.) Read in data and do any preprocessing needed.  
2.) Use `window_and_correlate` function from `mm.py` for 2D DAS data or the `window_and_correlate` function from `mm_1d.py` for geophone / seismometer data.  
3.) Use `detections` function from `mad_funcs.py` to calculate MAD (median absolute deviation) for detection significance.  
