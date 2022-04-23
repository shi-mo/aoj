while s = gets
    h, w = s.split.map(&:to_i)
    exit 0 if 0 == h && 0 == w

    1.upto(h) do |i|
      if i <= 1 || h <= i
        puts('#' * w)
        next
      end
      puts('#' + ('.'*(w-2)) + '#')
    end
    puts
end
