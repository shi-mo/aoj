NUM_BUILDINGS = 4
NUM_FLOORS = 3
NUM_ROOMS = 10

def main
  n = gets.to_i
  t = init_tenants

  n.times do
    b, f, r, v = gets.chomp.split.map(&:to_i)
    t[b-1][f-1][r-1] += v
  end

  print_tenants(t)
end

def init_tenants
  Array.new(NUM_BUILDINGS){
    Array.new(NUM_FLOORS){
      Array.new(NUM_ROOMS){ 0 }
    }
  }
end

def print_tenants(t)
  NUM_BUILDINGS.times do |bi|
    puts '#'*20 if 0 < bi
    NUM_FLOORS.times do |fi|
      NUM_ROOMS.times do |ri|
        print " #{t[bi][fi][ri]}"
      end
      puts
    end
  end
end

main
