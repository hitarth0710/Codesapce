import java.io.*;
import java.net.*;

public class EchoClient {
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket("localhost", 6000);
        System.out.println("Connected to the server");

        OutputStream output = socket.getOutputStream();
        PrintWriter writer = new PrintWriter(output, true);

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            System.out.println("Enter message: ");
            String message = reader.readLine();
            writer.println(message);

            InputStream input = socket.getInputStream();
            BufferedReader response = new BufferedReader(new InputStreamReader(input));

            String serverResponse;
            if ((serverResponse = response.readLine()) != null) {
                System.out.println(serverResponse);
            }
        }
    }
}