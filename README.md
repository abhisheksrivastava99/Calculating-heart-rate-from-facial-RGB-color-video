# Calculating-heart-rate-from-facial-RGB-color-video
**Step-1**:Record two videos in different light conditions.</br>
**Step-2**:Import critical python libraries required.</br>
**Step-3**:Read both the videos from local storage.</br>
**Step-4**:Detect face and facial landmarks. </br>
**Step-5**:Select forehead as ROI.</br>
**Step-6**:Compute mean and perform normalization of respective RGB channel values.</br>
**Step-7**:Apply ICA and input will be RGB channel normalized values.</br>
**Step-8**:Apply fourier transform.</br>
**Step-9**:Calculate heart rate.</br>
HR=60*(number of peaks/time) bpm </br>
**Step-10**:Plot the graph.</br>
**Step-11**:Calculate heart rate variability(HRV) using RMSSD.</br>




## References
**1.** https://www.osapublishing.org/boe/fulltext.cfm?uri=boe-6-7-2466&id=320343</br>
**2.** https://www.osapublishing.org/boe/fulltext.cfm?uri=boe-5-4-1124&id=281701</br>
**3.** https://dsp.stackexchange.com/questions/48421/camera-measurement-of-heart-rate-frequency-bias-towards-50-bpm-0-83-hz</br>
**4.** https://web.mit.edu/~gari/www/papers/GDCliffordThesis.pdf</br>
**5.** https://web.njit.edu/~joelsd/signals/classwork/BME314signalscw12a.pdf</br>


**6.** https://www.researchgate.net/publication/308847680_Determination_of_heart_rate_from_photoplethysmogram_using_Fast_Fourier_Transform</br>
**7.** https://imotions.com/blog/heart-rate-variability/</br>
**8.** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5624990/</br>
**9.** https://stackoverflow.com/questions/57647638/how-can-i-detect-the-forehead-region-using-opencv-and-dlib</br>
**10.** https://www.pyimagesearch.com/2017/04/10/detect-eyes-nose-lips-jaw-dlib-opencv-python/</br>
**11.** https://www.pyimagesearch.com/2021/01/19/crop-image-with-opencv/</br>
**12.** https://www.geeksforgeeks.org/detect-the-rgb-color-from-a-webcam-using-python-opencv/</br>
**13.** http://people.csail.mit.edu/balakg/cvpr2013_pulsepaper.pdf</br>
**14.** https://web.stanford.edu/class/cs231a/prev_projects_2016/finalReport.pdf</br>
**15.** https://chrisalbon.com/machine_learning/preprocessing_images/using_mean_color_as_a_feature/</br>
**16.** https://ep.liu.se/ecp/129/002/ecp16129002.pdf</br>
**17.** https://towardsdatascience.com/independent-component-analysis-ica-in-python-a0ef0db0955e</br>
