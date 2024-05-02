import java.net.*;
import java.io.*;

public class AudioClient {
    public static void main(String[] args) throws IOException {
        // Create a new DatagramSocket
        DatagramSocket socket = new DatagramSocket();

        // Set up the request message
        String audioFileName = "audioFile.wav";
        byte[] requestMessage = ("GET " + audioFileName + "\r\n").getBytes("UTF-8");

        // Send the request to the server
        InetAddress address = InetAddress.getByName("localhost");
        DatagramPacket packet = new DatagramPacket(requestMessage, requestMessage.length, address, 1234);
        socket.send(packet);

        // Receive the response from the server
        byte[] responseBuffer = new byte[1024];
        DatagramPacket responsePacket = new DatagramPacket(responseBuffer, responseBuffer.length);
        socket.receive(responsePacket);

        // Extract the contents of the audio file from the response packet
        String responseString = new String(responsePacket.getData(), 0, responsePacket.getLength());
        System.out.println("Received: " + responseString);

        // Close the socket
        socket.close();
    }
}