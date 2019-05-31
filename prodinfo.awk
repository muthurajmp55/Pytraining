#!/usr/bin/awk -f 

BEGIN {
  FS = "\t"
  lno = 1
  inValue = 0
}

{
  if (lno != 1) {
    print "========================"
    print "Product ID: ", $1
    print "Product Name: ", $2
    print "Unit Price: ", $3
    print "Available Quantity: ", $4
    print "========================"
    inValue += $3 * $4
  }
  lno++
}

END {
  print "There are ", lno - 1, " products in the inventory"
  print "The total stock value is Rs. ", inValue
  print "### DONE ###"
}

