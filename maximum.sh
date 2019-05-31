read -p "Enter 3 numbers: " x y z
max=$x
if [ $y -gt $max ]; then
  max=$y
fi
if [ $z -gt $max ]; then
  max=$z
fi
echo "Maximum value is $max"

