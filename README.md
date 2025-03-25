# Heart Rate Calculation from Facial RGB Video

## Overview
This project calculates heart rate from facial videos recorded in **normal light** and **low light** conditions. It utilizes computer vision and signal processing techniques to extract **pulse signals** from subtle changes in skin color.

## Steps to Calculate Heart Rate
**Step 1**: Record two videos in different light conditions.  
**Step 2**: Import critical Python libraries.  
**Step 3**: Read both videos from local storage.  
**Step 4**: Detect face and facial landmarks using OpenCV and dlib.  
**Step 5**: Select the forehead as the **Region of Interest (ROI)**.  
**Step 6**: Compute the **mean RGB values** for the forehead region and normalize them.  
**Step 7**: Apply **Independent Component Analysis (ICA)** to extract pulse signals.  
**Step 8**: Perform **Fast Fourier Transform (FFT)** to extract the dominant heart rate frequency.  
**Step 9**: Calculate heart rate using:  
```python
HR = 60 * (number of peaks / time)  # bpm
```
**Step 10**: Plot the extracted **pulse signal**.  
**Step 11**: Calculate Heart Rate Variability (HRV) using **Root Mean Square of Successive Differences (RMSSD)**.  

## Features
- Detects face and extracts the **forehead region** as ROI.
- Computes mean RGB values and normalizes them.
- Applies **Independent Component Analysis (ICA)** to extract pulse signals.
- Performs **Fast Fourier Transform (FFT)** for frequency analysis.
- Calculates **heart rate** using peak detection.
- Computes **Heart Rate Variability (HRV)** using RMSSD.
- Visualizes extracted pulse signals and heart rate trends.

## Dependencies
Ensure you have the following Python libraries installed:
```bash
pip install numpy pandas opencv-python dlib matplotlib scipy scikit-learn
```

## Usage
### 1. Load and Process Video
- Record two videos: **one in normal light** and **one in low light**.
- Read both videos from local storage.
- Detect the face and extract the forehead region.

### 2. Signal Processing
- Normalize the RGB channel values.
- Apply ICA to separate independent sources.
- Use FFT to extract dominant heart rate frequency.

### 3. Heart Rate Calculation
Heart rate is calculated using:
```python
HR = 60 * (number of peaks / time)  # bpm
```

### 4. Visualization
- Plot extracted pulse signals.
- Compare heart rate in different lighting conditions.
```python
plt.plot(y_test_inverse, 'g', label='Actual Heart Rate')
plt.plot(test_predict, 'r', label='Predicted Heart Rate')
plt.legend()
plt.show()
```

## Future Improvements
- Enhance face tracking for more stable ROI selection.
- Experiment with deep learning-based heart rate estimation.
- Improve accuracy under extreme lighting conditions.

## References
1. https://www.osapublishing.org/boe/fulltext.cfm?uri=boe-6-7-2466&id=320343  
2. https://www.osapublishing.org/boe/fulltext.cfm?uri=boe-5-4-1124&id=281701  
3. https://dsp.stackexchange.com/questions/48421/camera-measurement-of-heart-rate-frequency-bias-towards-50-bpm-0-83-hz  
4. https://web.mit.edu/~gari/www/papers/GDCliffordThesis.pdf  
5. https://web.njit.edu/~joelsd/signals/classwork/BME314signalscw12a.pdf  
6. https://www.researchgate.net/publication/308847680_Determination_of_heart_rate_from_photoplethysmogram_using_Fast_Fourier_Transform  
7. https://imotions.com/blog/heart-rate-variability/  
8. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5624990/  
9. https://stackoverflow.com/questions/57647638/how-can-i-detect-the-forehead-region-using-opencv-and-dlib  
10. https://www.pyimagesearch.com/2017/04/10/detect-eyes-nose-lips-jaw-dlib-opencv-python/  
11. https://www.pyimagesearch.com/2021/01/19/crop-image-with-opencv/  
12. https://www.geeksforgeeks.org/detect-the-rgb-color-from-a-webcam-using-python-opencv/  
13. http://people.csail.mit.edu/balakg/cvpr2013_pulsepaper.pdf  
14. https://web.stanford.edu/class/cs231a/prev_projects_2016/finalReport.pdf  
15. https://chrisalbon.com/machine_learning/preprocessing_images/using_mean_color_as_a_feature/  
16. https://ep.liu.se/ecp/129/002/ecp16129002.pdf  
17. https://towardsdatascience.com/independent-component-analysis-ica-in-python-a0ef0db0955e  

## Author
Developed by **Abhishek Srivastava**.

## License
This project is licensed under the MIT License.

