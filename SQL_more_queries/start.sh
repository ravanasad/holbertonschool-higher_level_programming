#!/usr/bin/bash

echo "SELECT * FROM tv_show_genres" | mysql -hlocalhost -uroot  hbtn_0d_tvshows
echo "shows"
echo "SELECT * FROM tv_shows" | mysql -hlocalhost -uroot  hbtn_0d_tvshows
echo "genres"
echo "SELECT * FROM tv_genres" | mysql -hlocalhost -uroot  hbtn_0d_tvshows
