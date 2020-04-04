# The nato alphabet in a ruby hash class
nato_alphabet = {
    "a" => "alpha",
    "b" => "bravo",
    "c" => "charlie",
    "d" => "delta",
    "e" => "echo",
    "f" => "foxtrot",
    "g" => "golf",
    "h" => "hotel",
    "i" => "india",
    "j" => "juliet",
    "k" => "kilo",
    "l" => "lima",
    "m" => "mike",
    "n" => "november",
    "o" => "oscar",
    "p" => "papa",
    "q" => "quebec",
    "r" => "romeo",
    "s" => "sierra",
    "t" => "tango",
    "u" => "uniform",
    "v" => "victor",
    "w" => "whiskey",
    "x" => "x-ray",
    "y" => "yankee",
    "z" => "zulu",
}

puts
nato_alphabet.each do |letter, word|
    puts("#{letter}: #{word}")
end