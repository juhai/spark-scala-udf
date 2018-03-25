#!/bin/bash

data_filename="Coursera-SwiftKey.zip"
md5sum="e0629c64b1747103a7e751b0a30d3858"
data_url="https://d396qusza40orc.cloudfront.net/dsscapstone/dataset/${data_filename}"
unpacked_location="/var/tmp/coursera-data"
data_location="${unpacked_location}/${data_filename}"

{ [ -e ${data_location} ] && [ $(md5 < ${data_location}) == "${md5sum}" ]; } || \
    { echo "Downloading dataset" && mkdir -p $(dirname ${data_location}) && wget --progress bar -O ${data_location} ${data_url}; }

# { [ -e ${data_location} ] && [ $(md5 < ${data_location}) == "${md5sum}" ]; } || { echo "Downloading"; }

[ -e "${unpacked_location}/final" ] || \
    { echo "Unpacking dataset" && cd ${unpacked_location} && unzip ${data_filename}; }

