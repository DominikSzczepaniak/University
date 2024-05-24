// Dominik Szczepaniak
// lista8
// zadanie 1

class Masa
    def initialize(kg)
      @kilogramy = kg
    end

    def funty
      @kilogramy * 2.20462
    end

    def funty=(lbs)
      @kilogramy = lbs / 2.20462
    end
end


class Dlugosc
    def initialize(m)
      @metry = m
    end

    def stopy
      @metry * 3.28084
    end

    def stopy=(ft)
      @metry = ft / 3.28084
    end
end

class Powierzchnia
    def initialize(hektary)
      @hektary = hektary
    end

    def cale_kwadratowe
      @hektary * 15500031.0
    end

    def cale_kwadratowe=(sqin)
      @hektary = sqin / 15500031.0
    end
end


class Cisnienie
    def initialize(bary)
      @bary = bary
    end

    def psi
      @bary * 14.5038
    end

    def psi=(psi)
      @bary = psi / 14.5038
    end
end


powierzchnie = [1, 0.5, 2]
puts "Hektary | Cale kwadratowe"
powierzchnie.each do |hektar|
area = Powierzchnia.new(hektar)
puts "#{hektar} | #{area.cale_kwadratowe.round(2)}"
end

cisnienia = [1, 0.5, 2]
puts "Bary | PSI"
cisnienia.each do |bar|
pressure = Cisnienie.new(bar)
puts "#{bar} | #{pressure.psi.round(2)}"
end
