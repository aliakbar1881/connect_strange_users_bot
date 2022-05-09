#!/bin/bash
clear

echo "=============== Hey $USER ==============="
echo

echo " - > Your bash environment is initialize"
echo

conda init

echo
echo "* * * Enter your desired conda environment to activatation : "
read condaEnv

conda activate $condaEnv

export PYTHONPATH=${PWD}

echo " - > Your \"PYTHONPATH\" variable is  $PYTHONPATH"
echo

export BOT_TOKEN="5116983436:AAGrk1j7aVTn2MaLgZavwPl3lXHF0bGrOWE"

echo " - > Your bot token is => $BOT_TOKEN"
echo

echo " - > current time : `date `"
echo

echo "=============== Done ! ==============="
echo
