read -p "Enter 2 nos: " x y
read -p "Enter operator: " op
if [ "$op" = '+' -o "$op" = '-' -o "$op" = '/' -o "$op" = '*' ]; then
  echo -n "$x $op $y = "
  expr $x "$op" $y
else
  echo "Invalid operator $op"
fi

