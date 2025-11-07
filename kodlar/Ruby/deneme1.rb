puts("ilk kod sayılır bakalıom çalışçakmı")
a = 1
b = 3
puts(a + b)
if a > b 
  puts("hey")
else 
  puts("yeh")

  def hey (sayi = 1 , sayib = 2 , islem = "+")
    if islem == "+" 
      puts(sayi + sayib)
    elsif islem == "-"
      puts(sayi - sayib)
    elsif islem == "/"
      puts(sayi / sayib)
    else :
      puts(sayi * sayib)