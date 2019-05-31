read -p "Enter CSV file to process: " fil
lno=1
while read line
do
  valno=1
  for num in $(echo $line | tr ',' ' ')
  do
    if [ $valno -eq 1 ]; then
      lmin=$num
      lmax=$num
    else
      if [ $lmin -gt $num ]; then
        lmin=$num
      fi
      if [ $lmax -lt $num ]; then
        lmax=$num
      fi
    fi
    if [ $lno -eq 1 ]; then
      fmin=$lmin
      fmax=$lmax
    else
      if [ $fmin -gt $lmin ]; then
        fmin=$lmin
      fi
      if [ $fmax -lt $lmax ]; then
        fmax=$lmax
      fi
    fi
    valno=$(expr $valno + 1)
  done
  echo "$line - Min: $lmin Max: $lmax"
  lno=$(expr $lno + 1)
done < $fil
echo "File Min: $fmin"
echo "File Max: $fmax"

