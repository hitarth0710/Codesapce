import javax.swing.*;
import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;
import javax.swing.event.UndoableEditEvent;
import javax.swing.event.UndoableEditListener;
import javax.swing.text.BadLocationException;
import javax.swing.text.StyledDocument;
import javax.swing.undo.UndoManager;
import java.awt.*;
import java.awt.event.*;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import javax.swing.text.Style;
import javax.swing.text.StyleConstants;
import javax.swing.text.StyleContext;

public class App {
    public static void main(String[] args) {

        JFrame frame = new JFrame("Text Editor");
        JTextPane textPane = new JTextPane(); // Use JTextPane instead of JTextArea

        // Create a scroll pane to hold the text area
        JScrollPane scrollPane = new JScrollPane(textPane);
        scrollPane.setPreferredSize(new Dimension(500, 500));

        // Create a menu bar
        JMenuBar menuBar = new JMenuBar();

        // Create a menu
        JMenu menu = new JMenu("File");
        menuBar.add(menu);

        // Create a menu item for saving the text
        JMenuItem saveItem = new JMenuItem("Save");
        saveItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Create a file chooser
                JFileChooser fileChooser = new JFileChooser();
                int returnValue = fileChooser.showSaveDialog(null);
                if (returnValue == JFileChooser.APPROVE_OPTION) {
                    File selectedFile = fileChooser.getSelectedFile();
                    try {
                        // Save the text
                        PrintWriter out = new PrintWriter(new FileWriter(selectedFile));
                        out.println(textPane.getText());
                        out.close();
                    } catch (IOException ex) {
                        ex.printStackTrace();
                    }
                }
            }
        });
        saveItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_S, ActionEvent.CTRL_MASK));
        menu.add(saveItem);

        // Create a menu item for 'Save As'
        JMenuItem saveAsItem = new JMenuItem("Save As");
        saveAsItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Create a file chooser
                JFileChooser fileChooser = new JFileChooser();
                int returnValue = fileChooser.showSaveDialog(null);
                if (returnValue == JFileChooser.APPROVE_OPTION) {
                    File selectedFile = fileChooser.getSelectedFile();
                    try {
                        // Save the text
                        PrintWriter out = new PrintWriter(new FileWriter(selectedFile));
                        out.println(textPane.getText());
                        out.close();
                    } catch (IOException ex) {
                        ex.printStackTrace();
                    }
                }
            }
        });
        saveAsItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_S, ActionEvent.CTRL_MASK | ActionEvent.SHIFT_MASK));
        menu.add(saveAsItem);

        // Create a menu item for 'Open'
        JMenuItem openItem = new JMenuItem("Open");
        openItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Create a file chooser
                JFileChooser fileChooser = new JFileChooser();
                int returnValue = fileChooser.showOpenDialog(null);
                if (returnValue == JFileChooser.APPROVE_OPTION) {
                    File selectedFile = fileChooser.getSelectedFile();
                    try {
                        // Read the file and set the text of the textArea
                        String content = new String(Files.readAllBytes(selectedFile.toPath()));
                        textPane.setText(content);
                    } catch (IOException ex) {
                        ex.printStackTrace();
                    }
                }
            }
        });
        openItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_O, ActionEvent.CTRL_MASK));
        menu.add(openItem);

        // Add the menu bar to the frame
        frame.setJMenuBar(menuBar);

        // Add the scroll pane to the frame
        frame.add(scrollPane);

        // Set the default close operation and pack the frame
        frame.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
        frame.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent we) {
                int result = JOptionPane.showConfirmDialog(frame, "Do you want to save before exiting?", "Confirm Exit", JOptionPane.YES_NO_CANCEL_OPTION);
                switch (result) {
                    case JOptionPane.YES_OPTION:
                        saveItem.doClick(); // simulate a click on the save button
                        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                        break;
                    case JOptionPane.NO_OPTION:
                        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                        break;
                    case JOptionPane.CANCEL_OPTION:
                        frame.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
                        break;
                }
            }
        });
        frame.pack();

        // Show the frame
        frame.setVisible(true);

        UndoManager undoManager = new UndoManager();
        textPane.getDocument().addUndoableEditListener(new UndoableEditListener() {
            public void undoableEditHappened(UndoableEditEvent e) {
                undoManager.addEdit(e.getEdit());
            }
        });

        // Create a menu item for 'Undo'
        JMenuItem undoItem = new JMenuItem("Undo");
        undoItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (undoManager.canUndo()) {
                    undoManager.undo();
                }
            }
        });
        undoItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_Z, ActionEvent.CTRL_MASK));
        menu.add(undoItem);

        // Create a menu item for 'Redo'
        JMenuItem redoItem = new JMenuItem("Redo");
        redoItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (undoManager.canRedo()) {
                    undoManager.redo();
                }
            }
        });
        redoItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_Y, ActionEvent.CTRL_MASK));
        menu.add(redoItem);

    }
}

class SyntaxHighlighter {
    private static final String[] JAVA_KEYWORDS = {
        "abstract", "assert", "boolean", "break", "byte", "case", "catch", "char", "class", "const",
        "continue", "default", "do", "double", "else", "enum", "extends", "final", "finally", "float",
        "for", "goto", "if", "implements", "import", "instanceof", "int", "interface", "long", "native",
        "new", "package", "private", "protected", "public", "return", "short", "static", "strictfp", "super",
        "switch", "synchronized", "this", "throw", "throws", "transient", "try", "void", "volatile", "while"
    };

    public static void applySyntaxHighlighting(JTextPane textPane) {
        try {
            StyledDocument doc = textPane.getStyledDocument();
            Style defaultStyle = StyleContext.getDefaultStyleContext().getStyle(StyleContext.DEFAULT_STYLE);
            Style keywordStyle = doc.addStyle("keywordStyle", defaultStyle);
            StyleConstants.setForeground(keywordStyle, Color.BLUE);

            doc.setCharacterAttributes(0, doc.getLength(), defaultStyle, true);

            for (String keyword : JAVA_KEYWORDS) {
                int pos = 0;
                while ((pos = doc.getText(0, doc.getLength()).indexOf(keyword, pos)) >= 0) {
                    doc.setCharacterAttributes(pos, keyword.length(), keywordStyle, true);
                    pos += keyword.length();
                }
            }
        } catch (BadLocationException ex) {
            ex.printStackTrace();
        }
    }
}