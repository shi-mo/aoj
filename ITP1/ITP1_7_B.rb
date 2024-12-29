while s = gets
  n, x = s.split.map(&:to_i)
  exit 0 if 0 == n && 0 == x

  c = 0
  [n, x].min.downto(3) do |k|
    ij = x - k
    next if ij < 3

    (k-1).downto(2) do |j|
      i = ij - j
      next if j <= i || i <= 0
      c += 1
    end
  end
  puts c
end
