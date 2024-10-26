##################
## Ren'py插件————立绘动画效果
##
## 插件作者: 永远的空之女王
## B站主页: https://space.bilibili.com/531455345?spm_id_from=333.1007.0.0
## 个人博客: https://lucylcarus.github.io/
##
##################
##
## 我该如何使用该插件？
## 
## 将该插件导入项目所在 game 文件夹即可使用
##
##################
##
## 适用范围？
##
## 以下效果适用于角色立绘
##
##################
##
##################
##
## 说明:
##
## 一般情况下，使用该插件时，您只需调整立绘位置、缩放大小即可，
## 可能会出现部分效果不适配的情况，请自行调整立绘位置、缩放大小
##
##################
##
####
##
## 使用方法:
##
## 使用show 立绘 at +效果
##
####

# 1.突然出现（适用于所有立绘）
transform burst_up:
    subpixel True
    alpha 0.00 
    xalign 0.5
    parallel:
        easein 0.12 alpha 1.0
    parallel:
        easein 0.12 zoom 0.9
        easein 0.12 zoom 1.0

# 2.从左侧进入（适用于所有立绘）
transform enter_from_left:
    subpixel True
    alpha 0.00 
    xoffset -20
    parallel:
        easein 0.5 alpha 1.0
    parallel:
        easein 0.5 xoffset 0

# 3.从右侧进入（适用于所有立绘）
transform enter_from_right:
    subpixel True
    alpha 0.00 
    xoffset 20
    parallel:
        easein 0.5 alpha 1.0
    parallel:
        easein 0.5 xoffset 0

# 4.人物淡出（适用于所有立绘）
transform exit:
    subpixel True
    alpha 1.00 
    easein 0.5 alpha 0.0

# 5.从左侧淡出（适用于所有立绘）
transform exit_from_left:
    subpixel True
    alpha 1.00 
    xoffset 0
    parallel:
        easein 0.5 alpha 0.0
    parallel:
        easein 0.5 xoffset -20

# 6.从右侧淡出（适用于所有立绘）
transform exit_from_right:
    subpixel True
    alpha 1.00 
    xoffset 0
    parallel:
        easein 0.5 alpha 0.0
    parallel:
        easein 0.5 xoffset 20

# 7.快速起身(适用于所有立绘)
transform stand_up:
    subpixel True
    yoffset 800
    linear 0.1 yoffset 0

# 8.点头一次,y为点头幅度(适用于所有立绘)
transform nod_once(y = 44):
    subpixel True
    easein 0.24 yoffset y 
    easeout 0.24 yoffset 0 

# 9.点头两次,y为点头幅度(适用于所有立绘)
transform nod_twice(y = 44):
    subpixel True
    easein 0.24 yoffset y 
    easeout 0.24 yoffset 0 
    easein 0.24 yoffset y 
    easeout 0.24 yoffset 0

# 10.摇头，t为时间(适用于所有立绘)
transform shocked(t=0.1):
    subpixel True
    easein t yoffset 0
    easeout t yoffset -100
    easein t yoffset 0

# 11.吓一跳(适用于所有立绘)
transform shake_head(t=0.15):
    subpixel True
    easein t xoffset 20
    easeout t xoffset 0
    easein t xoffset -15
    easeout t xoffset 0
    easein t xoffset 10
    easeout t xoffset 0

# 12.剧烈抖动(不循环)，t为时间(适用于所有立绘)
transform dithering(t=0.05):
    subpixel True
    easein t xoffset 20
    easeout t xoffset 0
    easein t xoffset -15
    easeout t xoffset 0
    easein t xoffset 10
    easeout t xoffset 0

# 13.剧烈抖动(循环)，t为时间(适用于所有立绘)
transform dithering_loop(t=0.05):
    subpixel True
    easein t xoffset 20
    easeout t xoffset 0
    easein t xoffset -15
    easeout t xoffset 0
    easein t xoffset 10
    easeout t xoffset 0
    repeat

###########
##
## 以下语句只有在特殊情况下使用
##
## extend语句切换立绘时替代with dissolve语句使用，可在显示对话框的情况下切换立绘，改变表情
##
###########

# 14.展示
transform display:
    alpha 0.0
    easein 0.12 alpha 1.0

# 15.消失
transform disappear:
    alpha 1.0
    easein 0.12 alpha 0.0

###############
## 更多
##
## 官方文档: https://doc.renpy.cn/zh-CN/
## 中文论坛: https://www.renpy.cn/
## 外网论坛: https://lemmasoft.renai.us/forums/
##
################