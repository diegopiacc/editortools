#!/bin/sh

rm -rf tmp_pdf
mkdir tmp_pdf

pdfseparate "$1" tmp_pdf/out%d.pdf
cd tmp_pdf

fcount=$(ls *.pdf | wc -l)
echo "Working on $fcount pages..."
#for file in *; do

echo "Confronto «» () {} []"
for i in $(seq 1 $fcount); do

  #filetxt=echo $file | sed "s/pdf/$txt/g"
  filein="out$i.pdf"
  pdftotext $filein
  filetxt="out$i.txt"
#  echo "filenames: $filein $filetxt"

  cnt_open_1_caret=$(grep -Fo '“' $filetxt | wc -l)
  cnt_close_1_caret=$(grep -Fo '”' $filetxt | wc -l)
  diff_caret=$((cnt_open_1_caret-cnt_close_1_caret))
  old_diff_caret=$diff_caret
  if [ $cnt_open_1_caret -ne $cnt_close_1_caret ]; then
    echo "Trovata discrepanza: $cnt_open_1_caret '“' vs $cnt_close_1_caret '”' a pagina $i  "
  fi


  cnt_open_1_caret=$(grep -Fo '«' $filetxt | wc -l)
  cnt_close_1_caret=$(grep -Fo '»' $filetxt | wc -l)
  diff_caret=$((cnt_open_1_caret-cnt_close_1_caret))
  old_diff_caret=$diff_caret
  if [ $cnt_open_1_caret -ne $cnt_close_1_caret ]; then
    echo "Trovata discrepanza: $cnt_open_1_caret '«' vs $cnt_close_1_caret '»' a pagina $i  "
  fi

  cnt_open_1_paren=$(grep -Fo '(' $filetxt | wc -l)
  cnt_close_1_paren=$(grep -Fo ')' $filetxt | wc -l)
  diff_paren=$((cnt_open_1_paren-cnt_close_1_paren))
  old_diff_paren=$diff_paren
  if [ $cnt_open_1_paren -ne $cnt_close_1_paren ]; then
    echo "Trovata discrepanza: $cnt_open_1_paren '(' vs $cnt_close_1_paren ')' a pagina $i  "
  fi

  # cnt_open_1_pargf=$(grep -Fo '{' $filetxt | wc -l)
  # cnt_close_1_pargf=$(grep -Fo '}' $filetxt | wc -l)
  # diff_pargf=$((cnt_open_1_pargf-cnt_close_1_pargf))
  # old_diff_pargf=$diff_pargf
  # if [ $cnt_open_1_pargf -ne $cnt_close_1_pargf ]; then
  #   echo "Trovata discrepanza: $cnt_open_1_pargf '{' vs $cnt_close_1_pargf '}' a pagina $i  "
  # fi

  cnt_open_1_parsq=$(grep -Fo '[' $filetxt | wc -l)
  cnt_close_1_parsq=$(grep -Fo ']' $filetxt | wc -l)
  diff_caret=$((cnt_open_1_caret-cnt_close_1_caret))
  old_diff_caret=$diff_caret
  if [ $cnt_open_1_parsq -ne $cnt_close_1_parsq ]; then
    echo "Trovata discrepanza: $cnt_open_1_parsq '[' vs $cnt_close_1_parsq ']' a pagina $i  "
  fi

done

echo "done"
exit
