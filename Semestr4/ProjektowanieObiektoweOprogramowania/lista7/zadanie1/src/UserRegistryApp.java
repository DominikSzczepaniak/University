import javax.swing.*;
import javax.swing.tree.DefaultMutableTreeNode;
import javax.swing.tree.DefaultTreeModel;
import javax.swing.tree.TreePath;
import javax.swing.tree.TreeSelectionModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;
import java.util.function.Consumer;

class EventAggregator {
    private Map<Class<?>, Set<Consumer<Object>>> subscribers = new HashMap<>();

    public <T> void subscribe(Class<T> eventType, Consumer<T> subscriber) {
        subscribers.computeIfAbsent(eventType, k -> new HashSet<>()).add((Consumer<Object>) subscriber);
    }

    public <T> void unsubscribe(Class<T> eventType, Consumer<T> subscriber) {
        subscribers.getOrDefault(eventType, new HashSet<>()).remove(subscriber);
    }

    public <T> void publish(T event) {
        Set<Consumer<Object>> consumers = subscribers.getOrDefault(event.getClass(), Collections.emptySet());
        for (Consumer<Object> consumer : consumers) {
            consumer.accept(event);
        }
    }
}

class CategorySelectedEvent {
    public DefaultMutableTreeNode categoryNode;

    public CategorySelectedEvent(DefaultMutableTreeNode categoryNode) {
        this.categoryNode = categoryNode;
    }
}

class UserSelectedEvent {
    public Person person;

    public UserSelectedEvent(Person person) {
        this.person = person;
    }
}

class UserUpdatedEvent {
    public DefaultMutableTreeNode node;
    public Person updatedPerson;

    public UserUpdatedEvent(DefaultMutableTreeNode node, Person updatedPerson) {
        this.node = node;
        this.updatedPerson = updatedPerson;
    }
}

class UserAddedEvent {
    public DefaultMutableTreeNode categoryNode;
    public Person newPerson;

    public UserAddedEvent(DefaultMutableTreeNode categoryNode, Person newPerson) {
        this.categoryNode = categoryNode;
        this.newPerson = newPerson;
    }
}

public class UserRegistryApp extends JFrame {
    private JTree categoryTree;
    private DefaultTreeModel treeModel;
    private JTextArea detailArea;
    private EventAggregator eventAggregator;
    private JButton addButton, editButton;

    public UserRegistryApp() {
        super("User Management System");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());
        eventAggregator = new EventAggregator();

        setupCategoryTree();
        setupDetailArea();

        setSize(1000, 600);
        setLocationRelativeTo(null);
        setVisible(true);

        eventAggregator.subscribe(CategorySelectedEvent.class, this::onCategorySelected);
        eventAggregator.subscribe(UserSelectedEvent.class, this::onUserSelected);
        eventAggregator.subscribe(UserUpdatedEvent.class, this::onUserUpdated);
        eventAggregator.subscribe(UserAddedEvent.class, this::onUserAdded);
    }

    private void setupCategoryTree() {
        DefaultMutableTreeNode root = new DefaultMutableTreeNode("Categories");
        DefaultMutableTreeNode students = new DefaultMutableTreeNode("Students");
        DefaultMutableTreeNode lecturers = new DefaultMutableTreeNode("Lecturers");
        root.add(students);
        root.add(lecturers);

        treeModel = new DefaultTreeModel(root);
        categoryTree = new JTree(treeModel);
        categoryTree.getSelectionModel().setSelectionMode(TreeSelectionModel.SINGLE_TREE_SELECTION);
        categoryTree.addTreeSelectionListener(e -> {
            DefaultMutableTreeNode selectedNode = (DefaultMutableTreeNode) categoryTree.getLastSelectedPathComponent();
            if (selectedNode != null) {
                if (selectedNode.getUserObject() instanceof Person) {
                    eventAggregator.publish(new UserSelectedEvent((Person) selectedNode.getUserObject()));
                } else {
                    eventAggregator.publish(new CategorySelectedEvent(selectedNode));
                }
            }
        });

        addButton = new JButton("Add User");
        addButton.addActionListener(this::displayAddUserDialog);
        editButton = new JButton("Edit User");
        editButton.setEnabled(false);
        editButton.addActionListener(this::displayEditUserDialog);

        JPanel bottomPanel = new JPanel();
        bottomPanel.add(addButton);
        bottomPanel.add(editButton);

        add(new JScrollPane(categoryTree), BorderLayout.WEST);
        add(bottomPanel, BorderLayout.SOUTH);
    }

    private void setupDetailArea() {
        detailArea = new JTextArea(10, 30);
        detailArea.setEditable(false);
        add(new JScrollPane(detailArea), BorderLayout.CENTER);
    }

    private void displayAddUserDialog(ActionEvent e) {
        DefaultMutableTreeNode selectedCategory = (DefaultMutableTreeNode) categoryTree.getLastSelectedPathComponent();
        if (selectedCategory == null || selectedCategory.getUserObject() instanceof Person) {
            JOptionPane.showMessageDialog(this, "Please select a category to add a user.");
            return;
        }

        JTextField firstNameField = new JTextField();
        JTextField lastNameField = new JTextField();
        JTextField birthDateField = new JTextField();
        JTextField addressField = new JTextField();

        JPanel panel = new JPanel(new GridLayout(0, 2));
        panel.add(new JLabel("First Name:"));
        panel.add(firstNameField);
        panel.add(new JLabel("Last Name:"));
        panel.add(lastNameField);
        panel.add(new JLabel("Birth Date (dd-MM-yyyy):"));
        panel.add(birthDateField);
        panel.add(new JLabel("Address:"));
        panel.add(addressField);

        int result = JOptionPane.showConfirmDialog(null, panel, "Enter new user details", JOptionPane.OK_CANCEL_OPTION, JOptionPane.PLAIN_MESSAGE);
        if (result == JOptionPane.OK_OPTION) {
            try {
                SimpleDateFormat sdf = new SimpleDateFormat("dd-MM-yyyy");
                Date birthDate = sdf.parse(birthDateField.getText());
                Person newPerson = new Person(firstNameField.getText(), lastNameField.getText(), birthDate, addressField.getText());
                eventAggregator.publish(new UserAddedEvent(selectedCategory, newPerson));
            } catch (ParseException ex) {
                JOptionPane.showMessageDialog(null, "Invalid date format. Please use dd-MM-yyyy.");
            }
        }
    }

    private void displayEditUserDialog(ActionEvent e) {
        DefaultMutableTreeNode selectedUserNode = (DefaultMutableTreeNode) categoryTree.getLastSelectedPathComponent();
        if (selectedUserNode == null || !(selectedUserNode.getUserObject() instanceof Person)) {
            JOptionPane.showMessageDialog(this, "Please select a user to edit.");
            return;
        }
        Person person = (Person) selectedUserNode.getUserObject();

        JTextField firstNameField = new JTextField(person.firstName);
        JTextField lastNameField = new JTextField(person.lastName);
        JTextField birthDateField = new JTextField(new SimpleDateFormat("dd-MM-yyyy").format(person.birthDate));
        JTextField addressField = new JTextField(person.address);

        JPanel panel = new JPanel(new GridLayout(0, 2));
        panel.add(new JLabel("First Name:"));
        panel.add(firstNameField);
        panel.add(new JLabel("Last Name:"));
        panel.add(lastNameField);
        panel.add(new JLabel("Birth Date (dd-MM-yyyy):"));
        panel.add(birthDateField);
        panel.add(new JLabel("Address:"));
        panel.add(addressField);

        int result = JOptionPane.showConfirmDialog(null, panel, "Edit user details", JOptionPane.OK_CANCEL_OPTION, JOptionPane.PLAIN_MESSAGE);
        if (result == JOptionPane.OK_OPTION) {
            try {
                SimpleDateFormat sdf = new SimpleDateFormat("dd-MM-yyyy");
                person.birthDate = sdf.parse(birthDateField.getText());
                person.firstName = firstNameField.getText();
                person.lastName = lastNameField.getText();
                person.address = addressField.getText();
                eventAggregator.publish(new UserUpdatedEvent(selectedUserNode, person));
            } catch (ParseException ex) {
                JOptionPane.showMessageDialog(null, "Invalid date format. Please use dd-MM-yyyy.");
            }
        }
    }

    private void onCategorySelected(CategorySelectedEvent event) {
        detailArea.setText("Category: " + event.categoryNode.getUserObject().toString() + " selected. Please select a user or add a new user to this category.");
        editButton.setEnabled(false);
    }

    private void onUserSelected(UserSelectedEvent event) {
        detailArea.setText(event.person.getDetails());
        editButton.setEnabled(true);
    }

    private void onUserUpdated(UserUpdatedEvent event) {
        event.node.setUserObject(event.updatedPerson);
        treeModel.nodeChanged(event.node);
        detailArea.setText(event.updatedPerson.getDetails());
    }

    private void onUserAdded(UserAddedEvent event) {
        DefaultMutableTreeNode newUserNode = new DefaultMutableTreeNode(event.newPerson);
        event.categoryNode.add(newUserNode);
        treeModel.nodesWereInserted(event.categoryNode, new int[]{event.categoryNode.getIndex(newUserNode)});
        categoryTree.expandPath(new TreePath(event.categoryNode.getPath()));
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(UserRegistryApp::new);
    }
}