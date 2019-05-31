read -p "Enter a number: " num
i=1
until [ $i -gt 10 ]
do
  prod=$(expr $num \* $i)
  echo "$num * $i = $prod"
  i=$(expr $i + 1)
done

