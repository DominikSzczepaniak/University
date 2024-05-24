class Function2D
    def initialize(&block)
        @func = block
    end
  
    def value(x, y)
        @func.call(x, y)
    end
  
    def volume(a, b, c, d)
        n_x = 100  
        n_y = 100
        dx = (b - a) / n_x.to_f
        dy = (d - c) / n_y.to_f
        volume = 0.0
    
        n_x.times do |i|
            x = a + i * dx
            n_y.times do |j|
            y = c + j * dy
            volume += value(x, y) * dx * dy
            end
        end
        volume
    end
  
    def contour_line(a, b, c, d, height, precision = 0.01, step = 0.1)
        contour = []
        x = a
        while x <= b
            y = c
            while y <= d
                current_value = value(x, y)
                if (current_value - height).abs < precision
                    contour.push([x, y])
                end
                y += step
            end
            x += step
        end
            contour
        end
    end
  
f2d = Function2D.new { |x, y| Math.sin(x) * Math.cos(y) }

puts "Wartość funkcji w punkcie (π/2, π/3): #{f2d.value(Math::PI/2, Math::PI/3)}"
puts "Objętość pod wykresem na prostokącie [0, π] x [0, π]: #{f2d.volume(0, Math::PI, 0, Math::PI)}"
contour = f2d.contour_line(0, Math::PI, 0, Math::PI, 0.5, 0.05, 0.2)
puts "Linie poziomic na wysokości 0.5 dla zakresu [0, π] x [0, π]:"
contour.each { |point| puts point.inspect }