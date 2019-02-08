# download_movie_for_zuidadianying

专门为最大电影网下载电影而设计的脚本

由于最大电影网的存储设计，每个电影被打散成一堆3-4秒的视频片段，且正常情况下只提供在线观看，不提供下载。

此脚本提供两种方式下载：

# 第一种：

1、通过python脚本中的get_movie_url_for_thunder函数从原始url中提取出所有url列表，写入txt文件中，每一行为一个视频url；

2、将txt中的所有内容复制，打开迅雷，新建任务，粘贴，确认下载，将所有视频片段下载到一个新的独立的文件夹中；

3、将combine.bat脚本复制到上一步迅雷下载的文件夹中，双击运行，将所有的视频片段以二进制的形式复制拼接在一起，形成all.ts，即为完整的视频。

## 注意：

1、由于combine.bat，此脚本只能在windows下使用，其他linux和mac系统，自行用其他方式拼接视频。

2、由于combine.bat中的*.ts，所以要保证该文件夹下的所有ts文件均为刚刚迅雷下载的文件，无其他文件，否则拼接视频会有问题。迅雷下载的文件的文件名按照从前到后序号从小到大，所以copy拼接时，无顺序问题，所以，拼接前不要自行修改文件名，以免影响顺序导致视频拼接有问题。


# 第二种：

通过python脚本中的download函数完成所有过程

## 注意：

1、由于python脚本中的combine_files函数仍然使用了windows系统下的copy函数进行视频拼接，所以此脚本的拼接部分仅限windows系统下使用，其他linux和mac系统，自行处理视频拼接逻辑；

2、由于脚本中的downloadfile函数的requests.get会导致下载超时，所以会有部分视频片段由于超时会下载失败，这一部分可以通过查看print（目前未加入日志部分）内容自行单独下载对应的片段，也可以自行加入下载失败后的重试逻辑；

3、由于所有过程均在一条流程线上执行，所以，当有部分片段由于下载超时而下载失败时，最后的视频拼接过程仍然执行，会导致拼接后的视频缺失下载失败的视频片段，这部分可以通过手动下载缺失的视频片段后，再重新手动拼接视频解决。

3、根据自己的实际需要，自行修改main函数的注释部分。


# 总说明：

由于只是一个临时脚本下载电影，最大电影网的逻辑以后也可能会修改，所以此脚本目的只为了临时使用，所以，很多复杂的逻辑并没有去处理：例如各种可能导致崩溃的情况、日志的输出、下载超时的重试逻辑、调用时通过命令行传参等等。
