echo -n "Enter the first value: "
read x
read -p "Enter second value: " y
if test $x -gt $y; then
  echo $x is greater than $y
elif test $x -lt $y; then
  echo $x is less than $y
else
  echo Both values are equal
fi

