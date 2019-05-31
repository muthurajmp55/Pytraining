read -p "Enter file with numbers: " fil
sum=0
while read LINE
do
  sum=$(expr $sum + $LINE)
done < $fil
echo "The total sum is $sum"

