read -p "Enter a filename: " fname
if [ -e $fname ]; then
  if [ -f $fname ]; then
    echo "$fname --> Regular file"
  elif [ -d $fname ]; then
    echo "$fname --> Directory"
  else
    echo "$fname --> Something else"
  fi
else
  echo "$fname DOES NOT EXIST!!"
fi

