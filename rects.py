from pygame import *
from math import *
yard=[[Rect(42,81,77,96),Rect(127,79,67,96),Rect(202,80,75,95),
  Rect(282,79,77,99),Rect(359,76,77,100),Rect(444,78,76,102),
  Rect(526,81,71,98),Rect(606,88,70,92),Rect(680,93,85,90)],
 [Rect(35,183,82,89),Rect(121,183,69,92),Rect(196,181,77,91),
  Rect(279,182,75,94),Rect(360,183,75,89),Rect(438,181,81,97),
  Rect(523,181,69,92),Rect(598,183,81,92),Rect(681,185,91,90)],
 [Rect(39,277,74,98),Rect(121,277,73,102),Rect(195,282,85,98),
  Rect(286,282,71,100),Rect(363,281,72,103),Rect(440,288,81,95),
  Rect(526,285,67,97),Rect(598,281,84,104),Rect(688,282,84,101)],
 [Rect(38,382,79,91),Rect(117,382,78,88),Rect(196,390,83,80),
  Rect(283,386,70,84),Rect(364,388,75,83),Rect(439,389,79,83),
  Rect(522,385,75,84),Rect(598,388,80,75),Rect(685,387,90,77)],
 [Rect(31,477,85,93),Rect(123,475,70,98),Rect(202,478,77,96),
  Rect(284,476,78,94),Rect(362,477,82,94),Rect(447,474,73,97),
  Rect(520,475,80,98),Rect(605,474,74,98),Rect(690,472,82,97)]]

bar=[Rect(87,10,44,65),Rect(145,10,46,65),Rect(205,10,44,64),
     Rect(263,9,45,66),Rect(322,9,46,66),Rect(382,9,45,67)]

shovelRect=Rect(500,0,71,71)

resumeRect=Rect(242,425,300,45)
pauseRect=Rect(571,0,112,31)

menuRects=[Rect(405,70,317,136),Rect(407,175,309,130),Rect(409,260,273,117),
           Rect(549,425,93,89),Rect(639,452,67,99),Rect(703,460,75,88)]

helpRect=Rect(323,521,159,43)

igMenuRect=Rect(679,0,115,32)
directRects=[Rect(295,292,205,40),Rect(296,336,204,39),Rect(296,379,203,40),
             Rect(235,445,331,72)]
direct=["almanac","adventure","menu","none"]

choiceRects=[Rect(23,124,48,69),Rect(76,125,48,67),Rect(129,124,48,68),
             Rect(182,125,47,67),Rect(235,124,47,67),Rect(288,125,47,67),
             Rect(341,124,47,68),Rect(394,124,47,68),Rect(24,196,46,66),
             Rect(77,196,45,66),Rect(130,195,45,66),Rect(183,194,47,70),
             Rect(235,194,48,68),Rect(288,193,48,70),Rect(341,194,48,67),
             Rect(393,193,49,70)]
choiceCorner=[[23,124],[23,124],[129,124],[182,125],[235,124],[288,125],
              [341,124],[394,124],[24,196],[77,196],[130,195],[183,194],
              [235,194],[288,193],[341,194],[393,193]]
topCorner=[[0,0],[50,0],[100,0],[150,0],[200,0],[250,0]]

alRects=[Rect(26,89,69,67),Rect(109,88,70,70),Rect(195,90,68,68),
         Rect(279,88,71,70),Rect(365,88,69,68),Rect(24,170,69,67),
         Rect(110,171,69,64),Rect(194,171,70,64),Rect(279,169,72,67),
         Rect(365,170,69,65)]

alDoneRect=Rect(679,569,81,18)


playRect= Rect(157,329,151,37)
menuRect=Rect(681,1,113,27)
almanacRect=Rect(561,574,107,20)
shopRect=Rect(682,575,107,19)


