#!/usr/bin/awk -f 
BEGIN {
  printf "Enter a number (Ctrl-D to quit): "
}
{
  printf "Number entered: %d and its square is: %d\n", $0, $0*$0
  printf "Enter a number (Ctrl-D to quit): "
}
END {
 print "BYE"
}
