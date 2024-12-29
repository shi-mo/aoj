def grade(m, f, r)
  mf = m + f
  return 'F' if -1 == m || -1 == f
  return 'A' if 80 <= mf
  return 'B' if 65 <= mf
  return 'C' if 50 <= mf

  if 30 <= mf
    return (50 <= r) ? 'C' : 'D'
  end

  'F'
end

while s = gets
  m, f, r = s.split.map(&:to_i)
  exit 0 if [-1, -1, -1] == [m, f, r]

  puts grade(m, f, r)
end
