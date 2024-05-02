import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Random;
import java.net.URL;

public class RPC extends JFrame implements ActionListener {
    private JButton rockButton;
    private JButton paperButton;
    private JButton scissorsButton;
    private Random random;
    private int computerChoice;
    private int playerChoice;

    public RPC() {
        super("Rock-Paper-Scissors");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());

        URL rockURL = getClass().getResource("rock.jpg");
        URL paperURL = getClass().getResource("paper.jpg");
        URL scissorsURL = getClass().getResource("scissors.jpg");

             
        if (rockURL == null) {
            System.out.println("Could not find rock.jpg");
        }
        if (paperURL == null) {
            System.out.println("Could not find paper.jpg");
        }
        if (scissorsURL == null) {
            System.out.println("Could not find scissors.jpg");
        }

        this.setSize(200, 200);

        // Get the width and height of the frame
        int frameWidth = this.getWidth();
        int frameHeight = this.getHeight();
        
        // Calculate the desired width and height of the images
        int imageWidth = frameWidth / 4; // adjust as needed
        int imageHeight = frameHeight / 4; // adjust as needed
        
        // Load and scale images
        ImageIcon rockIcon = new ImageIcon(new ImageIcon(rockURL).getImage().getScaledInstance(imageWidth, imageHeight, Image.SCALE_DEFAULT));
        ImageIcon paperIcon = new ImageIcon(new ImageIcon(paperURL).getImage().getScaledInstance(imageWidth, imageHeight, Image.SCALE_DEFAULT));
        ImageIcon scissorsIcon = new ImageIcon(new ImageIcon(scissorsURL).getImage().getScaledInstance(imageWidth, imageHeight, Image.SCALE_DEFAULT));

        // Create buttons with images
        rockButton = new JButton(rockIcon);
        paperButton = new JButton(paperIcon);
        scissorsButton = new JButton(scissorsIcon);


        add(rockButton);
        add(paperButton);
        add(scissorsButton);

        random = new Random();

        computerChoice = 0;
        playerChoice = 0;

        rockButton.addActionListener(this);
        paperButton.addActionListener(this);
        scissorsButton.addActionListener(this);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == rockButton) {
            playerChoice = 1;
        } else if (e.getSource() == paperButton) {
            playerChoice = 2;
        } else if (e.getSource() == scissorsButton) {
            playerChoice = 3;
        }

        computerChoice = random.nextInt(3) + 1;

        displayResults();
    }

    private void displayResults() {
        String results = "";

        if (computerChoice == playerChoice) {
            results += "Tie!";
        } else if ((playerChoice == 1 && computerChoice == 2) ||
                   (playerChoice == 2 && computerChoice == 3) ||
                   (playerChoice == 3 && computerChoice == 1)) {
            results += "You Win!";
        } else {
            results += "Computer Wins!";
        }

        JOptionPane.showMessageDialog(null, results);
    }

    public static void main(String[] args) {
        RPC frame = new RPC();
        frame.setSize(300, 150);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}