#!/bin/bash

raspistill -t 4000000 -tl 10000 -o image_num_%03d_today.jpg -l latest.jpg -n

exit 0
