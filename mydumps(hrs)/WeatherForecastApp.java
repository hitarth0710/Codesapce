import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class WeatherForecastApp extends JFrame implements ActionListener {
    private JTextField locationField;
    private JButton searchButton;
    private JTextArea resultArea;

    public WeatherForecastApp() {
        setTitle("Weather Forecast App");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());

        JPanel topPanel = new JPanel(new FlowLayout());
        JLabel locationLabel = new JLabel("Enter Location:");
        locationField = new JTextField(20);
        searchButton = new JButton("Search");
        searchButton.addActionListener(this);

        topPanel.add(locationLabel);
        topPanel.add(locationField);
        topPanel.add(searchButton);

        add(topPanel, BorderLayout.NORTH);

        resultArea = new JTextArea(10, 30);
        resultArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(resultArea);
        add(scrollPane, BorderLayout.CENTER);
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == searchButton) {
            String location = locationField.getText();
            String weatherData = fetchWeatherData(location);
            displayWeatherData(weatherData);
        }
    }

    private void displayWeatherData(String weatherData) {
        resultArea.setText(weatherData);

        // Update background color based on weather condition
        if (weatherData.contains("Sunny")) {
            resultArea.setBackground(Color.YELLOW);
        } else if (weatherData.contains("Rainy")) {
            resultArea.setBackground(Color.BLUE);
        } else if (weatherData.contains("Cloudy")) {
            resultArea.setBackground(Color.GRAY);
        } else {
            // Default color for other conditions
            resultArea.setBackground(Color.WHITE);
        }
    }

    private String fetchWeatherData(String location) {
        try (BufferedReader reader = new BufferedReader(new FileReader("weather_data.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(",");
                if (parts.length >= 2 && parts[0].trim().equalsIgnoreCase(location.trim())) {
                    return "Location: " + parts[0].trim() + "\n" +
                            "Weather: " + parts[1].trim();
                }
            }
            return "Weather data not found for location: " + location;
        } catch (IOException ex) {
            return "Error: " + ex.getMessage();
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            WeatherForecastApp app = new WeatherForecastApp();
            app.setVisible(true);
        });
    }
}
