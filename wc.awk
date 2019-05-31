#!/usr/bin/awk -f 
BEGIN {
  words = 0
  chars = 0
  FS = " "
}
{
  words += NF
  chars += length($0)
}
END {
  printf "Lines: %d Words: %d Characters: %d\n", NR, words, chars
}

