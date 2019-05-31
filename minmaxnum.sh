read -p "Enter file with numbers: " fil
ln=1
while read LINE
do
  if [ $ln -eq 1 ]; then
    min=$LINE
    max=$LINE
  else
    if [ $min -gt $LINE ]; then
      min=$LINE
    fi
    if [ $max -lt $LINE ]; then
      max=$LINE
    fi
  fi
  ln=$(expr $ln + 1)
done < $fil
echo "Minimum value: $min"
echo "Maximum value: $max"

