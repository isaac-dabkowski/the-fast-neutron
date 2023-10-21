from manim import *

global ALL_ISOTOPES
ALL_ISOTOPES = {
    # Skip H-1 and other extremely exotic low A nuclei, no sense in calculating their binding energies with SEMF
    1: [2, 3], 
    2: [3, 4],
    3: [3, 4, 5, 6],
    4: [5, 6, 7, 8, 9, 10],
    5: [6, 7, 8, 9, 10, 11, 12, 13],
    6: [8, 9, 10, 11, 12, 13, 14, 15],
    7: [10, 11, 12, 13, 14, 15, 16, 17, 18],
    8: [12, 13, 14, 15, 16, 17, 18, 19, 20],
    9: [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    10: [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
    11: [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    12: [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32],
    13: [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36],
    14: [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38],
    15: [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41],
    16: [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45],
    17: [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47],
    18: [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    19: [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53],
    20: [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56],
    21: [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
    22: [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63],
    23: [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65],
    24: [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67],
    25: [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
    26: [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72],
    27: [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75],
    28: [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78],
    29: [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
    30: [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83],
    31: [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86],
    32: [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
    33: [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92],
    34: [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94],
    35: [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97],
    36: [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100],
    37: [71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102],
    38: [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105],
    39: [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108],
    40: [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    41: [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113],
    42: [83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
    43: [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118],
    44: [87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
    45: [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122],
    46: [91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124],
    47: [93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130],
    48: [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132],
    49: [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135],
    50: [99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137],
    51: [103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139],
    52: [105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142],
    53: [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144],
    54: [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147],
    55: [112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151],
    56: [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153],
    57: [117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155],
    58: [119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157],
    59: [121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159],
    60: [124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161],
    61: [126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163],
    62: [128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165],
    63: [130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167],
    64: [134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169],
    65: [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171],
    66: [138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173],
    67: [140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175],
    68: [143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177],
    69: [145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179],
    70: [148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181],
    71: [150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184],
    72: [153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188],
    73: [155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190],
    74: [158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192],
    75: [160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194],
    76: [162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196],
    77: [164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199],
    78: [166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202],
    79: [169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205],
    80: [171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    81: [176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212],
    82: [178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215],
    83: [184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218],
    84: [188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220],
    85: [193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223],
    86: [195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228],
    87: [199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232],
    88: [202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234],
    89: [206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236],
    90: [209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238],
    91: [212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240],
    92: [217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242],
    93: [225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244],
    94: [228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247],
    95: [231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249],
    96: [233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252],
    97: [235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254],
    98: [237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256],
    99: [240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258],
    100: [242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260],
    101: [245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262],
    102: [248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264],
    103: [251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266],
    104: [253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268],
    105: [255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270],
    106: [258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273],
    107: [260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275],
    108: [263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277],
    109: [265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279],
    110: [267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281],
    111: [272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283],
    112: [277, 278, 279, 280, 281, 282, 283, 284, 285],
    113: [283, 284, 285, 286, 287],
    114: [285, 286, 287, 288, 289],
    115: [287, 288, 289, 290, 291],
    116: [289, 290, 291, 292],
    118: [293]
}


def calc_BE_A(Z, N):
    """
    Calculate binding energy per nucleon for a given
    number of protons and neutrons with the SEMF
    """
    # Mass of proton and neutron in amu
    m_p = 1.007276
    m_n = 1.008665
    # MeV per amu
    c_2 = 931.494
    # SEMF coefficients
    a_V = 15.835
    a_S = 18.33
    a_C = 0.714
    a_A = 23.2
    a_P = 11.2
    # Atomic number
    A = Z + N
    # Initialize bindign energy
    BE = 0
    # Volume term
    vol = a_V * A
    BE += vol
    # Surface term
    surf = a_S * A ** (2 / 3)
    BE -= surf
    # Coulomb term
    col = a_C * (Z * (Z - 1)) / A ** (1 / 3)
    BE -= col
    # Asymmetry term
    asym = a_A * (A - 2 * Z) ** 2 / A
    BE -= asym
    # Pairing term
    if Z % 2 == 0 and N % 2 == 0:
        delta = 1
    elif Z % 2 == 1 and N % 2 == 1:
        delta = -1
    else:
        delta = 0
    pair = delta * a_P / A ** (1 / 2)
    BE += pair
    return BE / A


def create_BE_data(constrain_to_real_isotopes=False, A_max=250):
    """
    Generates BE/A data for many different nuclides.
    """
    BE_A = dict()
    # Loop over all mass numbers
    for A in range(2, A_max + 1):
        # Loop over all possible combinations of
        # neutrons and protons for the given mass number
        for Z in range(1, A + 1):
            N = A - Z
            be_per_a = calc_BE_A(Z=Z, N=N)
            # Cutoff to make pretty chart
            if constrain_to_real_isotopes is False:
                include = True if be_per_a > (4/A_max)*A + 1.8 else False
            # Cutoff to not include non physical isotopes
            else:
                include = True if Z in ALL_ISOTOPES and A in ALL_ISOTOPES[Z] else False
            if include is True:
                if be_per_a > 0:
                    if A not in BE_A:
                        BE_A[A] = list()
                    BE_A[A].append((Z, be_per_a))
    return BE_A


class BindingEnergyTitleCard(Scene):
    def construct(self):
        section_title = Tex("Nuclear binding energy and the semi-empirical mass formula")
        self.wait()
        self.play(Write(section_title))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class MassDefect(Scene):
    def construct(self):
        # Helper function to make protons
        def proton():
            proton = Circle(
                radius=0.35,
                color=RED,
            ).set_fill("#7d3129", opacity=1.0)
            return proton

        # Helper function to make neutrons
        def neutron():
            neutron = Circle(
                radius=0.35,
                color=GREEN,
            ).set_fill("#416033", opacity=1.0)
            return neutron

        # Start with nucleons apart from one another
        he4_p1 = proton()
        he4_p2 = proton()
        he4_n1 = neutron()
        he4_n2 = neutron()
        he4 = VGroup(he4_p1, he4_p2, he4_n1, he4_n2).arrange(RIGHT, buff=LARGE_BUFF)
        self.play(GrowFromCenter(he4))
        self.wait()

        # Arrange into nucleus
        self.play(
            he4_p1.animate.move_to([-he4_p1.radius, he4_p1.radius, 0]),
            he4_p2.animate.move_to([he4_p1.radius, -he4_p1.radius, 0]),
            he4_n1.animate.move_to([he4_p1.radius, he4_p1.radius, 0]),
            he4_n2.animate.move_to([-he4_p1.radius, -he4_p1.radius, 0])
        )
        self.play(he4.animate.rotate(np.pi/4))
        self.wait()

        # Predicted mass of nucleus
        tex = Tex(r"\underline{What would you expect the mass of the $^4$He nucleus to be?}").to_edge(UP)
        self.play(Write(tex))
        self.wait()
        self.play(he4.animate.to_edge(LEFT))
        self.wait()
        mp_mn = Tex(r"$m_p = 1.007278$ amu, $m_n = 1.008665$ amu").next_to(tex, DOWN)
        amu_kg = Tex(r"$1\text{ amu} = 1.66054\text{e-}27\text{ kg}$").next_to(mp_mn, DOWN)
        he_mass_calc = VGroup(
            Tex(r"$M\left(^4\text{He}\right)=Z\cdot m_p + (A-Z)\cdot m_n$"),
            Tex(r"$M\left(^4\text{He}\right)=2\cdot m_p + 2\cdot m_n$"),
            Tex(r"$M\left(^4\text{He}\right)=2\cdot (1.007278\text{ u}) + 2\cdot(1.008665\text{ u})$"),
            Tex(r"$M\left(^4\text{He}\right)=4.031883\text{ u}$")
        ).arrange(DOWN, buff=MED_SMALL_BUFF, center=False, aligned_edge=LEFT).next_to(amu_kg, DOWN * 3).shift(RIGHT)
        self.play(Write(mp_mn))
        self.wait()
        self.play(Write(amu_kg))
        self.wait()
        for m in he_mass_calc:
            self.play(Write(m))
            self.wait()
        predicted_mass = he_mass_calc[-1].copy()
        self.play(
            FadeOut(he_mass_calc),
            FadeOut(mp_mn),
            FadeOut(amu_kg),
            Transform(
                predicted_mass,
                Tex("Predicted mass = 4.031883 u").next_to(tex, DOWN * 2)
            )
        )
        self.wait()

        # Reveal actual mass and mass defect
        actual_mass = Tex("Actual mass = 4.001506 u").next_to(predicted_mass, DOWN * 2).align_to(predicted_mass, RIGHT)
        self.play(Write(actual_mass))
        self.wait()
        mass_defect = Tex(r"$\Delta$m = 0.030377 u").next_to(actual_mass, DOWN * 2).align_to(actual_mass, RIGHT)
        self.play(Write(mass_defect))
        self.wait()
        self.play(Transform(mass_defect, Tex("Mass defect = 0.030377 u").next_to(actual_mass, DOWN * 2).align_to(actual_mass, RIGHT)))
        self.wait()

        # Discuss connection between mass defect and binding energy
        md_be =  VGroup(
            Tex("The nucleus is in a stable"),
            Tex("configuration, it would take"),
            Tex("energy input to pull it apart.")
        ).arrange(DOWN, buff=MED_SMALL_BUFF).next_to(mass_defect, DOWN).to_edge(DOWN)
        self.play(Write(md_be))
        self.wait()
        self.play(FadeOut(predicted_mass), FadeOut(actual_mass), mass_defect.animate.next_to(tex, DOWN))
        self.wait()
        einstein_pic = ImageMobject("assets/Einstein.jpg").scale(0.15).shift(DOWN * 0.5)
        einstein_border = SurroundingRectangle(
            einstein_pic,
            color=YELLOW,
            buff=0.0
        )
        self.play(FadeOut(md_be), FadeIn(einstein_pic), FadeIn(einstein_border))
        self.wait()
        be = Tex(r"$E=mc^{2}$").next_to(einstein_border, DOWN)
        self.play(Write(be))
        self.wait()
        self.play(FadeOut(einstein_pic), FadeOut(einstein_border))
        self.wait()
        self.play(Transform(be, Tex(r"$\text{BE}=\Delta m \cdot c^2$").next_to(mass_defect, DOWN * 3.0)))
        self.wait()
        self.play(Transform(be, Tex(r"$\text{BE}=\Delta m \cdot c^2=28.296\text{ MeV}$").next_to(mass_defect, DOWN * 3.0)))
        self.wait()

        # Hint at SEMF
        self.play(FadeOut(mass_defect), FadeOut(be))
        self.wait()
        semf = Tex(r"$M\left(^A_ZX\right)=Z\cdot m_p + (A-Z)\cdot m_n$").shift(RIGHT)
        self.play(Write(semf))
        self.wait()
        wrong_line = Line(semf.get_left(), semf.get_right(), color=RED)
        self.play(
            Transform(semf, Tex(r"$M\left(^A_ZX\right)=Z\cdot m_p + (A-Z)\cdot m_n$", color=RED).shift(RIGHT)),
            Create(wrong_line)
        )
        self.wait()
        self.play(
            Transform(semf, Tex(r"$M\left(^A_ZX\right)=Z\cdot m_p + (A-Z)\cdot m_n - \Delta m$").shift(RIGHT)),
            FadeOut(wrong_line)
        )
        self.wait()
        self.play(Transform(semf, Tex(r"$M\left(^A_ZX\right)=Z\cdot m_p + (A-Z)\cdot m_n - \frac{\text{BE(A, Z)}}{c^2}$").shift(RIGHT)))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class SEMFAnimation(Scene):
    def construct(self):
        # Helper function to make protons
        def proton():
            proton = Circle(
                radius=0.5,
                color=RED,
            ).set_fill("#7d3129", opacity=1.0)
            return proton

        # Helper function to make neutrons
        def neutron():
            neutron = Circle(
                radius=0.5,
                color=GREEN,
            ).set_fill("#416033", opacity=1.0)
            return neutron

        # Display section title and equation
        tex = Tex(r"\underline{The semi-empirical mass formula}").to_edge(UP)
        self.play(Write(tex))
        self.wait()
        semf = Tex(r"$M\left(^A_ZX\right)=Z\cdot m_p + (A-Z)\cdot m_n - \frac{\text{BE(A, Z)}}{c^2}$")
        self.play(Write(semf))
        self.wait()
        self.play(FadeOut(semf))
        self.wait()

        # Display binding enegy eq
        be = MathTex("\\text{BE}(A, Z)=", "a_VA", "-", "a_SA^{2/3}", "-", "a_c\\frac{Z(Z-1)}{A^{1/3}}", "-", "a_A\\frac{(A-2Z)^2}{A}", "+", "\\delta(A, Z)a_PA^{-1/2}", font_size=38)
        self.play(Write(be))
        self.wait()
        self.play(be.animate.next_to(tex, DOWN * 1.5))
        self.wait()

        # Display a key real quick
        symkey = VGroup(
            Tex(r"$A=\text{Mass number (\# protons + \# neutrons)}$"),
            Tex(r"$Z=\text{Atomic number (\# protons)}$"),
            Tex(r"$a_V, a_C, a_A, a_P=\text{Experimentally determined coefficients}$")
        ).arrange(DOWN, buff=MED_LARGE_BUFF, center=False, aligned_edge=LEFT).shift(UP * 0.5 + LEFT * 0.5)
        self.play(Write(symkey))
        self.wait()
        self.play(FadeOut(symkey))
        self.wait()

        # Draw a line across screen
        line = Line([-10, be.get_bottom()[1] - 0.25, 0], [10, be.get_bottom()[1] - 0.25, 0])
        self.play(Create(line))
        self.wait()

        # Make a nucleus
        nuc = ImageMobject("assets/random_nucleus.png").to_edge(RIGHT).shift(LEFT * 0.5 + DOWN)
        self.play(
            GrowFromCenter(nuc)
        )
        self.wait()

        # Volume term
        volframe = SurroundingRectangle(be[1], buff = .1)
        termname = Tex(r"\underline{\textit{Volume term}}").next_to(be, DOWN * 3.0).shift(LEFT * 3)
        termtex = Tex(r"$a_VA$").next_to(termname, DOWN)
        termdesc = Tex(r"Decribes strong force\\between neighboring nucleons").next_to(termtex, DOWN * 2)
        arrows = VGroup(
            Arrow(start=[5.05, -0.75, 0], end=[4.9, -1.35, 0], buff=0.0),
            Arrow(start=[5.05, -0.75, 0], end=[5.5, -1.25, 0], buff=0.0),
            Arrow(start=[5.05, -0.75, 0], end=[5.7, -0.65, 0], buff=0.0),
            Arrow(start=[5.05, -0.75, 0], end=[5.25, -0.15, 0], buff=0.0),
            Arrow(start=[5.05, -0.75, 0], end=[4.63, -0.08, 0], buff=0.0),
            Arrow(start=[5.05, -0.75, 0], end=[4.4, -0.75, 0], buff=0.0),
        )
        coefftex = Tex(r"$a_V\approx15.835\text{ MeV}$").next_to(termdesc, DOWN * 2)
        term_grp = VGroup(
            termname,
            termtex,
            termdesc,
            arrows,
            coefftex
        )
        self.play(Create(volframe))
        self.wait()
        self.play(Write(termname))
        self.wait()
        self.play(Write(termtex))
        self.wait()
        self.play(Write(termdesc))
        self.wait()
        self.play(Create(arrows))
        self.wait()
        self.play(Write(coefftex))
        self.wait()
        self.play(FadeOut(term_grp))
        self.wait()

        # Surface term
        surfframe = SurroundingRectangle(be[3], buff=.1)
        self.play(ReplacementTransform(volframe, surfframe))
        termname = Tex(r"\underline{\textit{Surface term}}").next_to(be, DOWN * 3.0).shift(LEFT * 3)
        termtex = Tex(r"$a_SA^{2/3}$").next_to(termname, DOWN)
        termdesc = Tex(r"Decribes how nucleons on nucleus's\\surface have fewer neighbors").next_to(termtex, DOWN * 2)
        coefftex = Tex(r"$a_S\approx18.33\text{ MeV}$").next_to(termdesc, DOWN * 2)
        arrows = VGroup(
            Arrow(start=[5.7, -0.65, 0], end=[5.05, -0.75, 0], buff=0.0),
            Arrow(start=[5.7, -0.65, 0], end=[5.5, -1.25, 0], buff=0.0),
            Arrow(start=[5.7, -0.65, 0], end=[5.25, -0.15, 0], buff=0.0),
        )
        term_grp = VGroup(
            termname,
            termtex,
            termdesc,
            arrows,
            coefftex
        )
        self.play(Write(termname))
        self.wait()
        self.play(Write(termtex))
        self.wait()
        self.play(Write(termdesc))
        self.wait()
        self.play(Create(arrows))
        self.wait()
        self.play(Write(coefftex))
        self.wait()
        self.play(FadeOut(term_grp))
        self.wait()

        # Coulomb term
        colframe = SurroundingRectangle(be[5], buff=.1)
        self.play(ReplacementTransform(surfframe, colframe))
        termname = Tex(r"\underline{\textit{Coulomb term}}").next_to(be, DOWN * 3.0).shift(LEFT * 3)
        termtex = Tex(r"$a_C\frac{Z(Z-1)}{A^{1/3}}$").next_to(termname, DOWN)
        termdesc = Tex(r"Decribes how protons repel\\each other").next_to(termtex, DOWN * 2)
        coefftex = Tex(r"$a_C\approx0.714\text{ MeV}$").next_to(termdesc, DOWN * 2)
        arrows = VGroup(
            Arrow(start=[4.92, -1.3, 0], end=[5.7, -0.65, 0], buff=0.0, stroke_width=4, max_tip_length_to_length_ratio=0.17),
            Arrow(start=[4.92, -1.3, 0], end=[5.25, -0.15, 0], buff=0.0, stroke_width=4, max_tip_length_to_length_ratio=0.15),
            Arrow(start=[4.92, -1.3, 0], end=[4.07, -0.22, 0], buff=0.0, stroke_width=4, max_tip_length_to_length_ratio=0.13),
            Arrow(start=[4.92, -1.3, 0], end=[3.75, -0.8, 0], buff=0.0, stroke_width=4, max_tip_length_to_length_ratio=0.13),
            Arrow(start=[4.92, -1.3, 0], end=[4.65, -2.0, 0], buff=0.0, stroke_width=4, max_tip_length_to_length_ratio=0.2),
            Arrow(start=[4.92, -1.3, 0], end=[5.8, -1.8, 0], buff=0.0, stroke_width=4, max_tip_length_to_length_ratio=0.17)
        )
        term_grp = VGroup(
            termname,
            termtex,
            termdesc,
            arrows,
            coefftex
        )
        self.play(Write(termname))
        self.wait()
        self.play(Write(termtex))
        self.wait()
        self.play(Write(termdesc))
        self.wait()
        self.play(Create(arrows))
        self.wait()
        self.play(Write(coefftex))
        self.wait()
        self.play(FadeOut(term_grp), FadeOut(nuc))
        self.wait()

        # Asymmetry term
        asymframe = SurroundingRectangle(be[7], buff=.1)
        self.play(ReplacementTransform(colframe, asymframe))
        termname = Tex(r"\underline{\textit{Asymmetry term}}").next_to(be, DOWN * 3.0)
        termtex = Tex(r"$a_A\frac{(A-2Z)^2}{A}$").next_to(termname, DOWN)
        termdesc = Tex(r"Decribes how protons and neutrons\\fill quantum states more efficiently\\when they come in equal numbers").next_to(termtex, DOWN * 2)
        coefftex = Tex(r"$a_A\approx23.2\text{ MeV}$").next_to(termdesc, DOWN * 2)
        term_grp = VGroup(
            termname,
            termtex,
            termdesc,
            coefftex
        )
        self.play(Write(termname))
        self.wait()
        self.play(Write(termtex))
        self.wait()
        self.play(Write(termdesc))
        self.wait()
        self.play(Write(coefftex))
        self.wait()
        self.play(FadeOut(term_grp))
        self.wait()

        # Pairing term
        pairframe = SurroundingRectangle(be[9], buff=.1)
        self.play(ReplacementTransform(asymframe, pairframe))
        termname = Tex(r"\underline{\textit{Pairing term}}").next_to(be, DOWN * 3.0).shift(LEFT * 3.5)
        termtex = Tex(r"$\delta(A, Z)a_PA^{-1/2}$").next_to(termname, DOWN)
        termdesc = Tex(r"Decribes how pairs of like-\\nucleons are energetically\\favorable due to spin-coupling").next_to(termtex, DOWN * 2)
        coefftex = Tex(r"$a_P\approx11.2\text{ MeV}$").next_to(termdesc, DOWN * 2)
        term_grp = VGroup(
            termname,
            termtex,
            termdesc,
            coefftex
        )
        delta_font_size = 37
        deltatex = Tex(r"$\delta(A,Z)=$", font_size=delta_font_size).shift(DOWN * 1.0)
        deltaterms=VGroup(
            Tex("+1 if even $N_p$, even $N_n$", font_size=delta_font_size),
            Tex("-1 if odd $N_p$, odd $N_n$", font_size=delta_font_size),
            Tex("0 if otherwise", font_size=delta_font_size),
        ).arrange(DOWN, buff=MED_LARGE_BUFF, center=False, aligned_edge=LEFT).next_to(deltatex, RIGHT * 2.5)
        deltadesc = VGroup(
            deltatex,
            deltaterms
        ).to_edge(RIGHT).shift(RIGHT * 0.35)
        deltabrace = Brace(Line(deltaterms[0].get_corner(UL), deltaterms[-1].get_corner(DL)), LEFT).next_to(deltaterms, LEFT)
        self.play(Write(termname))
        self.wait()
        self.play(Write(termtex))
        self.wait()
        self.play(Write(termdesc))
        self.wait()
        self.play(Create(deltadesc), FadeIn(deltabrace))
        self.wait()
        self.play(Write(coefftex))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class SEMFPlots(Scene):
    def construct(self):
        # Generate SEMF data
        data = create_BE_data()

        # Show that Iron is the most stable for 56 nucleons
        fe_question = Tex(r"\underline{For 56 nucleons, what number of protons will maximize binding energy?}", font_size=40).to_edge(UP)
        fe_data = data[56]
        fe_z = [d[0] for d in fe_data]
        fe_be = [56 * d[1] for d in fe_data]
        fe_data = [*zip(fe_z, fe_be)]
        fe_ax = Axes(
            x_range=[10, 40, 5],
            y_range=[150, 600, 50],
            tips=False,
            y_axis_config={"include_numbers": True, "font_size": 30},
            x_axis_config={"include_numbers": True,  "font_size": 30},
        ).scale(0.8)
        fe_ax_x_label = fe_ax.get_x_axis_label(Tex("Atomic number", font_size = 40), edge=DOWN, buff=0.1).next_to(fe_ax.coords_to_point(sum(fe_ax.x_range[0:2]) / 2, fe_ax.y_range[0]), DOWN * 2)
        fe_ax_y_label = fe_ax.get_y_axis_label(Tex("BE (MeV)", font_size=40)).next_to(fe_ax.coords_to_point(fe_ax.x_range[0], sum(fe_ax.y_range[0:2]) / 2), LEFT).rotate(np.pi / 2)
        fe_graph = fe_ax.plot_line_graph(
            x_values=fe_z,
            y_values=fe_be,
            line_color=YELLOW,
            add_vertex_dots=False,
            stroke_width=2,
        )
        fe_dot = Dot(fe_ax.coords_to_point(*max(fe_data, key=lambda x: x[1])))
        fe_line = DashedLine(start=fe_dot.get_center(), end=[fe_dot.get_x(), fe_ax.coords_to_point(0, fe_ax.y_range[0])[1], 0])
        fe_tex = Tex("$^{56}$Fe").next_to(fe_dot, UP)
        self.play(Write(fe_question))
        self.wait()
        self.play(Create(fe_ax), FadeIn(fe_ax_x_label), FadeIn(fe_ax_y_label))
        self.wait()
        self.play(DrawBorderThenFill(fe_graph))
        self.wait()
        self.play(GrowFromCenter(fe_dot), Create(fe_line), Write(fe_tex))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != fe_question])
        self.wait()

        # Show that Uranium is the most stable for 238
        u_question = Tex(r"\underline{For 238 nucleons, what number of protons will maximize binding energy?}", font_size=40).to_edge(UP)
        u_data = data[238]
        u_z = [d[0] for d in u_data]
        u_be = [238 * d[1] for d in u_data]
        u_data = [*zip(u_z, u_be)]
        u_ax = Axes(
            x_range=[60, 125, 10],
            y_range=[1350, 1850, 50],
            tips=False,
            y_axis_config={"include_numbers": True, "font_size": 30},
            x_axis_config={"include_numbers": True,  "font_size": 30},
        ).scale(0.8)
        u_ax_x_label = u_ax.get_x_axis_label(Tex("Atomic number", font_size = 40), edge=DOWN, buff=0.1).next_to(u_ax.coords_to_point(sum(u_ax.x_range[0:2]) / 2, u_ax.y_range[0]), DOWN * 2)
        u_ax_y_label = u_ax.get_y_axis_label(Tex("BE (MeV)", font_size=40)).next_to(u_ax.coords_to_point(u_ax.x_range[0], sum(u_ax.y_range[0:2]) / 2), LEFT).rotate(np.pi / 2)
        u_graph = u_ax.plot_line_graph(
            x_values=u_z,
            y_values=u_be,
            line_color=YELLOW,
            add_vertex_dots=False,
            stroke_width=2,
        )
        u_dot = Dot(u_ax.coords_to_point(*max(u_data, key=lambda x: x[1])))
        u_line = DashedLine(start=u_dot.get_center(), end=[u_dot.get_x(), u_ax.coords_to_point(0, u_ax.y_range[0])[1], 0])
        u_tex = Tex("$^{238}$U").next_to(u_dot, UP)
        self.play(Transform(fe_question, u_question))
        self.wait()
        self.play(Create(u_ax), FadeIn(u_ax_x_label), FadeIn(u_ax_y_label))
        self.wait()
        self.play(DrawBorderThenFill(u_graph))
        self.wait()
        self.play(GrowFromCenter(u_dot), Create(u_line), Write(u_tex))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != fe_question])
        self.wait()


class PlotAllIsotopes(ThreeDScene):
        def construct(self):
            phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
            data = create_BE_data(constrain_to_real_isotopes=False)
            real_isotope_data = create_BE_data(constrain_to_real_isotopes=True, A_max=298)
            # Make axes
            ax = ThreeDAxes(
                x_range=[0, 250, 50],
                y_range=[0, 150, 25],
                z_range=[0, 10, 2],
                x_length=5,
                y_length=6,
                z_length=4,
                tips=False,
                x_axis_config={"include_numbers": True,  "font_size": 30},
                y_axis_config={"include_numbers": True, "font_size": 30, "numbers_to_exclude": [150]},
                z_axis_config={"include_numbers": True,  "font_size": 30}
            )
            # Fix x label orientations
            for label in ax.x_axis.numbers:
                self.camera.add_fixed_orientation_mobjects(label)
            # Add x axis label
            ax_x_label = ax.get_x_axis_label(Tex("Mass number", font_size = 40)).next_to(ax.coords_to_point(sum(ax.x_range[0:2]) / 2, ax.y_range[0]), DOWN * 7.0)
            self.camera.add_fixed_orientation_mobjects(ax_x_label)
            # Fix y label orientations
            for label in ax.y_axis.numbers:
                self.camera.add_fixed_orientation_mobjects(label)
            # Add y axis label
            ax_y_label = ax.get_x_axis_label(Tex("Atomic number", font_size=40)).next_to(ax.coords_to_point(ax.x_range[0], sum(ax.y_range[0:2]) / 2), LEFT * 2.5)
            self.camera.add_fixed_orientation_mobjects(ax_y_label)
            # Fix z labels
            for label in ax.z_axis.numbers:
                label.rotate(PI, ax.z_axis.get_unit_vector()).rotate(PI/2, ax.y_axis.get_unit_vector())
                self.camera.add_fixed_orientation_mobjects(label)
            # Add z axis label
            ax_z_label = Tex(r"$\frac{\text{BE}}{A}$ (MeV)", font_size=40).next_to(ax.coords_to_point(ax.x_range[0], ax.y_range[1], sum(ax.z_range[0:2]) / 2), LEFT * 7.0)
            self.camera.add_fixed_orientation_mobjects(ax_z_label)
            # Make the z axis transparent, and then use a dummy axis which is shifted in the y direction
            dummmy_ax = ax.z_axis.copy().shift(UP * ax.y_length)
            ax.z_axis.set_opacity(0.0)
            # Show the X/Y plane
            xy_plane = NumberPlane(
                x_range=[0, ax.x_range[1] / ax.x_range[2] + 1.0],
                y_range=[0, (ax.y_range[1] / ax.y_range[2]) - 1.0],
                background_line_style={
                    "stroke_color": GREY,
                    "stroke_width": 1,
                    "stroke_opacity": 0.5,
                },
            ).rotate(PI, axis=ax.y_axis.get_unit_vector()).rotate(PI/2, axis=ax.z_axis.get_unit_vector())
            xy_plane.x_axis.set_opacity(0.0)
            xy_plane.y_axis.set_opacity(0.0)
            xy_plane.move_to(ax.coords_to_point(ax.x_range[1]/2, ax.y_range[1]/2, 0))
            axes = VGroup(
                ax,
                dummmy_ax,
                xy_plane,
                ax_x_label,
                ax_y_label,
                ax_z_label
            )
            # Reposition camera
            self.set_camera_orientation(
                phi=65 * DEGREES,
                theta=215 * DEGREES,
                frame_center=[0, 0, 1.2],
                focal_distance=1e6
            )
            self.play(
                Create(ax),
                Create(dummmy_ax),
                Create(xy_plane)
            )
            self.wait()
            self.play(Create(ax_x_label))
            self.wait()
            self.play(Create(ax_y_label))
            self.wait()
            self.play(Create(ax_z_label))
            self.wait()

            # Plot all isotopes
            iso_plots = VGroup()
            other_iso_plots = VGroup()
            for A in data:
                x = [A] * len(data[A])
                y = [d[0] for d in data[A]]
                z = [d[1] for d in data[A]]
                graph = ax.plot_line_graph(
                    x_values=x,
                    y_values=y,
                    z_values=z,
                    add_vertex_dots=False,
                    stroke_width=0.7,
                )
                if A % 10 == 0:
                    iso_plots.add(graph)
                else:
                    other_iso_plots.add(graph)
            iso_plots.set_color_by_gradient(PINK, BLUE, YELLOW)
            other_iso_plots.set_color_by_gradient(PINK, BLUE, YELLOW)
            self.play(Create(iso_plots))
            self.wait()
            self.begin_ambient_camera_rotation(rate=0.07, about='theta')
            self.wait(10)

            # Scan over the entire range
            highlight = iso_plots[-1].copy().set_color(WHITE).set_stroke(width=2.0)
            self.play(FadeIn(highlight))
            self.wait()
            animations = list()
            for _, curve in reversed(list(enumerate(iso_plots[6:]))):
                new_highlight = curve.copy().set_color(WHITE).set_stroke(width=2.0)
                animations.append(Transform(highlight, new_highlight, rate_func=linear))
            self.play(ChangeSpeed(AnimationGroup(*animations), speedinfo={0.0: 0.1, 1: 0.1}, rate_func=linear))
            animations = list()
            for _, curve in reversed(list(enumerate(iso_plots[2:-6]))):
                new_highlight = curve.copy().set_color(WHITE).set_stroke(width=2.0)
                animations.append(Transform(highlight, new_highlight, rate_func=linear))
            self.play(ChangeSpeed(AnimationGroup(*animations), speedinfo={0.0: 0.5, 1: 0.5}, rate_func=linear))
            self.play(ChangeSpeed(AnimationGroup(*[Transform(highlight, iso_plots[1].copy().set_color(WHITE).set_stroke(width=2.0), rate_func=linear)]), speedinfo={0.0: 1.0, 1: 1.0}, rate_func=linear))
            self.play(ChangeSpeed(AnimationGroup(*[Transform(highlight, iso_plots[0].copy().set_color(WHITE).set_stroke(width=2.0), rate_func=linear)]), speedinfo={0.0: 1.0, 1: 1.0}, rate_func=linear))
            self.wait()
            self.play(FadeOut(highlight))
            self.wait()

            # Highlight iron
            fe_x = [56] * len(data[56])
            fe_y = [d[0] for d in data[56]]
            fe_z = [d[1] for d in data[56]]
            fe_graph = ax.plot_line_graph(
                x_values=fe_x,
                y_values=fe_y,
                z_values=fe_z,
                add_vertex_dots=False,
                stroke_width=2,
                stroke_color=WHITE
            )
            fe_dot = Sphere(radius=0.08, resolution=18).set_color(RED)
            fe_dot.move_to(ax.coords_to_point(fe_x[0], fe_y[fe_z.index(max(fe_z))], max(fe_z)))
            self.play(FadeIn(fe_graph))
            self.wait(3)
            self.play(GrowFromCenter(fe_dot))
            self.wait(3)
            self.play(
                FadeOut(fe_graph),
                FadeOut(fe_dot)
            )
            self.wait(2)

            # Highlight uranium
            u_x = [238] * len(data[238])
            u_y = [d[0] for d in data[238]]
            u_z = [d[1] for d in data[238]]
            u_graph = ax.plot_line_graph(
                x_values=u_x,
                y_values=u_y,
                z_values=u_z,
                add_vertex_dots=False,
                stroke_width=2,
                stroke_color=WHITE
            )
            u_dot = Sphere(radius=0.08, resolution=18).set_color(RED)
            u_dot.move_to(ax.coords_to_point(u_x[0], u_y[u_z.index(max(u_z))], max(u_z)))
            self.play(FadeIn(u_graph))
            self.wait(3)
            self.play(GrowFromCenter(u_dot))
            self.wait(2)
            self.play(
                FadeOut(u_graph),
                FadeOut(u_dot)
            )
            self.wait()

            # Draw line of max BE / A
            max_x = [*data]
            max_y = list()
            max_z = list()
            for A in data:
                y = [d[0] for d in data[A]]
                z = [d[1] for d in data[A]]
                max_y.append(
                    y[z.index(max(z))]
                )
                max_z.append(
                    max(z)
                )
            self.play(Create(other_iso_plots))
            self.wait(5)
            max_graph = ax.plot_line_graph(
                x_values=max_x,
                y_values=max_y,
                z_values=max_z,
                add_vertex_dots=False,
                stroke_width=3,
                stroke_color=YELLOW
            )
            self.stop_ambient_camera_rotation()
            self.play(
                phi.animate.set_value(50 * DEGREES),
                theta.animate.set_value(220 * DEGREES),
                run_time=3.0
            )
            self.wait()
            self.play(Create(max_graph), run_time=5)
            self.wait()

            # Constrain to real isotopes
            real_iso_plots = VGroup()
            for A in real_isotope_data:
                x = [A] * len(real_isotope_data[A])
                y = [d[0] for d in real_isotope_data[A]]
                z = [d[1] for d in real_isotope_data[A]]
                graph = ax.plot_line_graph(
                    x_values=x,
                    y_values=y,
                    z_values=z,
                    add_vertex_dots=False,
                    stroke_width=0.8,
                )
                real_iso_plots.add(graph)
            real_iso_plots.set_color_by_gradient(PINK, BLUE, YELLOW)
            self.play(
                FadeOut(iso_plots),
                FadeOut(other_iso_plots)
            )
            self.wait()
            self.play(Create(real_iso_plots), run_time=2.0)
            self.wait()
            self.play(
                FadeOut(ax_z_label),
                phi.animate.set_value(0 * DEGREES),
                theta.animate.set_value(270 * DEGREES),
                ax_x_label.animate.shift(UP * 1.2),
                run_time=2.5
            )
            self.wait()

            # Pivot to reveal BE/A plot
            cheater_section = ax.plot_line_graph(
                x_values=[4, 3, 2],
                y_values=[2, 1, 1],
                z_values=[5.46, 2.6, 1.112],
                add_vertex_dots=False,
                stroke_width=3,
                stroke_color=YELLOW
            )
            self.play(
                FadeOut(real_iso_plots),
                Create(cheater_section)
            )
            self.wait()
            animations = [
                FadeIn(ax_z_label),
                FadeOut(ax.y_axis),
                FadeOut(ax_y_label),
                phi.animate.set_value(90 * DEGREES),
                theta.animate.set_value(270 * DEGREES),
                ax_x_label.animate.shift(IN * 0.75),
                ax_z_label.animate.shift(RIGHT * 0.75)
            ]
            for label in ax.x_axis.numbers:
                animations.append(label.animate.shift(IN * 0.2))
            self.play(AnimationGroup(*animations, lag_ratio=0.0), run_time=5)
            self.play(*[mob.animate.shift(IN) for mob in self.mobjects])
            self.wait()

            # Discuss fission and fusion
            ff_line = DashedLine(
                start=ax.coords_to_point(56, 0, 0),
                end=ax.coords_to_point(56, 0, 10),
                color=WHITE
            )
            self.play(Create(ff_line))
            self.wait()
            fus_arrow = Arrow(
                start=ax.coords_to_point(15, 0, 1),
                end=ax.coords_to_point(25, 0, 7.5)
            )
            fus_arrow.rotate(PI/2, fus_arrow.get_unit_vector())
            fis_arrow = Arrow(
                start=ax.coords_to_point(240, 0, 8.4),
                end=ax.coords_to_point(90, 0, 9.8)
            )
            fis_arrow.rotate(PI/2, fis_arrow.get_unit_vector())
            self.play(Create(fus_arrow))
            self.wait()
            self.play(FadeOut(fus_arrow))
            self.wait()
            self.play(Create(fis_arrow))
            self.wait()
            self.play(FadeOut(fis_arrow))
            self.wait()
            self.play(*[FadeOut(mob) for mob in self.mobjects])
            self.wait()
