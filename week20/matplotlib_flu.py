import matplotlib.pyplot as plot

areas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
         58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
         86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
         111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132,
         133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154,
         155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176,
         177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198,
         199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220,
         221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242,
         243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264,
         265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286,
         287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308,
         309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330,
         331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352,
         353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374,
         375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396,
         397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418,
         419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440,
         441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462,
         463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484,
         485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506,
         507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528,
         529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550,
         551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572,
         573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594,
         595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616,
         617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638,
         639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660,
         661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682,
         683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704,
         705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726,
         727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748,
         749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770,
         771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792,
         793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814,
         815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836,
         837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858,
         859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880,
         881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902,
         903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924,
         925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946,
         947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968,
         969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990,
         991, 992, 993, 994, 995, 996, 997, 998, 999]

amounts = [0, 49, 55, 54, 70, 77, 37, 43, 94, 92, 54, 64, 51, 53, 44, 53, 8, 45, 45, 80, 21, 42, 51, 72, 94, 29, 83,
               3, 12, 17, 73, 49, 61, 92, 80, 72, 48, 25, 56, 73, 9, 34, 5, 4, 78, 89, 95, 78, 30, 5, 6, 53, 81, 63, 65,
               17, 91, 29, 24, 21, 17, 87, 75, 63, 84, 59, 35, 80, 63, 94, 44, 63, 3, 15, 58, 95, 17, 65, 51, 32, 28,
               22, 24, 46, 34, 55, 6, 92, 63, 54, 80, 84, 43, 29, 59, 98, 18, 94, 71, 58, 39, 71, 25, 92, 40, 35, 32, 5,
               92, 30, 2, 77, 49, 12, 61, 67, 91, 48, 87, 1, 80, 45, 89, 76, 69, 68, 13, 17, 84, 11, 36, 37, 98, 82, 76,
               79, 7, 74, 55, 6, 94, 50, 68, 7, 48, 66, 20, 79, 3, 35, 97, 56, 63, 88, 89, 58, 50, 37, 85, 94, 98, 4,
               37, 37, 32, 26, 56, 79, 92, 54, 55, 26, 89, 79, 93, 19, 96, 11, 51, 63, 64, 27, 32, 34, 87, 71, 9, 22,
               11, 78, 82, 84, 87, 88, 19, 64, 44, 67, 51, 65, 52, 1, 60, 94, 10, 17, 90, 72, 54, 73, 30, 55, 89, 48,
               52, 52, 15, 47, 42, 36, 57, 27, 89, 85, 46, 43, 49, 43, 76, 85, 64, 15, 51, 1, 82, 76, 40, 34, 6, 99, 82,
               67, 74, 24, 69, 36, 43, 43, 97, 1, 21, 61, 97, 99, 95, 91, 91, 75, 62, 33, 22, 16, 83, 11, 54, 82, 97,
               31, 85, 79, 42, 82, 53, 29, 85, 82, 17, 91, 8, 94, 84, 11, 17, 42, 70, 5, 8, 9, 0, 37, 31, 36, 20, 96,
               49, 75, 92, 82, 7, 5, 51, 72, 83, 99, 33, 79, 36, 70, 18, 42, 98, 37, 21, 36, 99, 10, 61, 43, 16, 0, 13,
               93, 50, 69, 75, 31, 76, 78, 58, 54, 1, 23, 84, 84, 44, 62, 56, 68, 23, 37, 83, 61, 0, 3, 31, 57, 15, 36,
               96, 50, 99, 84, 19, 77, 85, 60, 57, 64, 96, 4, 55, 70, 96, 0, 30, 0, 62, 69, 72, 30, 22, 72, 52, 41, 65,
               29, 51, 30, 3, 82, 22, 63, 29, 53, 40, 24, 63, 46, 38, 38, 1, 14, 24, 84, 36, 31, 20, 89, 51, 61, 96, 11,
               77, 19, 50, 88, 16, 21, 80, 95, 33, 43, 38, 98, 4, 44, 61, 62, 8, 89, 6, 67, 33, 17, 57, 45, 91, 98, 99,
               79, 64, 83, 60, 13, 6, 98, 20, 58, 46, 2, 24, 50, 62, 36, 2, 85, 82, 81, 87, 82, 66, 37, 53, 91, 99, 20,
               9, 99, 80, 77, 33, 71, 98, 40, 87, 92, 57, 42, 15, 64, 48, 37, 0, 69, 98, 29, 1, 8, 64, 6, 71, 6, 21, 26,
               72, 61, 57, 4, 49, 73, 65, 77, 66, 22, 11, 22, 7, 26, 5, 19, 56, 44, 63, 50, 0, 95, 12, 77, 27, 28, 0,
               27, 20, 58, 55, 58, 44, 17, 67, 81, 75, 89, 87, 70, 56, 36, 7, 39, 8, 22, 29, 26, 96, 6, 25, 93, 24, 62,
               16, 28, 13, 78, 14, 72, 37, 54, 98, 60, 89, 36, 78, 39, 22, 98, 84, 89, 95, 96, 1, 62, 72, 42, 51, 65,
               57, 10, 96, 5, 38, 68, 12, 8, 99, 39, 57, 68, 84, 63, 13, 50, 52, 43, 33, 43, 49, 52, 92, 77, 14, 55, 63,
               1, 99, 14, 38, 67, 76, 28, 36, 83, 28, 36, 78, 30, 92, 72, 16, 16, 55, 58, 51, 56, 36, 69, 4, 62, 33, 21,
               73, 92, 97, 27, 70, 86, 65, 34, 17, 76, 89, 41, 18, 62, 49, 75, 80, 64, 28, 70, 8, 46, 78, 2, 78, 50, 50,
               36, 86, 64, 99, 27, 82, 81, 70, 60, 17, 96, 95, 6, 41, 91, 99, 98, 99, 6, 86, 39, 19, 11, 18, 26, 40, 14,
               50, 67, 25, 50, 38, 99, 12, 10, 44, 55, 32, 4, 83, 67, 42, 29, 71, 44, 59, 98, 37, 53, 78, 76, 89, 62,
               77, 54, 72, 54, 10, 11, 53, 4, 50, 76, 53, 97, 72, 10, 29, 29, 51, 25, 17, 90, 41, 42, 46, 58, 34, 2, 8,
               47, 92, 6, 54, 83, 87, 12, 10, 78, 58, 58, 6, 96, 52, 15, 20, 15, 86, 1, 18, 34, 92, 43, 92, 96, 64, 49,
               25, 36, 61, 67, 27, 45, 87, 13, 23, 37, 18, 22, 36, 98, 2, 53, 34, 98, 68, 70, 45, 90, 59, 54, 56, 97,
               75, 59, 53, 0, 24, 51, 5, 11, 10, 95, 34, 39, 93, 14, 11, 47, 38, 4, 99, 60, 58, 38, 9, 80, 97, 25, 55,
               76, 57, 49, 41, 45, 27, 77, 71, 9, 37, 60, 25, 91, 13, 28, 28, 39, 99, 91, 31, 52, 20, 33, 25, 8, 52, 43,
               9, 43, 99, 37, 11, 62, 72, 24, 55, 71, 83, 76, 99, 23, 13, 78, 56, 24, 56, 0, 57, 6, 93, 72, 59, 10, 90,
               65, 95, 95, 75, 53, 12, 69, 25, 61, 36, 72, 4, 89, 80, 89, 68, 23, 59, 87, 25, 77, 54, 32, 21, 47, 47,
               54, 17, 36, 11, 19, 18, 80, 33, 39, 26, 50, 82, 17, 86, 18, 77, 20, 24, 30, 18, 8, 22, 33, 25, 47, 31,
               70, 92, 73, 18, 6, 14, 19, 85, 29, 82, 6, 76, 14, 22, 29, 94, 8, 30, 81, 37, 98, 27, 94, 11, 83, 91, 74,
               2, 49, 50, 51, 29, 51, 10, 64, 39, 45, 45, 68, 30, 78, 85, 52, 17, 91, 75, 26, 16, 79, 81, 58, 72, 67,
               73, 25, 7, 23, 6, 52, 91, 19, 22, 34, 35, 44, 11, 6, 31, 50, 48, 99, 82, 90, 6, 86, 75, 55, 10, 76, 12,
               59, 24, 29, 17, 76, 68, 61, 54, 19]

plot.scatter(areas, amounts)
plot.show()