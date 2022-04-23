def main
  a, b, c = gets.chomp.split.map(&:to_i)
  d = divisors(c, a..b)
  puts d.size
end

def divisors(n, r)
  d = []
  r.min.upto(r.max) do |i|
    next if 0 < n % i
    d << i
  end
  d
end

main
