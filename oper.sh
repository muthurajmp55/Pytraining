read -p "Enter 2 nos: " x y
read -p "Enter operator: " op
if [ "$op" = '+' ]; then
  echo -n $x '+' $y ' = '
  expr $x + $y
elif [ "$op" = '-' ]; then
  echo -n $x '-' $y ' = '
  expr $x - $y
elif [ "$op" = '/' ]; then
  echo -n $x '/' $y ' = '
  expr $x / $y
elif [ "$op" = '*' ]; then
  echo -n $x '*' $y ' = '
  expr $x '*' $y
else
  echo "Invalid operator "$op""
fi

