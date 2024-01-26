import numpy as np
import os
import binascii
import matplotlib.pyplot as plt
from scipy.optimize import minimize, root, curve_fit
from scipy.interpolate import interp1d
from copy import deepcopy
import LoadData
ROI_channels = [6, 24]
dataRefFringe = np.zeros([32, 670])
dataIllumination = np.zeros([32, 670])

FileNameArray = []
for Root, Dir, Files in os.walk("Illumination"):
    FileNameArray = Files
for i in range(0, 1):
    FullPathFringe = os.path.join("Illumination", FileNameArray[i])
    dataIllumination += LoadData.LoadLicelData(FullPathFringe)

FileNameArray = []
for Root, Dir, Files in os.walk("Fringe"):
    FileNameArray = Files

#需要条纹数据
def peak_finder(data_array, tolerance):
    """Finds the index of all local maxima inside the data array

    data_array: array of y data
    tolerance: ratio to be fulfilled between the found peak and the mximum of the array"""

    peaks = []
    max_peak = max(data_array)
    for i in range(1, len(data_array) - 1):
        if data_array[i - 1] <= data_array[i] and data_array[i] >= data_array[i + 1] and data_array[i] / max_peak >= tolerance:
            peaks.append(i)
    return peaks

def peak_finder_optimized(data_x, data_y, px_peak, tolerance):
    """Optimzes the peak position using a parabolic fit around the peak

    data_x: x coordinate

    data_y: y coordinate and where the local maxima want to be found

    px_peak: number of pixels before and after the peaks and which are included in order to perform the fit function.

    Returns:
        x,y,peak   Where "peak" is the iterator found by peak_finder()

    """
    peaks = peak_finder(data_y, tolerance)
    print(peaks)
    peaks_optimized = []

    for i in range(0, len(peaks)):

        try:

            peak = peaks[i]
            x = data_x[peak - px_peak:peak + px_peak + 1]
            y = data_y[peak - px_peak:peak + px_peak + 1]

            # print(y)
            x0_guess = data_x[peak]
            # print(x0_guess)
            delta_x = data_x[peak] - data_x[
                peak - 1]  # Assumes constant spacing in order to determine the guess value for the second derivative
            a_guess = np.diff(data_y[peak - 1:peak + 2], n=2) / (delta_x ** 2)
            # print(a_guess)
            b_guess = data_y[peak]
            # print(b_guess)
            # popt,pcov=curve_fit(parabola,x,y,p0=[x0_guess,a_guess,b_guess])
            # print(popt)
            popt, pcov = curve_fit(parabola, x, y, bounds=([x0_guess - 1, -100, 0], [x0_guess + 1, 0, 2000]))
            x_max = popt[0]
            y_max = popt[2]
            peaks_optimized.append([x_max, float(y_max), peak])

        except:

            print("peak_finder_optimized ERROR: Fit routine not possible. Local maximum discarted.")
    #    print(peaks_optimized)
    return peaks_optimized

def FWHM(data_x, data_y, px_peak, tolerance):
    print("data")
    print(data_x)
    print(data_y)
    peaks_optimized = peak_finder_optimized(data_x, data_y, px_peak, tolerance)
    print("data_1")
    print(peaks_optimized)
    return_array = []
    for i in range(0, len(peaks_optimized)):
        try:
            x_max, y_max, peak = peaks_optimized[i]
            upper_index = peak
            lower_index = peak
            print("data")
            print(data_y)
            while (data_y[upper_index] >= 0.45 * y_max):
                upper_index += 1
            while (data_y[lower_index] <= 0.45 * y_max):
                lower_index -= 1
            print("lower_index")
            print(lower_index)
            # Finding the lower point
            print(upper_index)
            x = data_x[lower_index:peak + 1]
            y = data_y[lower_index:peak + 1]
            f = interp1d(x, y, kind='linear')
            sol = root(lambda x: f(x) - 0.5 * y_max, data_x[lower_index + 1])
            print(sol.message)
            x1 = sol.x[0]
            # Finding the upper point
            x = data_x[peak:upper_index + 1]
            y = data_y[peak:upper_index + 1]
            f = interp1d(x, y, kind='linear')
            sol = root(lambda x: f(x) - 0.5 * y_max, data_x[upper_index - 1])
            print(sol.message)
            x2 = sol.x[0]
            FWHM = x2 - x1
            return_array.append([x_max, y_max, FWHM, peak, x1, x2])
        except:
            print("FWHM ERROR: Fit routine not possible. Local maximum discarted.")
            return_array.append([x_max, y_max, None, peak, None, None])
    return return_array

for i in range(0, 1):
    FullPathFringe = os.path.join("Fringe", FileNameArray[i])
    dataRefFringe += LoadData.LoadLicelData(FullPathFringe)
indexRayleigh = 120  # Just for determining FSR
width = 10
dataRayleighFSR = dataRefFringe / dataIllumination
dataRayleighFSR = np.sum(
    dataRayleighFSR[ROI_channels[0]:ROI_channels[1], indexRayleigh - width:indexRayleigh + width + 1], axis=1)
FSR_analysis = FWHM(np.arange(ROI_channels[0], ROI_channels[1]), dataRayleighFSR, 1, 0.7)
FSR_guess = FSR_analysis[1][0] - FSR_analysis[0][0]
FSR = FSR_guess
#需要ROI_channels
xFull = np.arange(ROI_channels[0], ROI_channels[1])
xFull = np.array(xFull, dtype=float)
x0 = xFull[0]
xSorted = deepcopy(xFull)
xSorted[xSorted > (x0 + FSR)] -= FSR  # Translating the second fringe back to a single FSR

dataRayleighSorted = np.array([x for (y, x) in sorted(zip(xSorted, dataRayleigh))])
dataCirrusSorted = np.array([x for (y, x) in sorted(zip(xSorted, dataCirrusCorrected))])
xSorted = np.array(sorted(xSorted))

xExtended = list(xSorted) + list(xSorted + FSR) + list(xSorted + 2 * FSR) + [xSorted[0] + 3 * FSR]
dataCirrusExtended = 3 * list(dataCirrusSorted) + [dataCirrusSorted[0]]
f = interp1d(xExtended, dataCirrusExtended, kind=3)
fineResolution = 1000
xFine = np.linspace(xExtended[0], xExtended[0] + 3 * FSR, 3 * fineResolution + 1)
dataCirrusFine = f(xFine)