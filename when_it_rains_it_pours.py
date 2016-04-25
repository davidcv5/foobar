#!/usr/bin/python


def reduce_peaks(heights, peaks):
    if len(peaks) == 3:
        if heights[peaks[0]] > heights[peaks[1]] < heights[peaks[2]]:
            return peaks[:1] + peaks[2:]
        else:
            return peaks

    if len(peaks) < 3:
        return peaks

    reduced_peaks = [0]
    increase = heights[0] < heights[1]

    for i in range(1, len(peaks)):
        if heights[peaks[i - 1]] < heights[peaks[i]]:
            if increase and heights[reduced_peaks[-1]] > heights[peaks[i]]:
                reduced_peaks[-1] = peaks[i]
            else:
                reduced_peaks.append(peaks[i])
            increase = True
        else:
            if not increase:
                reduced_peaks.append(peaks[i - 1])
            increase = False

    if len(peaks) < len(heights) and not increase:
        reduced_peaks.append(peaks[-1])

    if len(peaks) > len(reduced_peaks):
        return reduce_peaks(heights, reduced_peaks)
    else:
        return reduced_peaks


def answer(heights):
    peaks = reduce_peaks(heights, range(len(heights)))
    if len(peaks) == 0:
        return 0
    total = 0
    for i in range(1, len(peaks)):
        m = min(heights[peaks[i - 1]], heights[peaks[i]])
        for j in range(peaks[i - 1] + 1, peaks[i]):
            total += m - heights[j]

    return total
