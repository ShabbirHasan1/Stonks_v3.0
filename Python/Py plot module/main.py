from plot import *
import matplotlib.pyplot as plt

if __name__ == '__main__':

    var1 = [64.53, 60.23, 55.93, 51.63, 47.32, 43.02, 38.72, 34.42, 30.12, 25.81, 21.51, 17.21, 12.91, 8.60, 4.30, 0.00, 2.12, 4.24, 6.36, 8.48, 10.60, 12.72, 14.84, 16.96, 19.08, 21.20, 23.32, 25.44, 27.56, 29.68, 31.80, 33.92, 36.04, 38.16, 40.28, 42.40, 44.52, 46.64, 48.76, 50.88, 48.04, 45.21, 42.37, 39.53, 36.70, 33.86, 40.75, 47.63, 54.52, 61.41,
]
    var2 = [77.67, 85.48, 93.27, 101.08, 108.88, 116.68, 124.48, 132.28, 124.39, 110.04, 95.69, 81.34, 66.98, 52.62, 38.27, 23.92, 9.57, 2.53, 10.11, 17.70, 25.29, 32.87, 40.46, 48.04, 55.63, 63.22, 70.81, 78.39, 85.97, 93.56, 101.14, 108.73, 116.32, 123.90, 131.49, 139.07, 146.66, 154.25, 161.83, 159.38, 145.07, 130.75, 116.44, 102.12, 87.80, 79.86, 96.13, 112.39, 128.67, 144.94,
]
    var3 = [194.68, 187.20, 179.72, 172.25, 164.78, 157.30, 149.83, 142.35, 134.87, 127.39, 119.92, 112.45, 104.97, 97.50, 90.02, 82.54, 75.07, 67.59, 60.12, 52.64, 45.16, 37.69, 30.22, 22.74, 15.26, 7.79, 0.31, 23.16, 47.32, 71.48, 95.66, 119.82, 143.98, 168.15, 192.31, 216.48, 240.65, 264.81, 288.97, 292.40, 271.33, 250.27, 229.20, 208.13, 187.06, 173.72, 189.77, 205.83, 221.87, 237.92,
]
########################
#
#     varA1 = [13.68, 20.13, 26.57, 33.02, 39.46, 45.91, 41.32, 36.73, 32.14, 27.55, 22.95, 18.36, 13.77, 9.18, 4.59, 0.00
# ]
#
#     varA2 = [20.13, 26.57, 33.02, 39.46, 45.91, 41.32, 36.73, 32.14, 27.55, 22.95, 18.36, 13.77, 9.18, 4.59, 0.00, 4.17,
# ]
#
#     varA3 = [26.57, 33.02, 39.46, 45.91, 41.32, 36.73, 32.14, 27.55, 22.95, 18.36, 13.77, 9.18, 4.59, 0.00, 4.17, 8.33,
# ]
########################
    # varB1 = [0.00, 4.60, 9.19, 13.78, 18.38, 22.97, 27.57, 32.16, 36.75, 41.35, 45.94, 50.54, 55.13, 59.73, 64.32, 68.92, 73.51, 78.10, 82.70, 83.58,]

    # varB2 = [174.30, 157.97, 141.63, 125.28, 108.94, 92.60, 76.26, 59.92, 43.58, 27.24, 10.90, 5.52, 22.06, 38.61, 55.16, 71.71, 88.25, 104.80, 107.53, 103.35]
    #
    # varB3 = [152.52, 136.18, 119.84, 103.49, 87.15, 70.81, 54.47, 38.13, 21.79, 5.45, 11.03, 27.58, 44.12, 60.67, 77.22, 93.77, 110.31, 106.13, 101.96, 97.77]

    plt.figure('var1')
    plt.plot(var1)

    plt.figure('var2')
    plt.plot(var2)

    plt.figure('var3')
    plt.plot(var3)

    #######################
    # plt.figure('varA1')
    # plt.plot(varA1)
    #
    # plt.figure('varA2')
    # plt.plot(varA2)
    #
    # plt.figure('varA3')
    # plt.plot(varA3)

    ######################
    # plt.figure('varB1')
    # plt.plot(varB1)

    # plt.figure('varB2')
    # plt.plot(varB2)
    #
    # plt.figure('varB3')
    # plt.plot(varB3)


    plt.show()
