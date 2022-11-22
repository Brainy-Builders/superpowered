#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor,
    TouchSensor,
    ColorSensor,
    InfraredSensor,
    UltrasonicSensor,
    GyroSensor,
)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
import time
import math
import os
from common import *
import os
f={0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: -2, 20: -2, 21: -2, 22: -2, 23: -2, 24: -2, 25: -2, 26: -2, 27: -2, 28: -2, 29: -2, 30: -2, 31: -2, 32: -2, 33: -2, 34: -2, 35: -2, 36: -2, 37: -2, 38: -2, 39: -2, 40: -2, 41: -2, 42: -2, 43: -2, 44: -2, 45: -3, 46: -3, 47: -3, 48: -3, 49: -3, 50: -3, 51: -3, 52: -3, 53: -3, 54: -3, 55: -3, 56: -3, 57: -3, 58: -5, 59: -5, 60: -5, 61: -5, 62: -5, 63: -5, 64: -5, 65: -5, 66: -5, 67: -5, 68: -5, 69: -10, 70: -10, 71: -10, 72: -10, 73: -10, 74: -10, 75: -10, 76: -10, 77: -10, 78: -10, 79: -10, 80: -10, 81: -14, 82: -14, 83: -14, 84: -14, 85: -14, 86: -14, 87: -14, 88: -14, 89: -14, 90: -14, 91: -14, 92: -14, 93: -14, 94: -17, 95: -17, 96: -17, 97: -17, 98: -17, 99: -17, 100: -17, 101: -17, 102: -17, 103: -17, 104: -17, 105: -17, 106: -17, 107: -17, 108: -18, 109: -18, 110: -18, 111: -18, 112: -18, 113: -18, 114: -18, 115: -18, 116: -18, 117: -18, 118: -18, 119: -18, 120: -18, 121: -18, 122: -19, 123: -19, 124: -19, 125: -19, 126: -19, 127: -19, 128: -19, 129: -19, 130: -19, 131: -19, 132: -19, 133: -19, 134: -19, 135: -19, 136: -19, 137: -20, 138: -20, 139: -20, 140: -20, 141: -20, 142: -20, 143: -20, 144: -20, 145: -20, 146: -20, 147: -20, 148: -20, 149: -20, 150: -20, 151: -20, 152: -20, 153: -20, 154: -20, 155: -20, 156: -20, 157: -20, 158: -20, 159: -20, 160: -20, 161: -20, 162: -20, 163: -20, 164: -20, 165: -21, 166: -21, 167: -21, 168: -21, 169: -21, 170: -21, 171: -21, 172: -21, 173: -21, 174: -21, 175: -21, 176: -21, 177: -21, 178: -21, 179: -21, 180: -22, 181: -22, 182: -22, 183: -22, 184: -22, 185: -22, 186: -22, 187: -22, 188: -22, 189: -22, 190: -22, 191: -22, 192: -22, 193: -22, 194: -22, 195: -23, 196: -23, 197: -23, 198: -23, 199: -23, 200: -23, 201: -23, 202: -23, 203: -23, 204: -23, 205: -23, 206: -23, 207: -23, 208: -23, 209: -23, 210: -25, 211: -25, 212: -25, 213: -25, 214: -25, 215: -25, 216: -25, 217: -25, 218: -25, 219: -25, 220: -25, 221: -25, 222: -25, 223: -25, 224: -28, 225: -28, 226: -28, 227: -28, 228: -28, 229: -28, 230: -28, 231: -28, 232: -28, 233: -28, 234: -28, 235: -28, 236: -28, 237: -32, 238: -32, 239: -32, 240: -32, 241: -32, 242: -32, 243: -32, 244: -32, 245: -32, 246: -32, 247: -32, 248: -32, 249: -32, 250: -32, 251: -32, 252: -36, 253: -36, 254: -36, 255: -36, 256: -36, 257: -36, 258: -36, 259: -36, 260: -36, 261: -36, 262: -36, 263: -36, 264: -36, 265: -36, 266: -36, 267: -36, 268: -36, 269: -36, 270: -36, 271: -36, 272: -36, 273: -36, 274: -36, 275: -36, 276: -36, 277: -36, 278: -36, 279: -36, 280: -36, 281: -36, 282: -36, 283: -36, 284: -36, 285: -36, 286: -37, 287: -37, 288: -37, 289: -37, 290: -37, 291: -37, 292: -37, 293: -37, 294: -37, 295: -37, 296: -37, 297: -37, 298: -37, 299: -37, 300: -37, 301: -37, 302: -37, 303: -39, 304: -39, 305: -39, 306: -39, 307: -39, 308: -39, 309: -39, 310: -39, 311: -39, 312: -39, 313: -39, 314: -39, 315: -39, 316: -39, 317: -39, 318: -39, 319: -39, 320: -39, 321: -39, 322: -39, 323: -39, 324: -39, 325: -39, 326: -39, 327: -39, 328: -39, 329: -39, 330: -39, 331: -39, 332: -39, 333: -38, 334: -38, 335: -38, 336: -38, 337: -38, 338: -38, 339: -38, 340: -38, 341: -38, 342: -38, 343: -38, 344: -38, 345: -38, 346: -38, 347: -38, 348: -38, 349: -33, 350: -33, 351: -33, 352: -33, 353: -33, 354: -33, 355: -33, 356: -33, 357: -33, 358: -33, 359: -33, 360: -33, 361: -33, 362: -33, 363: -33, 364: -33, 365: -29, 366: -29, 367: -29, 368: -29, 369: -29, 370: -29, 371: -29, 372: -29, 373: -29, 374: -29, 375: -29, 376: -29, 377: -29, 378: -29, 379: -24, 380: -24, 381: -24, 382: -24, 383: -24, 384: -24, 385: -24, 386: -24, 387: -24, 388: -24, 389: -24, 390: -24, 391: -24, 392: -24, 393: -24, 394: -24, 395: -24, 396: -21, 397: -21, 398: -21, 399: -21, 400: -21, 401: -21, 402: -21, 403: -21, 404: -21, 405: -21, 406: -21, 407: -21, 408: -21, 409: -21, 410: -21, 411: -21, 412: -21, 413: -20, 414: -20, 415: -20, 416: -20, 417: -20, 418: -20, 419: -20, 420: -20, 421: -20, 422: -20, 423: -20, 424: -20, 425: -20, 426: -20, 427: -20, 428: -20, 429: -18, 430: -18, 431: -18, 432: -18, 433: -18, 434: -18, 435: -18, 436: -18, 437: -18, 438: -18, 439: -18, 440: -18, 441: -18, 442: -18, 443: -18, 444: -14, 445: -14, 446: -14, 447: -14, 448: -14, 449: -14, 450: -14, 451: -14, 452: -14, 453: -14, 454: -14, 455: -14, 456: -12, 457: -12, 458: -12, 459: -12, 460: -12, 461: -12, 462: -12, 463: -12, 464: -11, 465: -11, 466: -11, 467: -11, 468: -11, 469: -11, 470: -11, 471: -9, 472: -9, 473: -9, 474: -9, 475: -9, 476: -9, 477: -9, 478: -9, 479: -9, 480: -9, 481: -9, 482: -3, 483: -3, 484: -3, 485: -3, 486: -3, 487: -3, 488: -3, 489: -3, 490: -3, 491: -3, 492: -3, 493: -2, 494: -2, 495: -2, 496: -2, 497: -2, 498: -2, 499: -2, 500: -2, 501: -2, 502: -1, 503: -1, 504: -1, 505: -1, 506: -1, 507: -1, 508: -1, 509: -1, 510: 2, 511: 2, 512: 2, 513: 2, 514: 2, 515: 2, 516: 2, 517: 2, 518: 2, 519: 7, 520: 7, 521: 7, 522: 7, 523: 7, 524: 7, 525: 7, 526: 7, 527: 7, 528: 7, 529: 7, 530: 8, 531: 8, 532: 8, 533: 8, 534: 8, 535: 8, 536: 8, 537: 8, 538: 8, 539: 8, 540: 8, 541: 10, 542: 10, 543: 10, 544: 10, 545: 10, 546: 10, 547: 10, 548: 10, 549: 10, 550: 10, 551: 10, 552: 14, 553: 14, 554: 14, 555: 14, 556: 14, 557: 14, 558: 14, 559: 14, 560: 14, 561: 14, 562: 14, 563: 14, 564: 14, 565: 19, 566: 19, 567: 19, 568: 19, 569: 19, 570: 19, 571: 19, 572: 19, 573: 19, 574: 19, 575: 19, 576: 23, 577: 23, 578: 23, 579: 23, 580: 23, 581: 23, 582: 23, 583: 25, 584: 25, 585: 25, 586: 25, 587: 25, 588: 25, 589: 25, 590: 25, 591: 25, 592: 25, 593: 27, 594: 27, 595: 27, 596: 27, 597: 27, 598: 27, 599: 27, 600: 27, 601: 27, 602: 27, 603: 27, 604: 27, 605: 33, 606: 33, 607: 33, 608: 33, 609: 33, 610: 33, 611: 33, 612: 33, 613: 33, 614: 33, 615: 33, 616: 33, 617: 33, 618: 37, 619: 37, 620: 37, 621: 37, 622: 37, 623: 37, 624: 37, 625: 37, 626: 37, 627: 37, 628: 37, 629: 37, 630: 37, 631: 37, 632: 37, 633: 42, 634: 42, 635: 42, 636: 42, 637: 42, 638: 42, 639: 42, 640: 42, 641: 42, 642: 42, 643: 42, 644: 42, 645: 42, 646: 42, 647: 42, 648: 42, 649: 42, 650: 46, 651: 46, 652: 46, 653: 46, 654: 46, 655: 46, 656: 46, 657: 46, 658: 46, 659: 46, 660: 46, 661: 46, 662: 46, 663: 46, 664: 46, 665: 46, 666: 46, 667: 44, 668: 44, 669: 44, 670: 44, 671: 44, 672: 44, 673: 44, 674: 44, 675: 44, 676: 44, 677: 44, 678: 44, 679: 44, 680: 44, 681: 44, 682: 44, 683: 43, 684: 43, 685: 43, 686: 43, 687: 43, 688: 43, 689: 43, 690: 43, 691: 43, 692: 43, 693: 43, 694: 43, 695: 43, 696: 43, 697: 43, 698: 43, 699: 43, 700: 46, 701: 46, 702: 46, 703: 46, 704: 46, 705: 46, 706: 46, 707: 46, 708: 46, 709: 46, 710: 46, 711: 46, 712: 46, 713: 46, 714: 46, 715: 46, 716: 49, 717: 49, 718: 49, 719: 49, 720: 49, 721: 49, 722: 49, 723: 49, 724: 49, 725: 49, 726: 49, 727: 49, 728: 49, 729: 49, 730: 48, 731: 48, 732: 48, 733: 48, 734: 48, 735: 48, 736: 48, 737: 48, 738: 48, 739: 48, 740: 48, 741: 48, 742: 48, 743: 48, 744: 48, 745: 45, 746: 45, 747: 45, 748: 45, 749: 45, 750: 45, 751: 45, 752: 45, 753: 45, 754: 45, 755: 45, 756: 45, 757: 40, 758: 40, 759: 40, 760: 40, 761: 40, 762: 40, 763: 40, 764: 40, 765: 40, 766: 40, 767: 40, 768: 40, 769: 40, 770: 37, 771: 37, 772: 37, 773: 37, 774: 37, 775: 37, 776: 37, 777: 37, 778: 37, 779: 37, 780: 37, 781: 37, 782: 35, 783: 35, 784: 35, 785: 35, 786: 35, 787: 35, 788: 35, 789: 35, 790: 35, 791: 35, 792: 35, 793: 35, 794: 35, 795: 35, 796: 35, 797: 35, 798: 35, 799: 35, 800: 35, 801: 35, 802: 35, 803: 35, 804: 35, 805: 35, 806: 35, 807: 34, 808: 34, 809: 34, 810: 34, 811: 34, 812: 34, 813: 34, 814: 34, 815: 34, 816: 34, 817: 34, 818: 34, 819: 34, 820: 37, 821: 37, 822: 37, 823: 37, 824: 39, 825: 39, 826: 39, 827: 39, 828: 39, 829: 39, 830: 39, 831: 39, 832: 39, 833: 39, 834: 43, 835: 43, 836: 43, 837: 43, 838: 43, 839: 43, 840: 43, 841: 43, 842: 43, 843: 43, 844: 43, 845: 43, 846: 43, 847: 43, 848: 43, 849: 43, 850: 50, 851: 50, 852: 50, 853: 50, 854: 50, 855: 50, 856: 50, 857: 50, 858: 50, 859: 50, 860: 50, 861: 50, 862: 50, 863: 50, 864: 50, 865: 50, 866: 50, 867: 50, 868: 51, 869: 51, 870: 51, 871: 51, 872: 51, 873: 51, 874: 51, 875: 51, 876: 51, 877: 51, 878: 51, 879: 51, 880: 51, 881: 51, 882: 51, 883: 51, 884: 51, 885: 51, 886: 51, 887: 51, 888: 53, 889: 53, 890: 53, 891: 53, 892: 53, 893: 53, 894: 53, 895: 53, 896: 53, 897: 53, 898: 53, 899: 53, 900: 53, 901: 53, 902: 53, 903: 53, 904: 53, 905: 53, 906: 53, 907: 55, 908: 55, 909: 55, 910: 55, 911: 55, 912: 55, 913: 55, 914: 55, 915: 55, 916: 55, 917: 55, 918: 55, 919: 55, 920: 55, 921: 55, 922: 55, 923: 55, 924: 57, 925: 57, 926: 57, 927: 57, 928: 57, 929: 57, 930: 57, 931: 57, 932: 57, 933: 57, 934: 57, 935: 57, 936: 57, 937: 57, 938: 60, 939: 60, 940: 60, 941: 60, 942: 60, 943: 60, 944: 60, 945: 60, 946: 60, 947: 60, 948: 60, 949: 60, 950: 60, 951: 60, 952: 62, 953: 62, 954: 62, 955: 62, 956: 62, 957: 62, 958: 62, 959: 62, 960: 62, 961: 62, 962: 62, 963: 62, 964: 62, 965: 62, 966: 62, 967: 62, 968: 62, 969: 68, 970: 68, 971: 68, 972: 68, 973: 68, 974: 68, 975: 68, 976: 68, 977: 68, 978: 68, 979: 68, 980: 68, 981: 68, 982: 68, 983: 73, 984: 73, 985: 73, 986: 73, 987: 73, 988: 73, 989: 73, 990: 73, 991: 73, 992: 73, 993: 73, 994: 73, 995: 73, 996: 73, 997: 73, 998: 76, 999: 76, 1000: 76, 1001: 76, 1002: 76, 1003: 76, 1004: 76, 1005: 76, 1006: 76, 1007: 76, 1008: 76, 1009: 76, 1010: 76, 1011: 76, 1012: 84, 1013: 84, 1014: 84, 1015: 84, 1016: 84, 1017: 84, 1018: 84, 1019: 84, 1020: 84, 1021: 84, 1022: 84, 1023: 84, 1024: 84, 1025: 82, 1026: 82, 1027: 82, 1028: 82, 1029: 82, 1030: 82, 1031: 82, 1032: 82, 1033: 82, 1034: 82, 1035: 82, 1036: 82, 1037: 82, 1038: 82, 1039: 80, 1040: 80, 1041: 80, 1042: 80, 1043: 80, 1044: 80, 1045: 80, 1046: 80, 1047: 80, 1048: 80, 1049: 80, 1050: 80, 1051: 80, 1052: 80, 1053: 80, 1054: 80, 1055: 78, 1056: 78, 1057: 78, 1058: 78, 1059: 78, 1060: 78, 1061: 78, 1062: 78, 1063: 78, 1064: 78, 1065: 78, 1066: 78, 1067: 78, 1068: 79, 1069: 79, 1070: 79, 1071: 79, 1072: 79, 1073: 79, 1074: 79, 1075: 79, 1076: 79, 1077: 80, 1078: 80, 1079: 80, 1080: 80, 1081: 80, 1082: 80, 1083: 80, 1084: 80, 1085: 80, 1086: 82, 1087: 82, 1088: 82, 1089: 82, 1090: 82, 1091: 82, 1092: 82, 1093: 82, 1094: 82, 1095: 82, 1096: 82, 1097: 82, 1098: 82, 1099: 82, 1100: 82, 1101: 82, 1102: 82, 1103: 82, 1104: 82, 1105: 82, 1106: 82, 1107: 82, 1108: 82, 1109: 82, 1110: 82, 1111: 82, 1112: 82, 1113: 82, 1114: 82, 1115: 82, 1116: 82, 1117: 82, 1118: 82, 1119: 82, 1120: 82, 1121: 82, 1122: 82, 1123: 82, 1124: 82, 1125: 82, 1126: 82, 1127: 82, 1128: 82, 1129: 82, 1130: 82, 1131: 82, 1132: 82, 1133: 82, 1134: 82, 1135: 82, 1136: 82, 1137: 82, 1138: 82, 1139: 83, 1140: 83, 1141: 83, 1142: 83, 1143: 83, 1144: 83, 1145: 83, 1146: 83, 1147: 83, 1148: 83, 1149: 83, 1150: 83, 1151: 83, 1152: 83, 1153: 83, 1154: 83, 1155: 83, 1156: 83, 1157: 83, 1158: 83, 1159: 83, 1160: 83, 1161: 83, 1162: 83, 1163: 83, 1164: 83, 1165: 84, 1166: 84, 1167: 84, 1168: 84, 1169: 84, 1170: 84, 1171: 84, 1172: 84, 1173: 84, 1174: 84, 1175: 84, 1176: 84, 1177: 84, 1178: 86, 1179: 86, 1180: 86, 1181: 86, 1182: 86, 1183: 86, 1184: 86, 1185: 86, 1186: 86, 1187: 86, 1188: 86, 1189: 86, 1190: 87, 1191: 87, 1192: 87, 1193: 87, 1194: 87, 1195: 87, 1196: 87, 1197: 87, 1198: 87, 1199: 87, 1200: 87, 1201: 87, 1202: 87, 1203: 87, 1204: 88, 1205: 88, 1206: 88, 1207: 88, 1208: 88, 1209: 88, 1210: 88, 1211: 88, 1212: 88, 1213: 88, 1214: 88, 1215: 88, 1216: 88, 1217: 90, 1218: 90, 1219: 90, 1220: 90, 1221: 90, 1222: 90, 1223: 90, 1224: 90, 1225: 90, 1226: 90, 1227: 90, 1228: 91, 1229: 91, 1230: 91, 1231: 91, 1232: 91, 1233: 91, 1234: 91, 1235: 91, 1236: 91, 1237: 91, 1238: 91, 1239: 91, 1240: 91, 1241: 92, 1242: 92, 1243: 92, 1244: 92, 1245: 92, 1246: 92, 1247: 92, 1248: 92, 1249: 92, 1250: 92, 1251: 92, 1252: 92, 1253: 92, 1254: 92, 1255: 91, 1256: 91, 1257: 91, 1258: 91, 1259: 91, 1260: 91, 1261: 91, 1262: 91, 1263: 91, 1264: 91, 1265: 91, 1266: 91, 1267: 91, 1268: 91, 1269: 91, 1270: 93, 1271: 93, 1272: 93, 1273: 93, 1274: 93, 1275: 93, 1276: 93, 1277: 93, 1278: 93, 1279: 93, 1280: 93, 1281: 93, 1282: 93, 1283: 93, 1284: 93, 1285: 93, 1286: 93, 1287: 93, 1288: 94, 1289: 94, 1290: 94, 1291: 94, 1292: 94, 1293: 94, 1294: 94, 1295: 94, 1296: 94, 1297: 94, 1298: 94, 1299: 94, 1300: 94, 1301: 94, 1302: 94, 1303: 94, 1304: 94, 1305: 94, 1306: 93, 1307: 93, 1308: 93, 1309: 93, 1310: 93, 1311: 93, 1312: 93, 1313: 93, 1314: 93, 1315: 93, 1316: 93, 1317: 93, 1318: 93, 1319: 93, 1320: 93, 1321: 93, 1322: 93, 1323: 93, 1324: 92, 1325: 92, 1326: 92, 1327: 92, 1328: 92, 1329: 92, 1330: 92, 1331: 92, 1332: 92, 1333: 92, 1334: 92, 1335: 92, 1336: 92, 1337: 92, 1338: 93, 1339: 93, 1340: 93, 1341: 93, 1342: 93, 1343: 93, 1344: 93, 1345: 93, 1346: 93, 1347: 93, 1348: 93, 1349: 93, 1350: 95, 1351: 95, 1352: 95, 1353: 95, 1354: 95, 1355: 95, 1356: 95, 1357: 95, 1358: 95, 1359: 95, 1360: 95, 1361: 95, 1362: 95, 1363: 95, 1364: 95, 1365: 95, 1366: 95, 1367: 95, 1368: 95, 1369: 95, 1370: 95, 1371: 95, 1372: 95, 1373: 95, 1374: 95, 1375: 95, 1376: 95, 1377: 95, 1378: 95, 1379: 95, 1380: 95, 1381: 95, 1382: 95, 1383: 95, 1384: 95, 1385: 95, 1386: 95, 1387: 95, 1388: 95, 1389: 96, 1390: 96, 1391: 96, 1392: 96, 1393: 96, 1394: 96, 1395: 96, 1396: 96, 1397: 96, 1398: 96, 1399: 96, 1400: 96, 1401: 96, 1402: 96, 1403: 96, 1404: 95, 1405: 95, 1406: 95, 1407: 95, 1408: 95, 1409: 95, 1410: 95, 1411: 95, 1412: 95, 1413: 95, 1414: 95, 1415: 95, 1416: 95, 1417: 95, 1418: 95, 1419: 95, 1420: 95, 1421: 95, 1422: 94, 1423: 94, 1424: 94, 1425: 94, 1426: 94, 1427: 94, 1428: 94, 1429: 94, 1430: 94, 1431: 94, 1432: 94, 1433: 94, 1434: 94, 1435: 94, 1436: 94, 1437: 93, 1438: 93, 1439: 93, 1440: 93, 1441: 93, 1442: 93, 1443: 93, 1444: 93, 1445: 93, 1446: 93, 1447: 93, 1448: 93, 1449: 93, 1450: 93, 1451: 93, 1452: 93, 1453: 93, 1454: 93}

def record():
    robot.reset()
    gyro.reset_angle(0)
    while True:
        c=robot.distance()
        b=gyro.angle()
        ev3.screen.print(c,", ",b)
        print(c,", ",b)
        time.sleep(0.3)
def run(load=f, speed=300, t_prime=0.5):
    robot.reset()
    d=load
    t=t_prime
    t_prime=time.time()+t_prime
    cur_time=time.time()
    cur_speed=robot.state()[1]
    speed_calc=speed-cur_speed
    bm=robot.distance()+list(d.keys())[-1]
    heading = gyro.angle()
    x=0
    while robot.distance()<bm:
        search_key=robot.distance()
        correction = (d[search_key]-gyro.angle()) * 2.
        if time.time() < t_prime:
            speed=(speed_calc)/t*(time.time()-cur_time)
        robot.drive(speed, correction)
        x+=1
    robot.stop()
    ev3.screen.print("sdr ",x)
    time.sleep(10)
def load_data(load=f):
    load=load.split("\n")
    d={}
    for i in load:
        x=i.replace(" ", "").split(",")
        d[int(x[0])]=int(x[1])
    x=load[-1].split(",")[0]
    vals={}
    for i in range(0,int(x.replace(" ",""))):
        vals[i]=d.get(i) or d[min(d.keys(), key = lambda key: abs(key-i))]
    print(vals)
    