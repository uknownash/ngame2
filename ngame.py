U
    ๚ฎ^ฤ  ใ                   @   s"   d dl Z d dlZdd Ze  dS )้    Nc               	      s*  d} dd d}d}dd}t  ddก}td}d}t ก  d	}tj |ก}d}	d
d}
d}d}d}ddd}d}d||krขtdd}| dก W 5 Q R X tdd}| 	ก W 5 Q R X dd dd    f	dd}t
d t
 t
d t
 t
 d   t
 t
d t
d! t
d" td#}|}t
d t
 |d$kr\d}|dkr|t|7 }|d7 }qnt
d t
d%|   t
d|
 d&   t| d'}|	s&|  |d(krโd)}	t||kr||kr|d*krJ||7 }t
| d+ t
 t
d|
 d&   t| d,}qศn<t
| d+ t
 t
d|
 d&   t| d,}qศnt|}||k r
 d8  t d-ก t
 t
| d.| d/ t
 |  t
d%|   t
d|
 d&   t| d,}qศ||kr d8  t d-ก t
 t
| d.| d0 t
 |  t
d%|   t
d|
 d&   t| d,}nิ||krศ d8  ||   |     t
d t
d1 t
| d2|   d3 | d t
 |d4 }|d48 }| | d7 } t
d5 t
d%|   t
d|
 d&   t| d6}t  ddก}qศqศnส|d7kr๖tdd~}| 	ก t
d t
d8  t
d t
 t
d t
d9 td:}| ก d;krุt d-ก t  nt
d t d-ก W 5 Q R X n0t
d< t
 t
 d   t
 t  d S )=N้   r   ้   ้
   ฺ ้d   ฺaFz
/score.txtz;-----------------------------------------------------------z                    z                     z            z                       z-------------------------z-------------------z--------z                   z--------------------๚	score.txtฺwฺ0ฺrc              	   S   s4   | t |kr0tdd}| t| ก W 5 Q R X d S )Nr   r	   )ฺintฺopenฺwriteฺstr)r   ฺbฺfฉ r   ๚/sdcard/code/python/ngame.pyฺnewscore=   s    zmain.<locals>.newscorec                   S   s   t  dก d S )Nฺclear)ฺosฺsystemr   r   r   r   ฺclsC   s    zmain.<locals>.clsc                     s    dkr  t d d  t  d  t  t  d  t  t  d  t   d} t  d S )Nr   ฺ
z	Game OverzYou are loss The GamezThanks For Playing๚Make By Alok MistryT)ฺprintฺexit)ฺgameOverฉ	Zchancer   Zfullr   ฺreadZscoreZsp5Zsp6Zsp9r   r   ฺendH   s    
zmain.<locals>.endr   z;----------------------Welcom To Ngame----------------------r   z1) ---------->	Start The Game 
z2) ---------->	High Score 
zChoose On of The Above : ฺ1zLevel =	zYour Chance Left zEnter a Number From 1 to 100 : r   TฺczPlease Enter A NumberzTry Again : r   zYour Entered Number z is too lowz is too Highz;--------------------You are win The Game------------------ zYour used chance is z And Your Score is ้   zCongratulation Your Level Is UpzEnter a Number : ฺ2zHigh Score =	zPress y to Go Back : 
zPress y/c : ฺyzChoose Right Number )ฺrandomZrandintฺtyper   ฺgetcwdฺpathฺexistsr   r   r   r   ฺinputr   r   r   ฺlowerฺmain)ฺlevelZhchanceZpointฺnฺfnZnonTypeฺdisr)   Zfpathr   ZspZsp2Zsp3Zsp4Zsp7Zsp8r   r    Zchooser   ZiiZnumZbuttonr   r   r   r-      s   










"


r-   )r&   r   r-   r   r   r   r   ฺ<module>
   s    Y