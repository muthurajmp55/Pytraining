#!/bin/bash

fil=$1
sz=$(stat -c%s $fil)
while true
do
  nsz=$(stat -c%s $fil)
  if [ $sz -ne $nsz ]; then
    echo $fil size changed
    sz=$nsz
  fi
  sleep 1
done

