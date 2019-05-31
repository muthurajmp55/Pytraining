read -p "Enter file to retrieve XML data: " fil
while read textLine
do
  myText=$(echo $textLine | grep -E '<(.+)>.+</\1>')
  if [ ${#myText} -gt 0 ]; then
    tagText=$(echo $myText | cut -d'<' -f2 | cut -d'>' -f1)
    tagData=$(echo $myText | cut -d'>' -f2 | cut -d'<' -f1)
    echo "$tagText: $tagData"
  fi
done < $fil

