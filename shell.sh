aa=start

if [ $1 = $aa ]
then
  echo started
  
  lxterminal -e python ./sec.py
  lxterminal -e python ./timealert.py
  lxterminal -e python ./aaaa.py
  lxterminal -e python ./ai.py
fi
