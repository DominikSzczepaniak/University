import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

abstract class Shape {
    int x, y, width, height;
    Color color;

    public Shape(int x, int y, int width, int height, Color color) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.color = color;
    }

    abstract public Shape clone();
    abstract void draw(Graphics g);

    boolean containsPoint(int x, int y) {
        return x >= this.x && x <= this.x + this.width && y >= this.y && y <= this.y + this.height;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Shape) {
            Shape other = (Shape) obj;
            return other.x == x && other.y == y && other.width == width && other.height == height && other.color.equals(color);
        }
        return false;
    }
}

class RectangleShape extends Shape {
    public RectangleShape(int x, int y, int width, int height, Color color) {
        super(x, y, width, height, color);
    }

    @Override
    public Shape clone() {
        return new RectangleShape(x, y, width, height, color);
    }

    @Override
    void draw(Graphics g) {
        g.setColor(color);
        g.fillRect(x, y, width, height);
    }
}

class OvalShape extends Shape {
    public OvalShape(int x, int y, int width, int height, Color color) {
        super(x, y, width, height, color);
    }

    @Override
    public Shape clone() {
        return new OvalShape(x, y, width, height, color);
    }

    @Override
    void draw(Graphics g) {
        g.setColor(color);
        g.fillOval(x, y, width, height);
    }
}

class SquareShape extends Shape {
    public SquareShape(int x, int y, int size, Color color) {
        super(x, y, size, size, color);
    }

    @Override
    public Shape clone() {
        return new SquareShape(x, y, width, color);
    }

    @Override
    void draw(Graphics g) {
        g.setColor(color);
        g.fillRect(x, y, width, width);
    }
}

class Memento {
    private Stack<List<Shape>> undoStack = new Stack<>();
    private Stack<List<Shape>> redoStack = new Stack<>();

    List<Shape> undo(List<Shape> currentState) {
        if (undoStack.isEmpty()) {
            throw new IllegalStateException("No more actions to undo");
        }
        redoStack.push(cloneList(currentState));
        return undoStack.pop();
    }

    List<Shape> redo(List<Shape> currentState) {
        if (redoStack.isEmpty()) {
            throw new IllegalStateException("No more actions to redo");
        }
        undoStack.push(cloneList(currentState));
        return redoStack.pop();
    }

    List<Shape> findDifferences(List<Shape> state){
        if(undoStack.empty()){
            return state;
        }
        List<Shape> top = undoStack.firstElement();
        List<Shape> diff = new ArrayList<>();
        for (int i = 0; i < Math.max(top.size(), state.size()); i++) {
            Shape topShape = i < top.size() ? top.get(i) : null;
            Shape stateShape = i < state.size() ? state.get(i) : null;
            if (stateShape == null || topShape == null || !topShape.equals(stateShape)) {
                if (stateShape != null) {
                    diff.add(stateShape.clone());
                }
            }
        }
        return diff;
    }

    void addUndo(List<Shape> state) {

        undoStack.push(cloneList(findDifferences(state)));
        redoStack.clear();
    }

    private List<Shape> cloneList(List<Shape> list) {
        List<Shape> newList = new ArrayList<>();
        for (Shape s : list) {
            newList.add(s.clone());
        }
        return newList;
    }
}


public class SimpleGraphicEditor extends JFrame {
    private List<Shape> shapes = new ArrayList<>();
    private Shape prototype;
    private String mode = "RECTANGLE";  // RECTANGLE, OVAL, SQUARE, MOVE, DELETE
    private final Memento memento = new Memento();
    private Shape selectedShape = null;
    private Point lastPoint = null;

    public SimpleGraphicEditor() {
        setTitle("Simple Graphic Editor");
        setSize(800, 600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        configureUI();
        setLocationRelativeTo(null);
        setVisible(true);
    }

    private void configureUI() {
        CanvasPanel canvas = new CanvasPanel();
        JPanel buttonsPanel = new JPanel();
        String[] modes = {"RECTANGLE", "OVAL", "SQUARE", "MOVE", "DELETE", "UNDO", "REDO"};
        for (String m : modes) {
            JButton btn = new JButton(m);
            btn.addActionListener(e -> {
                if ("UNDO".equals(m)) {
                    try {
                        shapes = memento.undo(new ArrayList<>(shapes));
                        canvas.repaint();
                    } catch (Exception ignored) {
                    }
                } else if ("REDO".equals(m)) {
                    try{
                        shapes = memento.redo(new ArrayList<>(shapes));
                        canvas.repaint();
                    } catch (Exception ignored){}
                } else {
                    mode = m;
                    updatePrototype();
                }
            });
            buttonsPanel.add(btn);
        }
        add(buttonsPanel, BorderLayout.NORTH);
        add(canvas, BorderLayout.CENTER);
    }

    private void updatePrototype() {
        switch (mode) {
            case "RECTANGLE":
                prototype = new RectangleShape(0, 0, 60, 40, Color.RED);
                break;
            case "OVAL":
                prototype = new OvalShape(0, 0, 60, 40, Color.GREEN);
                break;
            case "SQUARE":
                prototype = new SquareShape(0, 0, 40, Color.BLUE);
                break;
        }
    }

    class CanvasPanel extends JPanel {
        public CanvasPanel() {
            addMouseListener(new MouseAdapter() {
                @Override
                public void mousePressed(MouseEvent e) {
                    if ("MOVE".equals(mode) || "DELETE".equals(mode)) {
                        for (int i = shapes.size() - 1; i >= 0; i--) {
                            if (shapes.get(i).containsPoint(e.getX(), e.getY())) {
                                if ("DELETE".equals(mode)) {
                                    memento.addUndo(shapes);
                                    shapes.remove(i);
                                    repaint();
                                } else if ("MOVE".equals(mode)) {
                                    selectedShape = shapes.get(i);
                                    lastPoint = e.getPoint();
                                    selectedShape.x = lastPoint.x;
                                    selectedShape.y = lastPoint.y;
                                    memento.addUndo(shapes);
                                }
                                return;
                            }
                        }
                    } else {
                        memento.addUndo(shapes);
                        Shape newShape = prototype.clone();
                        newShape.x = e.getX() - newShape.width / 2;
                        newShape.y = e.getY() - newShape.height / 2;
                        shapes.add(newShape);
                        repaint();
                    }
                }

                @Override
                public void mouseReleased(MouseEvent e) {
                    if ("MOVE".equals(mode) && selectedShape != null && lastPoint != null) {
                        selectedShape = null;
                    }
                }
            });

            addMouseMotionListener(new MouseMotionAdapter() {
                @Override
                public void mouseDragged(MouseEvent e) {
                    if ("MOVE".equals(mode) && selectedShape != null && lastPoint != null) {
                        int dx = e.getX() - lastPoint.x;
                        int dy = e.getY() - lastPoint.y;
                        selectedShape.x += dx;
                        selectedShape.y += dy;
                        lastPoint = e.getPoint();
                        repaint();
                    }
                }
            });
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            for (Shape shape : shapes) {
                shape.draw(g);
            }
        }
    }

    public static void main(String[] args) {
        new SimpleGraphicEditor();
    }
}
