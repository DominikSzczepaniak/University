import java.util.ArrayList;
import java.util.List;
interface IShape {
    void draw();
}

interface IShapeFactoryWorker {
    boolean accepts(String shapeName);
    IShape create(Object... parameters);
}

class ShapeFactory {
    private List<IShapeFactoryWorker> workers = new ArrayList<>();

    public void registerWorker(IShapeFactoryWorker worker) {
        workers.add(worker);
    }

    public IShape createShape(String shapeName, Object... parameters) {
        for (IShapeFactoryWorker worker : workers) {
            if (worker.accepts(shapeName)) {
                return worker.create(parameters);
            }
        }
        throw new IllegalArgumentException("Nieznany kształt: " + shapeName);
    }
}

class Square implements IShape {
    private int side;

    public Square(int side) {
        this.side = side;
    }

    @Override
    public void draw() {
        System.out.println("kwadrat o boku:" + side);
    }
}

class SquareFactoryWorker implements IShapeFactoryWorker {
    @Override
    public boolean accepts(String shapeName) {
        return "Square".equalsIgnoreCase(shapeName);
    }

    @Override
    public IShape create(Object... parameters) {
        int side = (Integer) parameters[0];
        return new Square(side);
    }
}

//rozszerzamy o prostokat

class Rectangle implements IShape{
    private int width;
    private int height;

    public Rectangle(int w, int h){
        this.width = w;
        this.height = h;
    }

    @Override
    public void draw() {
        System.out.println("prostokat o wymiarach:" + width + " " + height);
    }
}

class RectangleFactoryWorker implements IShapeFactoryWorker{
    @Override
    public boolean accepts(String shapename){
        return "Rectangle".equalsIgnoreCase(shapename);
    }

    @Override
    public IShape create(Object... parameters){
        int width = (Integer) parameters[0];
        int height = (Integer) parameters[1];
        return new Rectangle(width, height);
    }
}


public class Main {
    public static void main(String[] args) {
        ShapeFactory factory = new ShapeFactory();
        factory.registerWorker(new SquareFactoryWorker());

        IShape square = factory.createShape("Square", 5);
        square.draw();

        factory.registerWorker(new RectangleFactoryWorker());
        IShape rect = factory.createShape("Rectangle", 3, 5);
        rect.draw();
    }
}