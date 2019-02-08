#!/usr/bin/python
# coding=utf-8

import urllib
import os
import requests

base_str = 'https://cn2.zuidadianying.com'

# 通过原始url获取含有电影列表url的url
def get_movie_list_url(base_url):
    try:
        for line in urllib.urlopen(base_url):
            line = line.strip()
            line.replace('  ', ' ')
            if line != '' and line.find("#") == -1:
                print 'movie_list_url is ' + base_str + line
                return base_str + line
    except:
        print 'movie_list_url is (null)'
        return ''

# 根据电影的url列表下载每个视频片段
def downloadfile(movie_list_url,out_dir_name):
    filename_pre_str = os.getcwd() + '/' + out_dir_name + '/'
    for line in urllib.urlopen(movie_list_url):
        line = line.strip()
        line.replace('  ', ' ')
        if line != '' and line.find("#") == -1:
            try:
                temp_index = line.rfind('/')
                filename = line[temp_index + 1:]
                print 'downloadfile : ' + base_str + line
                r = requests.get(url = base_str + line, timeout = (3.5, 30))
                with open(filename_pre_str + filename, 'wb') as f:
                    f.write(r.content)
            except Exception, e:
                print type(e), ':', e

# windows下合并多个文件到一个文件
def combine_files(out_dir_name):
    os.chdir(os.getcwd() + '/' + out_dir_name)
    try:
        os.system('copy /b "*.ts" "all.ts"')
    except Exception, e:
        print type(e), ':', e
    os.chdir(os.getcwd())

# 下载电影
def download(base_url,out_dir_name):
    print 'base_url is ' + base_url
    try:
        movie_list_url = get_movie_list_url(base_url)
        if movie_list_url != '':
            downloadfile(movie_list_url, out_dir_name)
            combine_files(out_dir_name)
    except Exception, e:
        print type(e), ':', e

# 将电影的url写入txt文件，用于迅雷下载
def write_url_to_file(movie_list_url, out_txt_name):
    fp_write = open(out_txt_name, 'w')
    for line in urllib.urlopen(movie_list_url):
        line = line.strip()
        line.replace('  ', ' ')
        if line != '' and line.find("#") == -1:
            try:
                fp_write.write(base_str + line + '\n')
            except Exception, e:
                print type(e), ':', e
    fp_write.close()

# 获取电影url列表，用于迅雷下载(每行一个链接)
def get_movie_url_for_thunder(base_url,out_txt_name):
    print 'base_url is ' + base_url
    try:
        movie_list_url = get_movie_list_url(base_url)
        if movie_list_url != '':
            write_url_to_file(movie_list_url, out_txt_name)
    except Exception, e:
        print type(e), ':', e

if __name__ == '__main__':

    #download('https://cn2.zuidadianying.com/20190207/Nj4iG5WQ/index.m3u8', 'llxq') # 流浪星球
    #get_movie_url_for_thunder('https://cn2.zuidadianying.com/20190207/Nj4iG5WQ/index.m3u8', 'llxq.txt') # 流浪星球

    download('https://cn2.zuidadianying.com/20190207/HAirIKlM/index.m3u8', 'fkdwxr')  # 疯狂的外星人
    #get_movie_url_for_thunder('https://cn2.zuidadianying.com/20190207/HAirIKlM/index.m3u8', 'fkdwxr.txt') # 疯狂的外星人

    #download('https://cn2.zuidadianying.com/20190207/7hFXzH8Z/index.m3u8', 'fcrs')  # 飞驰人生
    #get_movie_url_for_thunder('https://cn2.zuidadianying.com/20190207/7hFXzH8Z/index.m3u8', 'fcrs.txt') # 飞驰人生

    #download('https://cn2.zuidadianying.com/20190207/Nj4iG5WQ/index.m3u8', 'xxjzw')  # 新喜剧之王
    #get_movie_url_for_thunder('https://cn2.zuidadianying.com/20190207/Nj4iG5WQ/index.m3u8', 'xxjzw.txt') # 新喜剧之王

    print 'all finish'
