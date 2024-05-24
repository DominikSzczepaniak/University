class Function
    def initialize(&block)
        @func = block
    end
  
    def value(x)
        @func.call(x)
    end
  
    def zero(a, b, e)
        while (b - a) > e
            m = (a + b) / 2.0
            val_m = value(m)
            return m if val_m.abs < e
            val_a = value(a)
            if val_a * val_m < 0
                b = m
            else
                a = m
            end
        end
        nil
    end
  
    def field(a, b)
        n = 1000
        width = (b - a) / n.to_f
        area = 0
        n.times do |i|
            x = a + i * width
            height = value(x)
            area += height * width
        end
        area.abs
    end
  
    def deriv(x)
        h = 0.00001
        (value(x + h) - value(x)) / h
    end
  end
  
f = Function.new { |x| x * x * Math.sin(x) }

puts "Wartość funkcji w punkcie pi: #{f.value(Math::PI)}"
puts "Miejsce zerowe na przedziale [2, 4] z dokładnością 0.001: #{f.zero(2, 4, 0.001)}"
puts "Pole powierzchni na przedziale [0, Math::PI]: #{f.field(0, Math::PI)}"
puts "Pochodna w punkcie pi: #{f.deriv(Math::PI)}"
