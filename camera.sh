#!/bin/bash

raspistill -t 600000 -tl 10000 -o image_num_%03d_today.jpg -l latest.jpg -n

exit 0
