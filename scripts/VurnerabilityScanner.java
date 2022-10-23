// import java.net.*;
//
// class PortScanner {
//    public static void main(String []args) {
//       for (int port = 1; port <= 65535; port++) {
//          try {
//             Socket socket = new Socket();
//             socket.connect(new InetSocketAddress("localhost", port), 1000);
//             socket.close();
//             System.out.println("Port " + port + " is open");
//         } catch (Exception ex) {
//         }
//       }
//    }
// }
//
import java.io.*;
import java.net.*;

public class URLConnectionAuthReader {
  public static void main(String args[]) throws MalformedURLException, IOException {

    String urlString = "http://some.host.name.com";
    String username = "myname";
    String password = "mypassword";
    Authenticator.setDefault(new MyAuthenticator(username, password));

    URL url = new URL(urlString);
    InputStream content = (InputStream) url.getContent();
    InputStreamReader isr = new InputStreamReader(content);
    BufferedReader in = new BufferedReader(isr);

    String line;
    while ((line = in.readLine()) != null) {
      System.out.println(line);
    }
    System.out.println("Done.");
  }

  static class MyAuthenticator extends Authenticator {
    private String username, password;

    public MyAuthenticator(String username, String password) {
      this.username = username;
      this.password = password;
    }

    protected PasswordAuthentication getPasswordAuthentication() {
      System.out.println("Requesting Host  : " + getRequestingHost());
      System.out.println("Requesting Port  : " + getRequestingPort());
      System.out.println("Requesting Prompt : " + getRequestingPrompt());
      System.out.println("Requesting Protocol: " + getRequestingProtocol());
      System.out.println("Requesting Scheme : " + getRequestingScheme());
      System.out.println("Requesting Site  : " + getRequestingSite());
      return new PasswordAuthentication(username, password.toCharArray());
    }
  }
}

