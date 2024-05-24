// Dominik Szczepaniak
// lista8
// zadanie 2

class Dlugosc
    def initialize(kilometry)
        @kilometry = kilometry
    end

    def mile_morskie
        @kilometry / 1.852
    end

    def mile_morskie=(nmi)
        @kilometry = nmi * 1.852
    end
end

class Czas
    def initialize(godziny)
        @godziny = godziny
    end

    def sekundy
        @godziny * 3600
    end

    def sekundy=(sec)
        @godziny = sec / 3600.0
    end
end

class Predkosc
    def initialize(kmh)
        @kmh = kmh
    end

    def wezly
        @kmh / 1.852
    end

    def wezly=(knots)
        @kmh = knots * 1.852
    end
end


class Przyspieszenie
    def initialize(kms2)
        @kms2 = kms2
    end

    def mmh2
        @kms2 * 3.6e9
    end

    def mmh2=(mmh2)
        @kms2 = mmh2 / 3.6e9
    end
end


predkosci = [10, 50, 100] # km/h
puts "Km/h | Węzły"
predkosci.each do |kmh|
  speed = Predkosc.new(kmh)
  puts "#{kmh} km/h | #{speed.wezly.round(2)} węzłów"
end

przyspieszenia = [0.001, 0.005, 0.01] # km/s²
puts "Km/s² | Mm/h²"
przyspieszenia.each do |kms2|
  accel = Przyspieszenie.new(kms2)
  puts "#{kms2} km/s² | #{accel.mmh2.round(2)} mm/h²"
end
